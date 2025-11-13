from typing import Any, Dict, List

from pydantic import ValidationError

from instagram_reels.models import Reel, TopComment, TaggedUser
from utils.time_utils import parse_iso8601

def extract_hashtags(text: str) -> List[str]:
    if not text:
        return []
    words = text.split()
    return [w for w in words if w.startswith("#")]

def _parse_top_comments(raw_comments: List[Dict[str, Any]]) -> List[TopComment]:
    comments: List[TopComment] = []
    for item in raw_comments or []:
        try:
            comments.append(
                TopComment(
                    comment=item.get("comment", ""),
                    date_of_comment=parse_iso8601(item.get("date_of_comment", "")),
                    likes=int(item.get("likes", 0)),
                    num_replies=int(item.get("num_replies", 0)),
                    user_commenting=item.get("user_commenting", ""),
                    replies=item.get("replies", []) or [],
                )
            )
        except (ValueError, TypeError, ValidationError):
            # Skip malformed comment entries rather than failing the whole reel.
            continue
    return comments

def _parse_tagged_users(raw_users: List[Dict[str, Any]]) -> List[TaggedUser]:
    users: List[TaggedUser] = []
    for item in raw_users or []:
        try:
            users.append(
                TaggedUser(
                    id=str(item.get("id", "")),
                    username=item.get("username", ""),
                    full_name=item.get("full_name", None),
                    is_verified=bool(item.get("is_verified", False)),
                    profile_pic_url=item.get("profile_pic_url", None),
                )
            )
        except ValidationError:
            # Skip malformed tagged user entries.
            continue
    return users

def normalize_reel_payload(payload: Dict[str, Any]) -> Dict[str, Any]:
    """
    Normalize a raw payload into the canonical structure expected by Reel.
    This function is tolerant of missing fields and does best-effort coercion.
    """
    description = payload.get("description") or ""
    hashtags = payload.get("hashtags") or extract_hashtags(description)

    normalized = {
        "url": payload.get("url", ""),
        "user_posted": payload.get("user_posted", ""),
        "description": description,
        "hashtags": hashtags,
        "num_comments": int(payload.get("num_comments", 0) or 0),
        "date_posted": parse_iso8601(str(payload.get("date_posted", ""))),
        "likes": int(payload.get("likes", 0) or 0),
        "views": int(payload.get("views", 0) or 0),
        "video_play_count": int(payload.get("video_play_count", 0) or 0),
        "top_comments": _parse_top_comments(payload.get("top_comments") or []),
        "post_id": str(payload.get("post_id", "")),
        "thumbnail": payload.get("thumbnail", payload.get("thumbnail_url", "")),
        "shortcode": payload.get("shortcode", ""),
        "content_id": str(payload.get("content_id", "")),
        "product_type": payload.get("product_type", None),
        "coauthor_producers": payload.get("coauthor_producers", []) or [],
        "tagged_users": _parse_tagged_users(payload.get("tagged_users") or []),
        "length": float(payload.get("length", 0.0) or 0.0),
        "video_url": payload.get("video_url", payload.get("url", "")),
        "audio_url": payload.get("audio_url", None),
        "posts_count": int(payload.get("posts_count", 0) or 0),
        "followers": int(payload.get("followers", 0) or 0),
        "following": int(payload.get("following", 0) or 0),
    }
    return normalized

def parse_reel_payload(payload: Dict[str, Any]) -> Reel:
    """
    Parse a normalized or semi-normalized payload dict into a Reel model.
    """
    normalized = normalize_reel_payload(payload)
    # Pydantic v1/v2 compatibility: dict() is preserved as alias in v2.
    return Reel(**normalized)