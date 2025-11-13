import threading
import time
from dataclasses import dataclass

@dataclass
class RateLimiter:
    """
    Simple rate limiter enforcing a minimum interval between calls.

    rate_limit_per_second = 1.0  -> at most 1 request per second
    """

    rate_limit_per_second: float = 1.0

    def __post_init__(self) -> None:
        self._lock = threading.Lock()