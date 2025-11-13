import re
from typing import Iterable, List

_REEL_URL_PATTERN = re.compile(
    r"^https://(www\.)?instagram\.com/(reels?|p)/[A-Za-z0-9_\-]+/?",
    re.IGNORECASE,
)

def is_valid_reel_url(url: str) -> bool:
    return bool(_REEL_URL_PATTERN.match(url.strip()))

def validate_input_urls(urls: Iterable[str]) -> List[str]:
    valid: List[str] = []
    invalid: List[str] = []
    for url in urls:
        cleaned = url.strip()
        if not cleaned:
            continue
        if is_valid_reel_url(cleaned):
            valid.append(cleaned)
        else:
            invalid.append(cleaned)

    if invalid:
        raise ValueError(f"Invalid Instagram Reel URLs: {', '.join(invalid)}")

    return valid