# ScriptTimer

Estimate how long a video or speech script takes to deliver, at slow, normal and fast speaking rates.

## Who it helps

- **Creators timing reels and Shorts** — check whether a script fits a 30, 60 or 90 second slot before you record.
- **Speakers and presenters** — pace a talk, sermon, lesson or voiceover and see which parts run long.
- Anyone who writes words that will be spoken out loud and needs a quick timing check.

## Requirements

- Python 3
- Standard library only — nothing to install.

## Usage

Time a script passed directly on the command line:

```bash
python3 scripttimer.py --text "This simple test sentence has exactly ten words in it."
```

Time a script saved in a file:

```bash
python3 scripttimer.py --file script.txt
```

Exactly one of `--text` or `--file` is required. The tool prints the total
word count, the duration at three speaking rates (Slow 120 wpm, Normal
150 wpm, Fast 180 wpm), and a per-section breakdown. Sections are split on
blank lines, so you can time each part of a script separately.

See [examples.md](examples.md) for a full worked example with real output.

## License

MIT — see [LICENSE](LICENSE). Copyright (c) 2026 Muhammad Ahsan Anwar.
