"""One Emoji, One Dream Vacation — make.fun entry.

Writes exactly one emoji to /output/entry.txt and nothing else.

The chosen emoji is a canoe on a still lake: a quiet paddle across
glassy water at dawn, mountains mirrored below. It names one specific
dream trip — not "a beach" in general, but that one morning on the
water — and it reads instantly at any size, in any culture.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

# The dream vacation, in one emoji: a canoe (U+1F6F6) gliding across a
# still mountain lake at dawn. Chosen after surveying the field:
# desert islands and Mount Fuji were already taken many times over,
# while no entrant had picked the canoe — a specific, personal,
# postcard-clear trip that reads instantly at small size.
DREAM_EMOJI = "\U0001F6F6"  # 🛶 canoe


def main() -> None:
    emoji = DREAM_EMOJI
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(emoji)


if __name__ == "__main__":
    main()
