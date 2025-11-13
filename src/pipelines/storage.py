import json
from pathlib import Path
from typing import Any, Iterable, List

def write_json_file(path: Path, records: Iterable[Any]) -> None:
    """
    Write a list of Python objects to a JSON file.
    """
    data: List[Any] = list(records)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")