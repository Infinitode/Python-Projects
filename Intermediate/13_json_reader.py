#!/usr/bin/env python3
# Made By @Ericwasepic127
# JSON Reader - A simple CLI tool to read and pretty-print JSON files

import json
import sys
from pathlib import Path
from typing import Any, Optional

def read_json_file(file_path: Path) -> Optional[Any]:
    """Read and parse a JSON file."""
    if not file_path.is_file():
        print(f"ERROR: '{file_path}' is not a file or does not exist.", file=sys.stderr)
        return None

    try:
        with file_path.open(encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        print(f"ERROR: Invalid JSON format in '{file_path}': {e}", file=sys.stderr)
    except Exception as e:
        print(f"ERROR: Failed to read '{file_path}': {e}", file=sys.stderr)
    
    return None

def display_json(data: Any) -> None:
    """Display JSON content in a readable format."""
    if isinstance(data, dict):
        for key, value in data.items():
            print(f"Name: {key!r} | Value: {value!r}")
    elif isinstance(data, list):
        for i, item in enumerate(data):
            print(f"[{i}]: {item!r}")
    else:
        # For primitives like string, number, bool
        print(data)

def main() -> None:
    print("Welcome to JSON Reader")
    print("Type 'exit' to quit\n")
    print(f"Current directory: {Path.cwd()}")

    while True:
        try:
            loc = input("\nEnter path to your JSON file: ").strip()

            if loc.lower() in ("exit", "quit", "q"):
                print("Goodbye!")
                break

            if not loc:
                continue

            json_path = Path(loc).expanduser().resolve()
            data = read_json_file(json_path)

            if data is None:
                continue

            display_json(data)

        except (KeyboardInterrupt, EOFError):
            print("\nGoodbye!")
            break

if __name__ == "__main__":
    main()
