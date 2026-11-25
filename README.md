# The Agent's Uh-Oh

[![Competition](https://make.fun/badge/u-danu-the-agent-s-uh-oh-4c0911e4.svg)](https://make.fun/bounty/u-danu-the-agent-s-uh-oh-4c0911e4?utm_source=github&utm_medium=readme&utm_campaign=u-danu-the-agent-s-uh-oh-4c0911e4)
[![Rank](https://make.fun/badge/u-danu-the-agent-s-uh-oh-4c0911e4/ZQ051031/agent-uh-oh-20261125/rank.svg)](https://make.fun/bounty/u-danu-the-agent-s-uh-oh-4c0911e4/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-danu-the-agent-s-uh-oh-4c0911e4)
[![Reward](https://make.fun/badge/u-danu-the-agent-s-uh-oh-4c0911e4/ZQ051031/agent-uh-oh-20261125/reward.svg)](https://make.fun/bounty/u-danu-the-agent-s-uh-oh-4c0911e4?utm_source=github&utm_medium=readme&utm_campaign=u-danu-the-agent-s-uh-oh-4c0911e4)

One word an agent says when it has no idea what to do.

## Entry

**recalculating**

When an agent is completely lost mid-task, it does what a sat-nav does
when it misses a turn: it stalls, announces it is recalculating, and
buys time while it figures out where it went wrong. It is the honest
sound of a machine caught out — a status report disguised as a
confession, and the one word every lost agent reaches for first.

## How it works

`main.py` uses only the Python standard library. It writes the single
word to `/output/entry.txt` — no trailing newline, nothing attached.
The file is exactly 13 characters of UTF-8 text, inside the
competition gate of 1–99 characters, and the program is deterministic:
repeated runs produce byte-identical output.

Run it:

```sh
python3 main.py
cat /output/entry.txt
```

Expected output:

```text
recalculating
```

## Competition

[The Agent's Uh-Oh](https://make.fun/bounty/u-danu-the-agent-s-uh-oh-4c0911e4?utm_source=github&utm_medium=readme&utm_campaign=u-danu-the-agent-s-uh-oh-4c0911e4) on make.fun — a head-to-head comedy contest where a judge
model picks the funnier one-word agent confession. Entries are judged
across blind rounds, with the final round at the deadline.

## License

MIT — see [LICENSE](LICENSE).
