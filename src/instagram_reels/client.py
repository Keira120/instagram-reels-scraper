from datetime import datetime, timezone
from typing import Any, Dict, Optional
from urllib.parse import urlencode, urljoin

import requests

from config.settings import Settings, get_settings
from instagram_reels.validators import validate_input_urls
from utils.logging_utils import get_logger
from utils.retry import retry
from utils.time_utils import to_iso8601
from instagram_reels.rate_limiter import RateLimiter

class InstagramClient:
    """
    HTTP client responsible for talking to Instagram (via public oEmbed)
    and returning a canonical payload for each reel.
    """

    def __init__(
        self,
        settings: Optional[Settings] = None,
        session: Optional[requests.Session] = None,
        logger=None,
        rate_limiter: Optional[RateLimiter] = None,
    ) -> None:
        self.settings = settings or get_settings()
        self.session = session or requests.Session()
        self.logger = logger or get_logger(__name__)
        self.rate_limiter = rate_limiter or RateLimiter(self.settings.rate_limit_per_second)

    def _build_oembed_url(self, reel_url: str) -> str:
        base = self.settings.base_url.rstrip("/")
        endpoint = self.settings.oembed_endpoint
        if not endpoint.startswith("/"):
            endpoint = "/" + endpoint
        query = urlencode({"url": reel_url, "omitscript": "true"})
        return urljoin(base, endpoint) + f"?{query}"

    @retry(exceptions=(requests.RequestException,), tries=3, delay=1.0, backoff=2.0, logger=get_logger(__name__))
    def _fetch_oembed(self, reel_url: str) -> Dict[str, Any]:
        self.rate_limiter.wait()
        url = self._build_oembed_url(reel_url)
        self.logger.debug("Fetching oEmbed for reel: %s", reel_url)
        resp = self.session.get(
            url,
            timeout=self.settings.request_timeout,
            headers={"User-Agent": self.settings.user_agent},
            verify=self.settings.verify_ssl,
        )
        resp.raise_for_status()
        return resp.json()

    def _canonicalize_payload(self, reel_url: str, oembed_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Map oEmbed data into the canonical payload structure expected by the parser.
        Many analytics fields are not available via oEmbed, so we populate
        them with sensible defaults (e.g., zeros) while keeping structure ready
        for downstream analysis.
        """
        now_iso = to_iso8601(datetime.now(timezone.utc))
        description = oembed_data.get("title") or ""
        author_name = oembed_data.get("author_name") or ""
        thumbnail_url = oembed_data.get("thumbnail_url") or ""

        shortcode = reel_url.rstrip("/").split("/")[-1]

        payload: Dict[str, Any] = {
            "url": reel_url,
            "user_posted": author_name,
            "description": description,
            "hashtags": [],  # will be derived from description by parser if empty
            "num_comments": 0,
            "date_posted": now_iso,
            "likes": 0,
            "views": 0,
            "video_play_count": 0,
            "top_comments": [],
            "post_id": "",
            "thumbnail": thumbnail_url,
            "shortcode": shortcode,
            "content_id": "",
            "product_type": "clips",
            "coauthor_producers": [],
            "tagged_users": [],
            "length": "0",
            "video_url": reel_url,
            "audio_url": None,
            "posts_count": 0,
            "followers": 0,
            "following": 0,
        }
        return payload

    def fetch_reel_metadata(self, reel_url: str) -> Dict[str, Any]:
        """
        Public entrypoint: validate URL, fetch oEmbed, and return canonical payload.
        """
        (validated_url,) = validate_input_urls([reel_url])
        oembed_data = self._fetch_oembed(validated_url)
        payload = self._canonicalize_payload(validated_url, oembed_data)
        self.logger.info("Fetched metadata for reel: %s", validated_url)
        return payload

    def fetch_many(self, reel_urls: list[str]) -> list[Dict[str, Any]]:
        """
        Fetch metadata for multiple reels sequentially.
        """
        validated = validate_input_urls(reel_urls)
        results: list[Dict[str, Any]] = []
        for url in validated:
            try:
                results.append(self.fetch_reel_metadata(url))
            except Exception as exc:  # noqa: BLE001
                self.logger.error("Failed to fetch %s: %s", url, exc)
        return results