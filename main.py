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
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
