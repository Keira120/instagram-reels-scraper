import sys
from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = PROJECT_ROOT / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from instagram_reels.client import InstagramClient  # type: ignore  # noqa: E402
from config.settings import Settings  # type: ignore  # noqa: E402

class DummyResponse:
    def __init__(self) -> None:
        self._json = {
            "title": "Example reel title #example",
            "author_name": "example_user",
            "thumbnail_url": "https://example.com/thumb.jpg",
        }

    def raise_for_status(self) -> None:
        return None

    def json(self) -> dict:
        return dict(self._json)

def test_build_oembed_url_contains_original_url() -> None:
    settings = Settings()
    client = InstagramClient(settings=settings)
    reel_url = "https://www.instagram.com/p/ABC123/"
    full_url = client._build_oembed_url(reel_url)  # type: ignore[attr-defined]
    assert "oembed" in full_url
    assert "url=https" in full_url

def test_fetch_reel_metadata_uses_oembed(monkeypatch: pytest.MonkeyPatch) -> None:
    settings = Settings()
    client = InstagramClient(settings=settings)

    def fake_get(url: str, timeout: int, headers: dict, verify: bool) -> DummyResponse:  # type: ignore[override]
        assert "oembed" in url
        return DummyResponse()

    monkeypatch.setattr(client.session, "get", fake_get)  # type: ignore[arg-type]
    data = client.fetch_reel_metadata("https://www.instagram.com/p/ABC123/")

    assert data["url"] == "https://www.instagram.com/p/ABC123/"
    assert data["user_posted"] == "example_user"
    assert data["thumbnail"] == "https://example.com/thumb.jpg"
    assert data["product_type"] == "clips"