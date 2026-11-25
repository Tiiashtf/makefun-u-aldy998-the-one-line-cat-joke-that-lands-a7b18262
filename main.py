#!/usr/bin/env python3
"""The One-Line Cat Joke That Lands.

Writes a single one-line cat joke to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt).

The joke is a fixed string, so the program is deterministic and writes
the same bytes on every run. It clears only the *contents* of the output
directory -- never the directory itself -- so it also works when the
grader runs it with a root-owned output directory inside a sticky
parent directory.
"""

import os
import shutil

JOKE = (
    "My cat walked across my keyboard during a job interview, typed "
    "'mmmmmmmmmm', and got hired -- she starts Monday as my manager."
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")


def clear_contents(directory: str) -> None:
    """Remove everything inside `directory`, never the directory itself.

    Nested directories are removed recursively, symlinks are unlinked
    without being followed, and fifos/sockets are unlinked.
    """
    for name in os.listdir(directory):
        path = os.path.join(directory, name)
        if os.path.islink(path) or not os.path.isdir(path):
            os.unlink(path)
        else:
            shutil.rmtree(path)


def main() -> None:
    line = JOKE.strip()
    assert "\n" not in line, "joke must be a single line"
    assert 1 <= len(line) <= 199, "joke must be 1-199 characters"
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    clear_contents(OUTPUT_DIR)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as handle:
        handle.write(line + "\n")


if __name__ == "__main__":
    main()
