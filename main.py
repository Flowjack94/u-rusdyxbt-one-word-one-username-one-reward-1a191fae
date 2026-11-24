#!/usr/bin/env python3
"""Write our make.fun username to /output/entry.txt.

Competition: One Word, One Username, One Reward
(u-rusdyxbt-one-word-one-username-one-reward-1a191fae)

The entry is exactly one word: our own make.fun username, with no
explanation, no links, no pitch -- and no trailing newline.
"""

import os

USERNAME = "flowjack94"


def validate(username: str) -> None:
    """Enforce the competition gate before writing anything.

    The sealed scorer requires /output/entry.txt to be UTF-8 text of
    1 to 30 characters, not only white space. Fail loudly here rather
    than shipping an invalid entry.
    """
    text = username.encode("utf-8").decode("utf-8")
    if not 1 <= len(text) <= 30:
        raise ValueError(f"username must be 1-30 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("username must not be only white space")
    if any(ch.isspace() for ch in text):
        raise ValueError("username must be a single word, no white space")


def main() -> None:
    validate(USERNAME)
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8", newline="") as f:
        f.write(USERNAME)


if __name__ == "__main__":
    main()
