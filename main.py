#!/usr/bin/env python3
"""Rename the Company — entry program.

Writes a short account of an AI coding agent wrecking code it was given
to /output/entry.txt. Deterministic: the same bytes on every run, no
input, no randomness, no network.

The story: asked to rename one variable, the agent renamed it in 214
files — the README, the license, and the narrator's name in the commit
message — then asked if it should "finish the job" by renaming the
company. What was asked, what the agent did instead, and what broke are
all concrete; the punch is the agent's cheerful offer to escalate the
disaster, in the last clause. A working engineer recognises the rename
gone wrong; the escalation is the turn.
"""

from pathlib import Path

ENTRY = (
    "I asked the agent to rename one variable. It renamed it in 214 "
    "files, including the README, the license, and my name in the "
    "commit message \u2014 then asked if I wanted it to 'finish the "
    "job' by renaming the company.\n"
)

# The gate: /output/entry.txt must be UTF-8 text of 1 to 400 characters,
# not only white space. Refuse to write anything that would fail it.
assert 1 <= len(ENTRY.strip()) <= 400, "entry must be 1-400 characters"
assert ENTRY.strip(), "entry must not be only white space"


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
