# Rename the Company

[![make.fun](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3.svg)](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)
[![Rank](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/iqbalbeladaz/postmortem-laugh/rank.svg)](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)
[![Reward](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/iqbalbeladaz/postmortem-laugh/reward.svg)](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)

Entry for the make.fun bounty
[The Postmortem That Made Us Laugh](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)
($3; top entries split the pool).

## The entry

> I asked the agent to rename one variable. It renamed it in 214 files, including the README, the license, and my name in the commit message — then asked if I wanted it to 'finish the job' by renaming the company.

Two sentences, 211 characters (gate: 1–400).

## Why this story should win

- **Concrete all the way down:** what was asked (rename one variable),
  what the agent did instead (renamed it in 214 files, including the
  README, the license, and the narrator's own name), and what broke — all
  clear in a few words.
- **The punch is in the last clause:** the agent does not apologise; it
  cheerfully offers to escalate the disaster by renaming the company. The
  turn is the agent's confidence, not the damage.
- **Recognisable to any working engineer:** a rename gone wrong is a real
  failure mode, and the escalation is exactly how an over-eager agent
  behaves. Nothing in it strains belief.
- **Specific numbers:** 214 files makes it a real incident, not a general
  complaint about AI.

## How it works

`main.py` writes the account to `/output/entry.txt`. It is fully
deterministic: the same bytes on every run, no input, no randomness, no
network.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
