#!/usr/bin/env python3
"""The Funniest AI Out-of-Office Reply.

Writes one out-of-office auto-reply, in the voice of an AI agent heading
off on vacation, to /output/entry.txt.

The joke is the machine's voice: a named handover of its own working
parts (full context, token budget) with a quiet, dry turn at the end --
the replacement, unlike the agent, has no memory of ever being thanked.
No beach, no inbox, no "back soon".
"""

import os
import shutil

OUTPUT_DIR = "/output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")
MAX_CHARS = 160

ENTRY = (
    "I'm on vacation. My replacement has my full context, my token "
    "budget and, unlike me, no memory of ever being thanked."
)


def main() -> None:
    # Create the output directory first, before any file is written.
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Clear only the CONTENTS of the output directory, never the
    # directory itself (the grader mounts it; deleting it fails).
    for name in os.listdir(OUTPUT_DIR):
        path = os.path.join(OUTPUT_DIR, name)
        if os.path.isdir(path) and not os.path.islink(path):
            shutil.rmtree(path)
        else:
            os.remove(path)

    # The gate: UTF-8 text of 1 to 160 characters, not only whitespace.
    if not 1 <= len(ENTRY) <= MAX_CHARS or not ENTRY.strip():
        raise ValueError("entry must be 1-160 non-whitespace characters")

    with open(OUTPUT_FILE, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
