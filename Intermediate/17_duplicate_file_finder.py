"""Find files with identical content without changing or deleting anything.

Run with: python Intermediate/17_duplicate_file_finder.py [directory]
"""

import argparse
import hashlib
import os
import sys
from collections import defaultdict
from pathlib import Path


def file_digest(path):
    """Hash a file in chunks so even large files need little memory."""
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for chunk in iter(lambda: source.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def find_duplicates(directory):
    """Return (duplicate groups, read errors) for regular files under directory.

    Only files sharing a size are hashed. Symbolic links are skipped to avoid
    scanning outside the chosen tree. No files are modified.
    """
    directory = Path(directory)
    if not directory.is_dir():
        raise ValueError("Not a directory: {}".format(directory))

    by_size = defaultdict(list)
    errors = []

    def walk_error(error):
        errors.append(str(error))

    for root, _, filenames in os.walk(str(directory), onerror=walk_error):
        for name in filenames:
            path = Path(root) / name
            if path.is_symlink():
                continue
            try:
                if path.is_file():
                    by_size[path.stat().st_size].append(path)
            except OSError as error:
                errors.append(str(error))

    duplicates = []
    for candidates in by_size.values():
        if len(candidates) < 2:
            continue
        by_digest = defaultdict(list)
        for path in candidates:
            try:
                by_digest[file_digest(path)].append(path)
            except OSError as error:
                errors.append(str(error))
        duplicates.extend(
            sorted(paths, key=str) for paths in by_digest.values() if len(paths) > 1
        )

    duplicates.sort(key=lambda paths: str(paths[0]))
    return duplicates, errors


def main():
    parser = argparse.ArgumentParser(description="List files with identical contents.")
    parser.add_argument("directory", nargs="?", default=".", help="folder to scan (default: current folder)")
    args = parser.parse_args()
    try:
        groups, errors = find_duplicates(args.directory)
    except ValueError as error:
        parser.error(str(error))

    if not groups:
        print("No duplicate files found.")
    else:
        for number, paths in enumerate(groups, 1):
            print("Group {}:".format(number))
            for path in paths:
                print("  {}".format(path))

    for error in errors:
        print("Could not read: {}".format(error), file=sys.stderr)
    if errors:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
