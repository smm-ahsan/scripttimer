#!/usr/bin/env python3
"""ScriptTimer - estimate how long a video or speech script takes to deliver.

Reads a script from --text or --file, counts the words, and reports how long
it takes to speak at slow, normal and fast rates, plus a per-section
breakdown (sections are separated by blank lines).

Standard library only.
"""

import argparse
import re
import sys

RATES = [
    ("Slow", 120),
    ("Normal", 150),
    ("Fast", 180),
]

NORMAL_WPM = 150


def format_duration(words, wpm):
    """Return the speaking time for `words` at `wpm` formatted as M:SS."""
    total_seconds = round(words / wpm * 60)
    minutes, seconds = divmod(total_seconds, 60)
    return f"{minutes}:{seconds:02d}"


def split_sections(text):
    """Split text into sections on blank lines, dropping empty parts."""
    parts = re.split(r"\n\s*\n", text.strip())
    return [part for part in parts if part.strip()]


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Estimate how long a video or speech script takes to deliver."
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--text", help="The script text, as a quoted string.")
    group.add_argument("--file", help="Path to a file containing the script.")
    args = parser.parse_args(argv)

    if args.file:
        try:
            with open(args.file, "r", encoding="utf-8") as handle:
                text = handle.read()
        except OSError as exc:
            parser.error(f"could not read file: {exc}")
    else:
        text = args.text

    words = len(text.split())

    lines = []
    lines.append(f"Words: {words}")
    lines.append("")
    lines.append(f"{'Rate':<8}{'Speed':<10}{'Duration'}")
    for name, wpm in RATES:
        lines.append(f"{name:<8}{str(wpm) + ' wpm':<10}{format_duration(words, wpm)}")
    lines.append("")
    lines.append("Sections:")
    for index, section in enumerate(split_sections(text), start=1):
        section_words = len(section.split())
        seconds = round(section_words / NORMAL_WPM * 60)
        lines.append(
            f"Section {index}: {section_words} words, "
            f"about {seconds} seconds at normal speed."
        )

    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    sys.exit(main())
