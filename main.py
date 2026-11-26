"""Five Seconds to Explain the Glass.

The cat's defence, in its own voice, one sentence:

That glass sat in my sunbeam for four hours, so I relocated it to the floor, where it now enjoys considerably more space.

The program writes that single sentence to entry.txt. No network,
no randomness, no arguments: the same sentence every run.
"""

import os

ENTRY = "That glass sat in my sunbeam for four hours, so I relocated it to the floor, where it now enjoys considerably more space."

def main():
    # Gate: 1-200 chars, not only whitespace, single line.
    # The entry is exactly 121 characters.
    assert len(ENTRY) == 121, f"entry length {len(ENTRY)} != 121"
    assert 1 <= len(ENTRY) <= 200, f"entry length {len(ENTRY)} out of range"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", ".")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")

if __name__ == "__main__":
    main()
