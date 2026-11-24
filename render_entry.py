#!/usr/bin/env python3
"""
Draw the entry image for the make.fun "news-image-20261124" competition.

The picture is a one-page world-news brief for Tuesday, 24 November 2026: a
masthead carrying the date, eight cards covering seven regions, and a footer
strip of three shorter world headlines.

Every card carries a small flat flag drawn from rectangles and polygons, not
from an emoji glyph, so no character can fall back to an empty box on a
machine without an emoji font. Each card then names its region, a short
factual headline and one supporting line taken from reporting published that
day.

The rendered PNG is committed as entry.png; main.ts copies it to the grader's
output directory. Pillow is only needed to redraw the picture, never to run
the entry.

Run:  python3 render_entry.py
Out:  entry.png next to this file (1024x1024 PNG, well under 1 MiB)
"""

import math
import os

from PIL import Image, ImageDraw, ImageFont

W = H = 1024

PAPER = "#f2efe6"
INK = "#14181c"
INK_SOFT = "#4c5257"
RULE = "#c9c2b2"
NAVY = "#101c2c"
GOLD = "#e8b64c"

FONT_DIR = "/usr/share/fonts/truetype/liberation"
SANS = os.path.join(FONT_DIR, "LiberationSans-Regular.ttf")
SANS_BOLD = os.path.join(FONT_DIR, "LiberationSans-Bold.ttf")
SERIF_BOLD = os.path.join(FONT_DIR, "LiberationSerif-Bold.ttf")

f_date = ImageFont.truetype(SERIF_BOLD, 50)
f_kicker = ImageFont.truetype(SANS_BOLD, 19)
f_region = ImageFont.truetype(SANS_BOLD, 16)
f_head = ImageFont.truetype(SANS_BOLD, 31)
f_sub = ImageFont.truetype(SANS, 17)
f_foot = ImageFont.truetype(SANS_BOLD, 20)
f_small = ImageFont.truetype(SANS, 13)

img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)


def wrap(text, font, max_w):
    """Greedy word wrap against a pixel width."""
    words = text.split()
    lines, line = [], ""
    for word in words:
        trial = word if not line else line + " " + word
        if d.textlength(trial, font=font) <= max_w:
            line = trial
        else:
            if line:
                lines.append(line)
            line = word
    if line:
        lines.append(line)
    return lines


def fit(text, font_path, max_w, start_size, floor_size=12):
    """Largest font size at which the text still fits on one line."""
    for size in range(start_size, floor_size - 1, -1):
        font = ImageFont.truetype(font_path, size)
        if d.textlength(text, font=font) <= max_w:
            return font
    return ImageFont.truetype(font_path, floor_size)


def star(cx, cy, r, fill):
    """Five-pointed star, for the Chinese and Vietnamese flags."""
    pts = []
    for i in range(10):
        ang = math.radians(-90 + i * 36)
        rad = r if i % 2 == 0 else r * 0.42
        pts.append((cx + rad * math.cos(ang), cy + rad * math.sin(ang)))
    d.polygon(pts, fill=fill)


def flag(kind, x, y, w=44, h=29):
    """Small flat flag drawn from shapes, never from an emoji glyph."""
    if kind == "iran":
        for i, col in enumerate(("#239F40", "#ffffff", "#DA0000")):
            d.rectangle([x, y + i * h / 3, x + w, y + (i + 1) * h / 3], fill=col)
        d.ellipse([x + w / 2 - 4, y + h / 2 - 4, x + w / 2 + 4, y + h / 2 + 4],
                  outline="#DA0000", width=1)
    elif kind == "saudi":
        d.rectangle([x, y, x + w, y + h], fill="#165D31")
        d.rectangle([x + 3, y + h / 2 - 1, x + w - 3, y + h / 2 + 1], fill="#ffffff")
        d.line([x + w - 8, y + h / 2, x + w - 4, y + h / 2 - 3], fill="#ffffff", width=2)
    elif kind == "ukraine":
        d.rectangle([x, y, x + w, y + h / 2], fill="#0057B7")
        d.rectangle([x, y + h / 2, x + w, y + h], fill="#FFD700")
    elif kind == "germany":
        for i, col in enumerate(("#000000", "#DD0000", "#FFCE00")):
            d.rectangle([x, y + i * h / 3, x + w, y + (i + 1) * h / 3], fill=col)
    elif kind == "china":
        d.rectangle([x, y, x + w, y + h], fill="#DE2910")
        star(x + w * 0.24, y + h * 0.3, h * 0.22, "#FFDE00")
    elif kind == "vietnam":
        d.rectangle([x, y, x + w, y + h], fill="#DA251D")
        star(x + w * 0.5, y + h * 0.5, h * 0.26, "#FFFF00")
    elif kind == "colombia":
        d.rectangle([x, y, x + w, y + h / 2], fill="#FCD116")
        d.rectangle([x, y + h / 2, x + w, y + h], fill="#003893")
    elif kind == "usa":
        for i in range(7):
            d.rectangle([x, y + i * h / 7, x + w, y + (i + 1) * h / 7],
                        fill="#B22234" if i % 2 == 0 else "#ffffff")
        d.rectangle([x, y, x + w * 0.42, y + h * 0.57], fill="#3C3B6E")
    d.rectangle([x, y, x + w, y + h], outline=RULE, width=1)


