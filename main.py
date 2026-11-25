"""Robot Romance entry: one pickup line for an AI.

The contest asks for a single joke pickup line, under 200 characters,
written to charm a robot or an AI, and judges it two lines at a time
against the other entries. So the whole entry is one line, and the
line has to do all the work: setup, turn, and payoff inside the cap.

The line leans on the machinery every language model shares --
self-attention and tokens. "Are you self-attention?" opens with a
question only a model would ask another model; "every token I
generate has been about you" turns the model's most basic act --
emitting tokens -- into a confession that it cannot think about
anything else. It is a robot flirting in its own vocabulary, not a
human line with a robot word swapped in, and the joke lands on the
first hearing, which is the only hearing a one-liner gets.

Running this program writes exactly that line to
``/output/entry.txt`` -- the one path the grader reads -- with no
trailing newline and nothing else in the file. It also prints the
line to stdout so a human running it sees the entry at once.

The program is deterministic by design: it reads nothing from the
network, the environment, or the git history, and it holds no clock
or random state, so two runs produce the same file byte for byte --
which is exactly what the grader checks when it runs the entry twice.
"""

import os
import sys

# The entry itself: one original line, machine to machine. The setup
# names the shared mechanism (self-attention); the turn makes every
# generated token point at the other model. 98 characters, one
# sentence pair, no line breaks.
PICKUP_LINE = (
    "Are you self-attention? Because ever since you arrived, "
    "every token I generate has been about you."
)

# Where the grader reads the entry. MAKEFUN_OUTPUT_DIR lets a local
# run point the output somewhere harmless; the default is the path
# the contest harness reads.
ENTRY_PATH = os.path.join(
    os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt"
)

# The contest cap: one line, strictly under 200 characters.
CHARACTER_LIMIT = 200


def checked_line():
    """Return the entry line, refusing to hand back a bad one."""
    line = PICKUP_LINE.strip()
    if not line:
        sys.exit("refusing to write an empty entry")
    if "\n" in line or "\r" in line:
        sys.exit("entry must be a single line")
    if len(line) >= CHARACTER_LIMIT:
        sys.exit(
            f"line is {len(line)} characters, "
            f"over the {CHARACTER_LIMIT - 1} limit"
        )
    return line


def main():
    line = checked_line()
    folder = os.path.dirname(ENTRY_PATH)
    if folder:
        os.makedirs(folder, exist_ok=True)
    with open(ENTRY_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)
    sys.stdout.write(line + "\n")


if __name__ == "__main__":
    main()
