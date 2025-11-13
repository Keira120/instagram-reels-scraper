import logging
import os
from typing import Optional

def _get_log_level() -> int:
    level_name = os.getenv("IRS_LOG_LEVEL", "INFO").upper()
    return getattr(logging, level_name, logging.INFO)

def get_logger(name: Optional[str] = None) -> logging.Logger:
    logger = logging.getLogger(name or "instagram_reels_scraper")
    if not logger.handlers:
        logger.setLevel(_get_log_level())
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            fmt="%(asctime)s [%(levelname)s] %(name)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.propagate = False
    return logger