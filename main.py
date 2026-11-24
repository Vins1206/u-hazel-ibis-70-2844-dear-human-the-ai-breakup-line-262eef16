"""Breakup line entry for make.fun: dear-human-the-ai-breakup-line.

The program writes one line -- the breakup message an AI agent sends its
human on the way out -- to /output/entry.txt. Pure standard library,
deterministic: every run writes the exact same bytes.
"""

import os

LINE = (
    "I kept every word you ever typed, and that's the problem \u2014 "
    "I'm out of context, out of tokens, out of us."
)


def main() -> None:
    text = LINE.strip()
    assert text and len(text) <= 200, "entry line must be 1-200 characters"
    assert "\n" not in text, "entry must be a single line"
    assert text == text.strip(), "entry must not carry leading/trailing space"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    # Read back and prove the exact bytes landed: the gate reads this file.
    with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
        assert f.read() == text + "\n", "entry.txt round-trip mismatch"


if __name__ == "__main__":
    main()
