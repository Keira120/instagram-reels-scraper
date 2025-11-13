from datetime import datetime, timezone
from typing import Optional

def parse_iso8601(value: str) -> datetime:
    """
    Parse an ISO 8601 timestamp into a timezone-aware datetime.
    Supports 'Z' suffix as UTC.
    """
    value = value.strip()
    if not value:
        return datetime.now(timezone.utc)
    if value.endswith("Z"):
        value = value[:-1] + "+00:00"
    try:
        dt = datetime.fromisoformat(value)
    except ValueError:
        # Fallback: return current UTC time if parsing fails.
        return datetime.now(timezone.utc)
    if dt.tzinfo is None:
        return dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)

def to_iso8601(dt: Optional[datetime] = None) -> str:
    if dt is None:
        dt = datetime.now(timezone.utc)
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc).isoformat().replace("+00:00", "Z")