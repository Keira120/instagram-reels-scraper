from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional

from config.settings import get_settings
from instagram_reels.client import InstagramClient
from instagram_reels.parser import parse_reel_payload
from pipelines.exporters import JsonExporter
from pipelines.storage import write_json_file
from utils.logging_utils import get_logger

def run_pipeline(
    urls: Iterable[str],
    output_file: Optional[Path] = None,
) -> List[Dict[str, Any]]:
    """
    High-level orchestration of the scraping pipeline.
    1. Fetch metadata for each reel.
    2. Parse into Reel models.
    3. Export to JSON-serializable dicts.
    4. Optionally persist to disk.
    """
    logger = get_logger("instagram_reels_scraper.pipeline")
    settings = get_settings()
    client = InstagramClient(settings=settings, logger=logger)
    exporter = JsonExporter()

    reel_dicts: List[Dict[str, Any]] = []

    for url in urls:
        try:
            raw_payload = client.fetch_reel_metadata(url)
            reel_model = parse_reel_payload(raw_payload)
            reel_dicts.append(exporter.to_dict(reel_model))
        except Exception as exc:  # noqa: BLE001
            logger.error("Pipeline failed for %s: %s", url, exc)

    if output_file is not None:
        write_json_file(output_file, reel_dicts)
        logger.info("Wrote %d records to %s", len(reel_dicts), output_file)

    return reel_dicts