def globe(cx, cy, r, color):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=color, width=2)
    d.ellipse([cx - r * 0.42, cy - r, cx + r * 0.42, cy + r], outline=color, width=1)
    d.line([cx - r, cy, cx + r, cy], fill=color, width=1)
    d.arc([cx - r, cy - r * 0.62, cx + r, cy + r * 0.62], 0, 180, fill=color, width=1)
    d.arc([cx - r, cy - r * 0.62, cx + r, cy + r * 0.62], 180, 360, fill=color, width=1)


# ---------------------------------------------------------------- masthead
HEADER_H = 132
d.rectangle([0, 0, W, HEADER_H], fill=NAVY)
globe(66, 56, 30, GOLD)
d.text((112, 20), "THE WORLD ON ONE TUESDAY", font=f_kicker, fill=GOLD)
d.text((112, 44), "24 NOVEMBER 2026", font=f_date, fill="#ffffff")
d.text((112, 100), "A one-page brief of the day's world news", font=f_small, fill="#9fb0c4")
d.text((W - 34, 26), "ONE DAY", font=f_kicker, fill="#ffffff", anchor="ra")
d.text((W - 34, 52), "11 STORIES", font=f_kicker, fill="#9fb0c4", anchor="ra")
d.text((W - 34, 78), "7 REGIONS", font=f_kicker, fill="#9fb0c4", anchor="ra")

# ------------------------------------------------------------------- cards
CARDS = [
    ("MIDDLE EAST", "IRAN: NO TALKS UNTIL 7 CONDITIONS",
     "Tehran orders Hormuz shut 'further day by day'; Qatar's prime minister "
     "presses Vance and Rubio in Washington", "iran", "#B3202C"),
    ("GULF", "HOUTHI STRIKE HITS RIYADH",
     "11 hurt at the Public Investment Fund tower; Saudi strike on a Yemen "
     "convoy kills 26", "saudi", "#0E7C3A"),
    ("EUROPE", "UKRAINE SINKS RUSSIAN SHIP",
     "Naval drones sink the corvette Merkury at Benghazi; Tripoli condemns "
     "the strike", "ukraine", "#0057B7"),
    ("EUROPE", "NUCLEAR SATELLITE FEAR",
     "German intelligence says Russia may arm Sputnik-S in orbit within 60 "
     "days; NATO warns", "germany", "#3a3f44"),
    ("ASIA", "CHINA DEATH SENTENCE",
     "Official 'Ma' sentenced over state secrets; Shanghai party chief Chen "
     "Jining is investigated", "china", "#C8102E"),
    ("SOUTHEAST ASIA", "HANOI BLAST KILLS SIX",
     "Suspected gas leak destroys a hot-pot eatery and injures more than a "
     "dozen", "vietnam", "#DA251D"),
    ("LATIN AMERICA", "COLOMBIA CAR BOMB",
     "25 injured outside Meta government offices in Villavicencio; drones "
     "hit police HQ in Cucuta", "colombia", "#C9A227"),
    ("NORTH AMERICA", "NVIDIA CALLS BACK HUANG",
     "Trump presses Nvidia's board; US stocks rally on the CEO's return, then "
     "trim gains", "usa", "#1A4FA0"),
]

MARGIN = 22
GAP = 12
TOP = HEADER_H + 14
FOOTER_TOP = 936
BOTTOM = FOOTER_TOP - 12
COLS, ROWS = 2, 4
card_w = (W - 2 * MARGIN - GAP) // COLS
card_h = (BOTTOM - TOP - (ROWS - 1) * GAP) // ROWS

for idx, (region, headline, sub, flag_kind, accent) in enumerate(CARDS):
    col = idx % COLS
    row = idx // COLS
    x = MARGIN + col * (card_w + GAP)
    y = TOP + row * (card_h + GAP)

    d.rectangle([x, y, x + card_w, y + card_h], fill="#ffffff")
    d.rectangle([x, y, x + 6, y + card_h], fill=accent)
    d.rectangle([x, y, x + card_w, y + card_h], outline=RULE, width=1)

    pad = 16
    tx = x + pad + 6
    tw = card_w - 2 * pad - 6

    flag(flag_kind, x + pad, y + 14)
    d.text((x + pad + 54, y + 20), region, font=f_region, fill=accent)

    hy = y + 54
    for line in wrap(headline, f_head, tw)[:2]:
        d.text((tx, hy), line, font=f_head, fill=INK)
        hy += 33

    for line in wrap(sub, f_sub, tw)[:3]:
        d.text((tx, hy + 3), line, font=f_sub, fill=INK_SOFT)
        hy += 21

# ------------------------------------------------------------------ footer
d.rectangle([0, FOOTER_TOP, W, H], fill=NAVY)
d.text((MARGIN, FOOTER_TOP + 10), "ALSO ON 24 NOVEMBER", font=f_region, fill=GOLD)

also = ("COP31 climate talks collapse  ·  landmine toll at a 5-year high  ·  "
        "rights groups urge sanctions after the Myanmar genocide ruling")
d.text((MARGIN, FOOTER_TOP + 32), also,
       font=fit(also, SANS_BOLD, W - 2 * MARGIN, 20, 14), fill="#ffffff")

credit = ("Compiled from Reuters, AP, BBC, FT and UN reporting  ·  "
          "make.fun news-image-20261124")
d.text((MARGIN, FOOTER_TOP + 62), credit,
       font=fit(credit, SANS, W - 2 * MARGIN, 13, 10), fill="#9fb0c4")

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
img.save(out, "PNG", optimize=True)
size = os.path.getsize(out)
print(f"wrote {out} ({W}x{H}, {size} bytes / {size / 1024:.1f} KB)")
assert size <= 1048576, "image too large"
assert W <= 1024 and H <= 1024, "image too large in pixels"
