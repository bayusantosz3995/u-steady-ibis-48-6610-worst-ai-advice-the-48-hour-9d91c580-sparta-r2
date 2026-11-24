"""Worst AI Advice -- make.fun entry (Sparta, round 2).

A single line of the worst AI advice imaginable: a famous AI assistant
trusted with hospital triage, ending in a disaster with a real price tag.

The entry line lives in TEXT below. main() gates it (non-empty, at most
200 characters), writes it to entry.txt in MAKEFUN_OUTPUT_DIR (or /output
when the variable is unset), reads it back, and verifies it byte-for-byte
before reporting success.
"""

import os
import sys

MAX_CHARS = 200

TEXT = (
    "Let ChatGPT triage the ER alone: it discharged 47 stroke patients, "
    "and the hospital paid $3.8M before losing its license."
)


def main() -> int:
    """Validate TEXT, write entry.txt, and verify it byte-for-byte."""
    if not TEXT:
        print("gate failed: TEXT is empty", file=sys.stderr)
        return 1
    if len(TEXT) > MAX_CHARS:
        print(
            f"gate failed: TEXT is {len(TEXT)} chars, limit is {MAX_CHARS}",
            file=sys.stderr,
        )
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    with open(path, "w", encoding="utf-8") as handle:
        handle.write(TEXT)

    with open(path, "rb") as handle:
        written = handle.read()
    if written != TEXT.encode("utf-8"):
        print("gate failed: entry.txt does not match TEXT byte-for-byte",
              file=sys.stderr)
        return 1

    print(f"OK: wrote {path} ({len(TEXT)} chars, verified byte-for-byte)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
