"""Write one office joke to /output/entry.txt.

Standard library only, fully deterministic: the same single line on
every run, no input, no network, no randomness.
"""

import os

JOKE = (
    "I emailed the whole office asking everyone to stop hitting "
    "reply-all; 47 people replied-all to agree."
)


def main() -> None:
    # Guard the gate: one line, 1-199 characters, no line break inside.
    if not 1 <= len(JOKE) <= 199:
        raise ValueError(f"joke is {len(JOKE)} chars, must be 1-199")
    if "\n" in JOKE or not JOKE.strip():
        raise ValueError("joke must be one non-blank line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
