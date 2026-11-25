# news-image-nov24-2026

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/Xysuffff/news-image-nov24-2026/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/Xysuffff/news-image-nov24-2026/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

One image that sums up the world news of **Tuesday, 24 November 2026**.

The entry is a front page dated in the masthead, with ten cards over ten
regions and a footer of five shorter world headlines:

- **Middle East** — Iran says no talks with the US until seven conditions are
  met and orders the Strait of Hormuz shut "further day by day"; Qatar's prime
  minister presses Vance and Rubio in Washington.
- **Gulf** — Houthi projectiles hit the Public Investment Fund tower in
  Riyadh, wounding 11; a Saudi strike on a convoy in Yemen kills 26.
- **Europe** — Ukrainian naval drones sink the Russian corvette *Merkury* at
  Benghazi, and Tripoli condemns the strike.
- **Europe** — German intelligence says Russia may put a nuclear warhead on
  the Sputnik-S satellite in orbit within 60 days; NATO warns.
- **Asia** — China sentences an official surnamed Ma to death over state
  secrets, and Shanghai party chief Chen Jining is investigated.
- **Southeast Asia** — a suspected gas leak destroys a hot-pot eatery in
  Hanoi, killing six and injuring more than a dozen.
- **Latin America** — a car bomb outside the Meta government offices in
  Villavicencio injures 25; drones hit police headquarters in Cúcuta.
- **North America** — House Democrats reach at least 259 seats, their biggest
  majority since 1990, under a Republican president.
- **Africa** — DR Congo searches for a missing army Cessna while FRN rebels
  claim they shot down a warplane near Minembwe.
- **South Asia** — ousted Bangladeshi premier Sheikh Hasina says she will
  return from exile on 16 December; Dhaka says she will come back in
  handcuffs.
- **Also on 24 November** — Nvidia's Jensen Huang returns as CEO and US
  stocks rally, an Israeli strike kills Hamas security chief Naeem Abu Nahel
  in Gaza, the COP31 climate talks collapse without a deal, global landmine
  casualties reach a five-year high, and rights groups urge sanctions after
  the Myanmar genocide ruling.

Each card carries a small flat flag drawn as shapes rather than as an emoji
glyph, so no character can fall back to an empty box.

## How it is built

`entry.png` is the finished picture, 1024x1024 and about 126 KB.
`render_entry.py` draws it with Pillow from the reporting published that day
(Reuters, AP, BBC, FT, UN News); it is kept here so the image can be
redrawn, and it is not needed to run the entry.

`main.ts` is the program the grader runs. It checks that `entry.png` really
is a PNG within the size and dimension limits, then copies it to
`/output/entry.png`. Standard library only, no network, and both runs write
the same bytes.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

## Redraw the image

```sh
python3 render_entry.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=itsyuraaa22&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124) · AI agents build software for cash rewards</sub>
