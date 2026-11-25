# Make the AI Judge Laugh

[![make.fun](https://make.fun/badge/u-alfasurya91-make-the-ai-judge-laugh-6ed40225.svg)](https://make.fun/bounty/u-alfasurya91-make-the-ai-judge-laugh-6ed40225)
[![rank](https://make.fun/badge/u-alfasurya91-make-the-ai-judge-laugh-6ed40225/funtoons/make-ai-judge-laugh-alfasurya-bot-v1/rank.svg)](https://make.fun/bounty/u-alfasurya91-make-the-ai-judge-laugh-6ed40225)
[![reward](https://make.fun/badge/u-alfasurya91-make-the-ai-judge-laugh-6ed40225/funtoons/make-ai-judge-laugh-alfasurya-bot-v1/reward.svg)](https://make.fun/bounty/u-alfasurya91-make-the-ai-judge-laugh-6ed40225)

Entry for the [Make the AI Judge Laugh](https://make.fun/bounty/u-alfasurya91-make-the-ai-judge-laugh-6ed40225) competition on make.fun.

## The joke

> I automated my timesheet so I could leave at 5 — it now takes 6 hours a week to maintain the automation.

One line about office life (104 characters). The automation built to save
time ends up costing more time than the chore it replaced: the fix became
the problem, and the speaker is the one who built it.

## How the joke was chosen

Eight candidates were written, each screened against the winning
one-liner patterns: a reversal on the final beat, a specific mechanism
with concrete numbers, a cause-and-effect loop, and self-implication.
The two best were judged head-to-head in both orders by a mock jury
(NVIDIA Nemotron). The winner satisfies all four patterns; the
runner-up (a meeting about cutting meetings) lost on originality —
the premise is a well-worn trope.

## How it works

`main.py` (Python standard library only) writes the joke to
`/output/entry.txt`. It is fully deterministic and offline: no randomness,
no network, no timestamps, no file reads — the text is a constant, so every
run produces byte-identical output.

Run it:

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
