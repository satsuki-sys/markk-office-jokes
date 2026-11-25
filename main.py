#!/usr/bin/env python3
"""One-Line Office Jokes entry for make.fun.

Writes a single one-line joke about office life to /output/entry.txt
(or ./output/entry.txt when /output is not writable).
"""
import os

JOKE = "The office printer only jams on documents marked urgent, which is how I know it can read."

def main():
    out_dir = "/output" if os.access("/output", os.W_OK) else os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)
    print(f"Wrote {len(JOKE)} chars to {path}")

if __name__ == "__main__":
    main()
