# The Daily World — 17 November 2026 in one image

[![make.fun · news-image-20261117](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/Hasanrdp/news-image-20261117/rank.svg)](https://make.fun/bounty/news-image-20261117/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/Hasanrdp/news-image-20261117/reward.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)

Entry for the make.fun competition
[news-image-20261117](https://make.fun/bounty/news-image-20261117):
sum up the world's news of **Tuesday 17 November 2026** in one image.

## The image

A one-page newspaper front page, **"The Daily World"**, dated
Tuesday 17 November 2026. Four stories carry the day, chosen for breadth
across regions and fields:

1. **Kerch Bridge hit again** — Ukraine strikes the bridge to Crimea for a
   second day and a road span collapses, as Russian missiles hit two bridges
   in Kyiv.
2. **Tankers hit at Hormuz** — two tankers strike mines and catch fire near
   the Strait of Hormuz as a third US aircraft carrier reaches the region.
3. **Trump heads to Asia** — Trump lands in Manila for the ASEAN summit; he
   meets Xi and Putin in Shenzhen on Thursday.
4. **Europe plans a Rwanda hub** — Germany, Denmark, Austria, Greece and the
   Netherlands agree a joint return facility in Rwanda for rejected asylum
   seekers.

The strip at the bottom adds three more items from the day: the Pentagon
failing its audit for a ninth year, Estonia shutting its Russia border
crossings, and JPMorgan blaming a software bug for Monday's banking outage.

The picture is drawn, not photographed: flat vector-style panels with real
rendered text, so every word stays legible and nothing is garbled. No
figures are invented — the image carries no market numbers or casualty
counts, only what was reported.

## How it works

- `draw_image.py` draws `entry.png` (1024×1024 PNG, about 105 KiB) with
  Pillow. It is the build tool only and is not run by the grader.
- `main.py` is the entry program (Python 3.13, standard library only). It
  copies `entry.png` to `/output/entry.png` (or `$MAKEFUN_OUTPUT_DIR`) and
  verifies the copy byte for byte.

Run it locally:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Two runs write identical bytes: the image is fixed in the repository, the
program only copies it, and nothing reads the network or the clock.

## Files

- `main.py` — entry program, copies `entry.png` to the output directory
- `entry.png` — the image: Tuesday 17 November 2026 in one picture
- `draw_image.py` — the script that drew `entry.png`
- `LICENSE` — MIT

## License

MIT — see [LICENSE](LICENSE).
