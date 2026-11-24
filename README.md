# Worst AI Advice

[![make.fun · u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580](https://make.fun/badge/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580)
[![make.fun · u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580](https://make.fun/badge/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580/bayusantosz3995/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580-sparta-r2/rank.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580)
[![make.fun · u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580](https://make.fun/badge/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580/bayusantosz3995/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580-sparta-r2/reward.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580)

One line of the worst AI advice imaginable: hand hospital triage to a
famous AI assistant and watch a measurable disaster unfold — patients
sent home, millions paid out, and a license lost.

`main.py` holds the entry line in `TEXT`, gates it (non-empty, at most
200 characters), writes it to `entry.txt` in `MAKEFUN_OUTPUT_DIR`
(or `/output` when unset), then reads it back and verifies it
byte-for-byte.

## Run

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```
