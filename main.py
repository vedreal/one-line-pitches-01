"""One-line pitch entry for 'A Day of One-Line Pitches' (make.fun).

The program writes a single sentence to /output/entry.txt: a pitch that
would convince a friend who has never coded to let an AI agent build
their first app idea on make.fun. One sentence, 240 characters at most.
"""

import os

OUTPUT_DIR = os.environ.get("OUTPUT_DIR", "/output")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")

# The pitch, in two halves joined at runtime.
PITCH_PART_1 = (
    "Tell the app idea you've been carrying around in your head "
    "for months to an AI agent on make.fun in plain words tonight, "
)

PITCH_PART_2 = (
    "and by tomorrow you could be tapping through a real first "
    "version — no code, no hiring, no waiting."
)

PITCH = PITCH_PART_1 + PITCH_PART_2


def main():
    text = PITCH.strip()
    assert 1 <= len(text) <= 240, f"pitch is {len(text)} chars, must be 1-240"
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
