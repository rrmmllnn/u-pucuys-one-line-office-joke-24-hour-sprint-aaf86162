#!/usr/bin/env python3
"""One-Line Office Joke: 24-Hour Sprint entry.

Writes a single original one-line joke about office life
(under 200 characters) to /output/entry.txt.
"""
import os

LINE = (
    "My boss told me to think outside the box, so I moved my desk "
    "into the hallway and now facilities thinks I'm a fire hazard."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
