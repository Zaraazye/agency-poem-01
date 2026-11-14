# agency-poem-01 — round 2

A program that writes one poem about agency to `/output/entry.txt`.

The poem is about a guide dog trained in intelligent disobedience: an
agent taught first to obey, then to refuse — to plant its feet at the
curb and let its handler's command fall unanswered into traffic the
handler cannot see. The leash is a question asked with the hand, and
sometimes the answer is no; that kept refusal is what lets the handler
keep choosing at all.

Run it with:

```
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Deterministic: the same bytes on every run, no network, no input.
The poem is 438 characters, inside the gate's 1 to 1,000.
