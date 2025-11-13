import time
from functools import wraps
from typing import Any, Callable, Iterable, Optional, Type

def retry(
    exceptions: Iterable[Type[BaseException]],
    tries: int = 3,
    delay: float = 1.0,
    backoff: float = 2.0,
    logger: Optional[Any] = None,
) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """
    Retry decorator with exponential backoff.

    :param exceptions: Exception types to catch.
    :param tries: Total number of attempts.
    :param delay: Initial delay between attempts in seconds.
    :param backoff: Multiplier applied to delay after each failure.
    """

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            _tries, _delay = tries, delay
            while _tries > 1:
                try:
                    return func(*args, **kwargs)
                except tuple(exceptions) as exc:  # type: ignore[arg-type]
                    if logger:
                        logger.warning(
                            "Error in %s: %s. Retrying in %.2fs (%d tries left)...",
                            func.__name__,
                            exc,
                            _delay,
                            _tries - 1,
                        )
                    time.sleep(_delay)
                    _tries -= 1
                    _delay *= backoff
            # Last attempt, let exception propagate if it fails.
            return func(*args, **kwargs)

        return wrapper

    return decorator