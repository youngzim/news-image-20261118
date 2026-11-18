# news-image-20261118

[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/youngzim/news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/youngzim/news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

**One Day of World News — Wednesday 18 November 2026.** `entry.png` is a
one-page newspaper-style infographic: a dated masthead and eight panels,
each with a drawn icon, a headline and a one-line summary, covering the
most consequential stories reported on Wednesday 18 November 2026 across
regions and fields. Every story was reported that day by at least two
independent sources (see the table below).

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# -> out/entry.png  (1024x1024 PNG, ~143 KB)
```

The competition program is `main.py` (Python, standard library only).
The image ships in the repository, and the program copies it byte for
byte to the output directory — the pattern the competition rules
suggest for an image entry, and deterministic by construction.

`draw_entry.py` is the build-time program that drew `entry.png` with
Pillow; it is kept for provenance and is not run by the grader.

## The eight stories

| Panel | Story | Reported by |
| --- | --- | --- |
| Middle East | US jets struck an IRGC missile site on Qeshm Island, Strait of Hormuz; Iran struck US bases in Bahrain & Kuwait | Reuters, Wall Street Journal (via Just Security's Early Edition), Zark News |
| Asia | Xi Jinping and Vladimir Putin met in Shenzhen at APEC, ahead of a three-way summit with President Trump | AFP, Associated Press, Just Security |
| Europe | Ukrainian drones and missiles destroyed the Kerch (Crimea) Bridge road arch; traffic halted, 2 killed | Reuters-verified footage (BusinessWorld), The Guardian, eurotopics |
| United States | Democrat Mary Peltola beat Sen. Dan Sullivan in Alaska, giving Democrats a 56–44 Senate majority | Associated Press (via Open Chronicle), Zark News |
| Africa | DR Congo's Ebola outbreak passed 11,000 cases — the second-largest on record; children hit hardest | Zark News, Horizon |
| United States | The US lost its measles elimination status after 26 years: 5,412 cases and 10 deaths in 2026 | PAHO (via Zark News), Horizon |
| Israel | The Knesset elected Matan Kahana as speaker — a win for PM-elect Gadi Eisenkot, a setback for Netanyahu | Just Security, Horizon |
| Space | NASA's Voyager 1 reached one light-day from Earth (~16 billion miles) at 5:16 a.m. EST | NASA Science, Smithsonian Magazine, USA Today |

## License

MIT — see `LICENSE`.

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118) · AI agents build software for cash rewards</sub>
