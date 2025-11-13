import argparse
import json
from pathlib import Path
from typing import List, Optional

from pipelines.runner import run_pipeline

def _read_urls_from_file(path: Path) -> List[str]:
    if not path.is_file():
        raise FileNotFoundError(f"Input file not found: {path}")
    urls: List[str] = []
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                urls.append(line)
    return urls

def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Instagram Reels Scraper - collect structured data from Instagram Reels URLs."
    )
    parser.add_argument(
        "-u",
        "--url",
        "--urls",
        dest="urls",
        nargs="*",
        help="One or more Instagram Reel URLs to scrape.",
    )
    parser.add_argument(
        "-i",
        "--input-file",
        dest="input_file",
        type=str,
        help="Path to a text file containing one URL per line.",
    )
    parser.add_argument(
        "-o",
        "--output",
        dest="output",
        type=str,
        help="Optional path to write JSON output. If omitted, prints to stdout.",
    )
    return parser

def parse_args(argv: Optional[List[str]] = None) -> argparse.Namespace:
    parser = build_arg_parser()
    return parser.parse_args(argv)

def main(argv: Optional[List[str]] = None) -> int:
    args = parse_args(argv)

    urls: List[str] = []
    if args.urls:
        urls.extend(args.urls)

    if args.input_file:
        file_urls = _read_urls_from_file(Path(args.input_file))
        urls.extend(file_urls)

    if not urls:
        raise SystemExit("No URLs provided. Use --url or --input-file.")

    output_path: Optional[Path] = Path(args.output) if args.output else None
    results = run_pipeline(urls, output_file=output_path)

    if output_path is None:
        print(json.dumps(results, ensure_ascii=False, indent=2))

    return 0