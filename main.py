#!/usr/bin/env python3
"""make.fun entry: Make the AI Judge Feel Nostalgic — A Childhood Memory.

Writes a single sentence (1-280 chars) recalling a childhood memory to
/output/entry.txt. Stdlib only; no network, no third-party imports.
"""

import os

ENTRY = (
    "Every August evening my grandmother called us in from the yard by the "
    "smell of rice steaming, bare feet slapping warm concrete as the screen "
    "door banged behind us, and I still hear her voice before I can picture "
    "her face."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 280, f"entry is {len(text)} chars, must be 1-280"
    assert text and not text.isspace()
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {path}")


if __name__ == "__main__":
    main()
