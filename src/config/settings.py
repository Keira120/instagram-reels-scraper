import json
import os
from dataclasses import dataclass, fields
from functools import lru_cache
from pathlib import Path
from typing import Any, Dict

@dataclass
class Settings:
    base_url: str = "https://www.instagram.com"
    oembed_endpoint: str = "/oembed/"
    request_timeout: int = 15
    rate_limit_per_second: float = 1.0
    user_agent: str = "instagram-reels-scraper/1.0"
    verify_ssl: bool = True
    log_level: str = "INFO"

def _coerce_value(value: str, target_type: Any) -> Any:
    if target_type is bool:
        return str(value).strip().lower() in ("1", "true", "yes", "on")
    if target_type is int:
        return int(value)
    if target_type is float:
        return float(value)
    return value

def _apply_overrides(settings: Settings, overrides: Dict[str, Any]) -> Settings:
    field_map = {f.name: f for f in fields(Settings)}
    for key, value in overrides.items():
        if key in field_map:
            target_type = field_map[key].type
            if isinstance(value, str):
                value = _coerce_value(value, target_type)
            setattr(settings, key, value)
    return settings

def _load_json_config(path: Path) -> Dict[str, Any]:
    try:
        if path.is_file():
            return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        # Failing to load config should not crash the app; we'll use defaults.
        return {}
    return {}

@lru_cache(maxsize=1)
def get_settings() -> Settings:
    settings = Settings()

    # Optional JSON config file
    config_env = os.getenv("IRS_CONFIG_PATH")
    if config_env:
        config_path = Path(config_env)
    else:
        # Reasonable default config path (can be overridden by env)
        config_path = Path("src") / "config" / "settings.example.json"

    json_overrides = _load_json_config(config_path)
    settings = _apply_overrides(settings, json_overrides)

    # Environment variable overrides
    env_to_field = {
        "IRS_BASE_URL": "base_url",
        "IRS_OEMBED_ENDPOINT": "oembed_endpoint",
        "IRS_REQUEST_TIMEOUT": "request_timeout",
        "IRS_RATE_LIMIT_PER_SECOND": "rate_limit_per_second",
        "IRS_USER_AGENT": "user_agent",
        "IRS_VERIFY_SSL": "verify_ssl",
        "IRS_LOG_LEVEL": "log_level",
    }
    env_overrides: Dict[str, Any] = {}
    for env_key, field_name in env_to_field.items():
        if env_key in os.environ:
            env_overrides[field_name] = os.environ[env_key]

    settings = _apply_overrides(settings, env_overrides)
    return settings