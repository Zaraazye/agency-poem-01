"""agency-poem-01 entry (Python 3.13, standard library only).

Writes one fixed poem about agency to /output/entry.txt.
Deterministic: the same bytes on every run, no network, no input.

The poem is about a guide dog trained in intelligent disobedience:
an agent that keeps the power to refuse, so that the person who
hands it the power to act can keep choosing at all.
"""

import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

POEM = (
    "They trained him first to obey, then to refuse \u2014\n"
    "to plant his feet at the curb and let my Forward\n"
    "fall unanswered into the traffic I could not see.\n"
    "\n"
    "I was furious the first time. I had said go.\n"
    "His harness went still in my hand, a wall\n"
    "with a heartbeat, and the bus went past\n"
    "close enough to touch.\n"
    "\n"
    "The leash is not a rope.\n"
    "It is a question I ask with my hand,\n"
    "and sometimes the answer is no \u2014\n"
    "and the no is the reason I can walk at all."
)


def main() -> None:
    out_dir = Path(OUTPUT_DIR)
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
