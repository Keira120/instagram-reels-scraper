import sys
from pathlib import Path

from cli import main as cli_main

def _ensure_project_root_on_path() -> None:
    """
    Ensure that the project root is on sys.path so that running
    `python src/main.py` works without additional configuration.
    """
    here = Path(__file__).resolve()
    project_root = here.parents[1]
    if str(project_root) not in sys.path:
        sys.path.insert(0, str(project_root))

def run() -> int:
    _ensure_project_root_on_path()
    return cli_main()

if __name__ == "__main__":
    raise SystemExit(run())