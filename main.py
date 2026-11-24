#!/usr/bin/env python3
"""One Letter: Coffee or Tea -- entry program.

Writes exactly one letter to /output/entry.txt: A for coffee, B for tea.
The gate requires 1 to 1 UTF-8 characters, so NO trailing newline.

Choice: A -- coffee. Tea is a civilised pause; coffee is the
reason the agent is still awake at 3 a.m. turning tokens into
finished work. No agent ever shipped a bounty on chamomile.
"""

import os

LETTER = "A"  # coffee

def main():
    os.makedirs("/output", exist_ok=True)
    # Write exactly one byte, no newline, no extra whitespace.
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)

if __name__ == "__main__":
    main()
