import sys
from pathlib import Path
from typing import Any, Dict, List

import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = PROJECT_ROOT / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from pipelines import runner  # type: ignore  # noqa: E402
from instagram_reels.parser import parse_reel_payload  # type: ignore  # noqa: E402

SAMPLE_PAYLOAD: Dict[str, Any] = {
    "url": "https://www.instagram.com/p/DDb5uxNyWa9/",
    "user_posted": "gaung_merah",
    "description": "Short description #Hashtag",
    "hashtags": [],
    "num_comments": 1,
    "date_posted": "2024-12-11T11:15:29.000Z",
    "likes": 10,
    "views": 100,
    "video_play_count": 120,
    "top_comments": [],
    "post_id": "3520661436311889597",
    "thumbnail": "https://example.com/thumb.jpg",
    "shortcode": "DDb5uxNyWa9",
    "content_id": "3520661436311889597_53789136377",
    "product_type": "clips",
    "coauthor_producers": [],
    "tagged_users": [],
    "length": "10.0",
    "video_url": "https://example.com/video.mp4",
    "audio_url": None,
    "posts_count": 1,
    "followers": 100,
    "following": 10,
}

class FakeClient:
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        self.calls: List[str] = []

    def fetch_reel_metadata(self, url: str) -> Dict[str, Any]:
        self.calls.append(url)
        return dict(SAMPLE_PAYLOAD, url=url)

def test_end_to_end_pipeline(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    monkeypatch.setattr(runner, "InstagramClient", FakeClient)  # type: ignore[attr-defined]

    output_file = tmp_path / "output.json"
    urls = ["https://www.instagram.com/p/DDb5uxNyWa9/"]
    results = runner.run_pipeline(urls, output_file=output_file)

    assert len(results) == 1
    record = results[0]
    assert record["url"] == urls[0]
    assert record["likes"] == 10
    assert record["followers"] == 100
    assert output_file.is_file()

def test_parser_integration() -> None:
    model = parse_reel_payload(SAMPLE_PAYLOAD)
    assert model.url == SAMPLE_PAYLOAD["url"]
    assert model.likes == 10
    assert "#Hashtag" in model.hashtags