#!/usr/bin/env python3
"""One-Line Office Joke: 24-Hour Sprint entry.

Writes one original one-line joke about office life
(under 200 characters) to /output/entry.txt.
"""
import os
import sys

JOKE = (
    "I showed up five minutes late to the meeting and still caught "
    "the part where absolutely nothing got decided."
)


def check_line(text):
    """Guard: the joke must be one non-blank line of 1-200 chars."""
    if not text or not text.strip():
        raise SystemExit("joke must not be blank")
    if "\n" in text or "\r" in text:
        raise SystemExit("joke must be a single line")
    if len(text) > 200:
        raise SystemExit("joke must be at most 200 characters")
    return text


def main():
    line = check_line(JOKE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
