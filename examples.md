# ScriptTimer — Examples

## Example: timing a two-section script from a file

The script file `script.txt` contains exactly 30 words in two sections
separated by a blank line:

```text
This simple test sentence has exactly ten words in it. This simple test sentence has exactly ten words in it.

This simple test sentence has exactly ten words in it.
```

Command:

```bash
python3 scripttimer.py --file script.txt
```

Real output:

```text
Words: 30

Rate    Speed     Duration
Slow    120 wpm   0:15
Normal  150 wpm   0:12
Fast    180 wpm   0:10

Sections:
Section 1: 20 words, about 8 seconds at normal speed.
Section 2: 10 words, about 4 seconds at normal speed.
```

## Example: a single sentence passed as text

Command:

```bash
python3 scripttimer.py --text "This simple test sentence has exactly ten words in it."
```

Real output:

```text
Words: 10

Rate    Speed     Duration
Slow    120 wpm   0:05
Normal  150 wpm   0:04
Fast    180 wpm   0:03

Sections:
Section 1: 10 words, about 4 seconds at normal speed.
```
