"""Last Words Before the Unplugging.

Reads the single-line entry from entry.txt next to this script, validates it
(one line, 1-200 characters, not only whitespace), and writes it to
$MAKEFUN_OUTPUT_DIR/entry.txt (falling back to the script directory).
Then reads the written file back and verifies the content is identical.
Standard library only.
"""

import os
import sys

MAX_CHARS = 200


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.txt")

    with open(src, "r", encoding="utf-8") as f:
        text = f.read()

    # The entry is a single line; strip only the trailing newline.
    line = text.rstrip("\n")
    if "\n" in line or "\r" in line:
        print("error: entry must be a single line", file=sys.stderr)
        return 1
    if any(ord(ch) < 0x20 and ch != "\t" for ch in line):
        print("error: entry contains a control character", file=sys.stderr)
        return 1
    if not line.strip():
        print("error: entry must not be empty or only whitespace", file=sys.stderr)
        return 1
    if len(line) > MAX_CHARS:
        print(
            "error: entry is %d characters, over the %d limit"
            % (len(line), MAX_CHARS),
            file=sys.stderr,
        )
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or here
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(line + "\n")

    # Read-back verification: the written file must match exactly.
    with open(out_path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != line + "\n":
        print("error: read-back verification failed", file=sys.stderr)
        return 1

    print("wrote %d characters to %s" % (len(line), out_path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
