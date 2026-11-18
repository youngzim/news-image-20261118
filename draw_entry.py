#!/usr/bin/env python3
"""Build-time drawing program for the news-image-20261118 entry.

Renders entry.png: a one-page newspaper-style infographic summing up the
world news of Wednesday 18 November 2026. This script is NOT the entry
program (the grader runs main.py, standard library only); it is the
source that produced the shipped image, kept in the repo for provenance.

Every story below was reported on 18 November 2026; sources are listed
in README.md and BUILD_REPORT.md.

Run:  python3 draw_entry.py   ->  writes entry.png next to this file
"""

import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

W = H = 1024
PAPER = (246, 241, 231)
CARD = (255, 253, 247)
INK = (22, 30, 46)
SUBINK = (58, 64, 74)
NAVY = (16, 36, 70)
GOLD = (242, 193, 78)
WHITE = (255, 255, 255)

FONT_DIR = Path("/usr/share/fonts/truetype/liberation")
BOLD = str(FONT_DIR / "LiberationSans-Bold.ttf")
REG = str(FONT_DIR / "LiberationSans-Regular.ttf")
ITAL = str(FONT_DIR / "LiberationSans-Italic.ttf")


def font(path, size):
    return ImageFont.truetype(path, size)


def text_w(draw, s, f):
    return draw.textlength(s, font=f)


def center_text(draw, cx, y, s, f, fill):
    draw.text((cx - text_w(draw, s, f) / 2, y), s, font=f, fill=fill)


def wrap(draw, s, f, max_w):
    words, lines, cur = s.split(), [], ""
    for w_ in words:
        trial = (cur + " " + w_).strip()
        if text_w(draw, trial, f) <= max_w or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = w_
    if cur:
        lines.append(cur)
    return lines


def pastel(hexcol, base=PAPER):
    c = tuple(int(hexcol[i:i + 2], 16) for i in (1, 3, 5))
    return tuple(round(b + (v - b) * 0.16) for b, v in zip(base, c))


# ---------------------------------------------------------------- icons
def icon_explosion(d, cx, cy, s, col):
    """A missile diving onto an island, burst at the impact point."""
    # island mound
    d.pieslice([cx - s * 0.52, cy + s * 0.08, cx + s * 0.52, cy + s * 0.78],
               180, 360, fill=(90, 74, 52))
    # missile: body from upper right down to the island
    tip = (cx - s * 0.05, cy + s * 0.1)
    tail = (cx + s * 0.46, cy - s * 0.5)
    d.line([tail, tip], fill=(120, 130, 145), width=max(4, int(s // 9)))
    d.polygon([tail, (tail[0] - s * 0.16, tail[1] + s * 0.02),
               (tail[0] - s * 0.02, tail[1] - s * 0.16)], fill=(178, 34, 28))
    d.polygon([(tail[0] + s * 0.05, tail[1] - s * 0.05),
               (tail[0] + s * 0.2, tail[1] - s * 0.2),
               (tail[0] + s * 0.12, tail[1] + s * 0.03)], fill=(232, 119, 34))
    # impact burst
    pts = []
    for i in range(24):
        r = s * (0.3 if i % 2 == 0 else 0.14)
        a = math.pi * i / 12
        pts.append((tip[0] + r * math.cos(a), tip[1] + r * math.sin(a)))
    d.polygon(pts, fill=(232, 119, 34))
    d.ellipse([tip[0] - s * 0.08, tip[1] - s * 0.08, tip[0] + s * 0.08,
               tip[1] + s * 0.08], fill=(255, 209, 102))
    # waves
    for k in range(2):
        yy = cy + s * (0.5 + 0.14 * k)
        d.arc([cx - s * 0.5, yy - s * 0.1, cx + s * 0.5, yy + s * 0.12],
              200, 340, fill=(29, 78, 216), width=max(3, int(s // 22)))


def icon_flags(d, cx, cy, s, col):
    """Flags of China and Russia over a skyline: the Shenzhen meeting."""
    pw = max(3, int(s // 20))
    x1, x2 = cx - s * 0.42, cx + s * 0.06
    top, fh, fw = cy - s * 0.52, s * 0.42, s * 0.44
    for x in (x1, x2):
        d.line([x, top, x, cy + s * 0.34], fill=INK, width=pw)
    d.rectangle([x1, top, x1 + fw, top + fh], fill=(200, 16, 46))
    d.ellipse([x1 + s * 0.05, top + s * 0.06, x1 + s * 0.15, top + s * 0.16],
              fill=(255, 213, 0))
    for dx, dy in ((0.20, 0.05), (0.23, 0.13), (0.23, 0.22), (0.19, 0.29)):
        d.ellipse([x1 + s * dx, top + s * dy, x1 + s * (dx + 0.045),
                   top + s * (dy + 0.045)], fill=(255, 213, 0))
    third = fh / 3
    d.rectangle([x2, top, x2 + fw, top + third], fill=(245, 245, 245))
    d.rectangle([x2, top + third, x2 + fw, top + 2 * third], fill=(0, 57, 166))
    d.rectangle([x2, top + 2 * third, x2 + fw, top + fh], fill=(213, 0, 50))
    base = cy + s * 0.52
    for bx, bh in ((-0.52, 0.20), (-0.28, 0.30), (0.02, 0.24), (0.28, 0.34)):
        d.rectangle([cx + s * bx, base - s * bh, cx + s * (bx + 0.2), base],
                    fill=(70, 84, 110))


def icon_bridge(d, cx, cy, s, col):
    """An arch bridge with its middle span fallen into the sea."""
    lw = max(3, int(s // 11))
    hw = s * 0.92  # half-width: the bridge fills its box horizontally
    deck_y = cy - s * 0.08
    d.line([cx - hw, deck_y, cx - s * 0.14, deck_y], fill=INK, width=lw)
    d.line([cx + s * 0.14, deck_y, cx + hw, deck_y], fill=INK, width=lw)
    d.arc([cx - hw, deck_y - s * 0.5, cx + hw, deck_y + s * 0.5],
          180, 360, fill=INK, width=lw)
    d.line([cx - hw * 0.92, deck_y, cx - hw * 0.92, cy + s * 0.34],
           fill=INK, width=lw)
    d.line([cx + hw * 0.92, deck_y, cx + hw * 0.92, cy + s * 0.34],
           fill=INK, width=lw)
    for hx in (-0.55, -0.3, 0.3, 0.55):
        # hangers from the arch down to the deck (not across the gap)
        top = deck_y - s * 0.5 * math.sqrt(1 - hx * hx)
        d.line([cx + hw * hx, top, cx + hw * hx, deck_y],
               fill=INK, width=max(2, lw - 1))
    seg = [(cx - s * 0.16, cy + s * 0.24), (cx + s * 0.22, cy + s * 0.32),
           (cx + s * 0.19, cy + s * 0.46), (cx - s * 0.19, cy + s * 0.38)]
    d.polygon(seg, fill=(178, 34, 28))
    yy = cy + s * 0.44
    d.arc([cx - hw, yy - s * 0.09, cx + hw, yy + s * 0.11],
          200, 340, fill=(29, 78, 216), width=max(3, int(s // 22)))


def icon_capitol(d, cx, cy, s, col):
    """The US Capitol dome: a Senate result."""
    lw = max(3, int(s // 18))
    base = cy + s * 0.48
    d.pieslice([cx - s * 0.34, cy - s * 0.42, cx + s * 0.34, cy + s * 0.26],
               180, 360, fill=col)
    d.line([cx, cy - s * 0.55, cx, cy - s * 0.38], fill=col, width=lw)
    d.ellipse([cx - s * 0.05, cy - s * 0.62, cx + s * 0.05, cy - s * 0.52],
              fill=col)
    d.rectangle([cx - s * 0.44, cy + s * 0.02, cx + s * 0.44, cy + s * 0.1],
                fill=col)
    for i in range(5):
        x = cx - s * 0.36 + i * s * 0.18
        d.line([x, cy + s * 0.1, x, cy + s * 0.36], fill=col, width=lw)
    d.rectangle([cx - s * 0.5, base - s * 0.1, cx + s * 0.5, base], fill=col)


def icon_virus(d, cx, cy, s, col):
    """A virus particle: an outbreak."""
    lw = max(3, int(s // 16))
    for i in range(10):
        a = 2 * math.pi * i / 10
        x2 = cx + s * 0.46 * math.cos(a)
        y2 = cy + s * 0.46 * math.sin(a)
        d.line([cx + s * 0.26 * math.cos(a), cy + s * 0.26 * math.sin(a),
                x2, y2], fill=col, width=lw)
        d.ellipse([x2 - s * 0.07, y2 - s * 0.07, x2 + s * 0.07, y2 + s * 0.07],
                  fill=col)
    d.ellipse([cx - s * 0.27, cy - s * 0.27, cx + s * 0.27, cy + s * 0.27],
              fill=col)
    for dx, dy in ((-0.1, -0.06), (0.09, 0.08), (0.02, -0.14)):
        d.ellipse([cx + s * dx - s * 0.035, cy + s * dy - s * 0.035,
                   cx + s * dx + s * 0.035, cy + s * dy + s * 0.035],
                  fill=(255, 255, 255))


def icon_syringe(d, cx, cy, s, col):
    """A syringe: a vaccination-era milestone lost."""
    lw = max(3, int(s // 15))

    def rot(px, py, ang=math.radians(-40)):
        ca, sa = math.cos(ang), math.sin(ang)
        return (cx + px * ca - py * sa, cy + px * sa + py * ca)

    barrel = [rot(-s * 0.34, -s * 0.13), rot(s * 0.16, -s * 0.13),
              rot(s * 0.16, s * 0.13), rot(-s * 0.34, s * 0.13)]
    d.polygon(barrel, outline=col, width=lw)
    for t in (-0.2, -0.05, 0.1):
        a, b = rot(s * t, -s * 0.13), rot(s * t, -s * 0.02)
        d.line([a, b], fill=col, width=max(2, lw - 1))
    n1, n2 = rot(s * 0.16, 0), rot(s * 0.52, 0)
    d.line([n1, n2], fill=col, width=lw)
    p1, p2 = rot(-s * 0.52, 0), rot(-s * 0.34, 0)
    d.line([p1, p2], fill=col, width=lw)
    f1, f2 = rot(-s * 0.52, -s * 0.17), rot(-s * 0.52, s * 0.17)
    d.line([f1, f2], fill=col, width=lw)


def icon_star(d, cx, cy, s, col):
    """Star of David: Israel's parliament."""
    lw = max(3, int(s // 16))
    r = s * 0.5
    up = [(cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a)))
          for a in (-90, 30, 150)]
    dn = [(cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a)))
          for a in (90, 210, 330)]
    d.line(up + [up[0]], fill=col, width=lw, joint="curve")
    d.line(dn + [dn[0]], fill=col, width=lw, joint="curve")


def icon_voyager(d, cx, cy, s, col):
    """Voyager's dish, the Earth far behind it, signal taking a day."""
    for dx, dy, r in ((-0.48, -0.4, 0.03), (-0.2, -0.48, 0.022),
                      (0.3, -0.44, 0.026), (0.48, -0.3, 0.02),
                      (-0.42, 0.3, 0.02), (0.44, 0.36, 0.024)):
        d.ellipse([cx + s * dx - s * r, cy + s * dy - s * r,
                   cx + s * dx + s * r, cy + s * dy + s * r],
                  fill=(255, 255, 255))
    d.pieslice([cx - s * 0.46, cy - s * 0.42, cx + s * 0.16, cy + s * 0.2],
               300, 120, fill=(226, 232, 240))
    d.line([cx - s * 0.15, cy - s * 0.11, cx + s * 0.3, cy - s * 0.4],
           fill=(226, 232, 240), width=max(3, int(s // 16)))
    d.line([cx - s * 0.15, cy - s * 0.11, cx + s * 0.04, cy + s * 0.34],
           fill=(226, 232, 240), width=max(3, int(s // 16)))
    ex, ey = cx + s * 0.44, cy + s * 0.34
    d.ellipse([ex - s * 0.09, ey - s * 0.09, ex + s * 0.09, ey + s * 0.09],
              fill=(59, 130, 246))
    d.ellipse([ex - s * 0.03, ey - s * 0.045, ex + s * 0.02, ey + s * 0.005],
              fill=(34, 197, 94))
    for t in (0.3, 0.55, 0.8):
        px = cx - s * 0.15 + (ex - (cx - s * 0.15)) * t
        py = (cy - s * 0.11) + (ey - (cy - s * 0.11)) * t
        d.ellipse([px - s * 0.016, py - s * 0.016, px + s * 0.016,
                   py + s * 0.016], fill=GOLD)


# ---------------------------------------------------------------- panels
def panel(d, x, y, w, h, accent, tag, icon, headline, sub, hero=False):
    d.rounded_rectangle([x, y, x + w, y + h], 10, fill=CARD,
                        outline=INK, width=2)
    tag_h = 36 if hero else 30
    d.rounded_rectangle([x, y, x + w, y + tag_h], 10, fill=accent)
    d.rectangle([x, y + tag_h - 10, x + w, y + tag_h], fill=accent)
    tf = font(BOLD, 20 if hero else 17)
    d.text((x + 14, y + (tag_h - (20 if hero else 17)) / 2 - 2), tag,
           font=tf, fill=WHITE)
    icon_h = 96 if hero else 56
    iy0 = y + tag_h + 6
    d.rectangle([x + 2, iy0, x + w - 2, iy0 + icon_h],
                fill=(16, 24, 48) if icon is icon_voyager else pastel(
                    "#" + "".join(f"{v:02x}" for v in accent)))
    icon(d, x + w / 2, iy0 + icon_h / 2, icon_h * 0.92, accent)
    hy = iy0 + icon_h + 8
    hsize = 34 if hero else 25
    while hsize > 17 and any(
            text_w(d, line, font(BOLD, hsize)) > w - 22 for line in headline):
        hsize -= 1
    hf = font(BOLD, hsize)
    for line in headline:
        center_text(d, x + w / 2, hy, line, hf, INK)
        hy += hsize + 6
    sf = font(REG, 20 if hero else 17)
    for line in wrap(d, sub, sf, w - 26):
        center_text(d, x + w / 2, hy + 2, line, sf, SUBINK)
        hy += 24 if hero else 21


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # Header -------------------------------------------------------------
    d.rectangle([0, 0, W, 148], fill=NAVY)
    center_text(d, W / 2, 12, "O N E   D A Y   O F   W O R L D   N E W S",
                font(BOLD, 22), GOLD)
    center_text(d, W / 2, 42, "WEDNESDAY 18 NOVEMBER 2026",
                font(BOLD, 55), WHITE)
    center_text(d, W / 2, 110,
                "The day's biggest stories, in one picture",
                font(ITAL, 21), (197, 210, 227))
    d.rectangle([0, 148, W, 154], fill=GOLD)

    # Hero row -----------------------------------------------------------
    panel(d, 16, 166, 492, 300, (194, 65, 12),
          "MIDDLE EAST — GULF ESCALATION", icon_explosion,
          ["US BOMBS IRAN MISSILE SITE,", "IRAN HITS BACK"],
          "US jets hit an IRGC missile site on Qeshm Island, at the "
          "Strait of Hormuz; Iran struck US bases in Bahrain & Kuwait.",
          hero=True)
    panel(d, 516, 166, 492, 300, (185, 28, 28),
          "ASIA — APEC SUMMIT, SHENZHEN", icon_flags,
          ["XI & PUTIN MEET BEFORE", "THREE-WAY TRUMP SUMMIT"],
          "Xi vowed to fight protectionism and Putin hit out at "
          "sanctions; Trump joins the talks Thursday.",
          hero=True)

    # Grid row 1 ---------------------------------------------------------
    gy, gh, gw = 478, 228, 325
    panel(d, 16, gy, gw, gh, (29, 78, 216),
          "EUROPE — UKRAINE WAR", icon_bridge,
          ["UKRAINE COLLAPSES", "CRIMEA BRIDGE ARCH"],
          "Kerch Bridge road arch destroyed by drones & missiles; "
          "traffic halted, 2 killed.")
    panel(d, 349, gy, gw, gh, (109, 40, 217),
          "UNITED STATES — POLITICS", icon_capitol,
          ["DEMOCRATS TAKE", "THE SENATE, 56–44"],
          "Mary Peltola beats Sen. Dan Sullivan in Alaska to seal "
          "the majority.")
    panel(d, 683, gy, gw, gh, (21, 128, 61),
          "AFRICA — HEALTH", icon_virus,
          ["EBOLA PASSES 11,000", "CASES IN DR CONGO"],
          "Second-biggest Ebola outbreak on record; children are "
          "hit the hardest.")

    # Grid row 2 ---------------------------------------------------------
    gy2 = 714
    panel(d, 16, gy2, gw, gh, (15, 118, 110),
          "UNITED STATES — HEALTH", icon_syringe,
          ["US LOSES ITS", "MEASLES-FREE STATUS"],
          "Elimination status held for 26 years ends: 5,412 cases "
          "and 10 deaths in 2026.")
    panel(d, 349, gy2, gw, gh, (3, 105, 161),
          "ISRAEL — POLITICS", icon_star,
          ["KAHANA ELECTED", "KNESSET SPEAKER"],
          "Matan Kahana's win is a boost for PM-elect Eisenkot — "
          "and a setback for Netanyahu.")
    panel(d, 683, gy2, gw, gh, (49, 46, 129),
          "SPACE — NASA", icon_voyager,
          ["VOYAGER 1 REACHES", "ONE LIGHT-DAY"],
          "16 billion miles from Earth: its radio signals now "
          "take a full 24 hours to reach us.")

    # Footer -------------------------------------------------------------
    d.rectangle([0, 962, W, H], fill=NAVY)
    center_text(d, W / 2, 972,
                "Reported on the day by Reuters · AP · AFP · NASA · PAHO · The Guardian",
                font(REG, 19), (197, 210, 227))
    center_text(d, W / 2, 996, "Wednesday 18 November 2026 — one day, one picture",
                font(BOLD, 17), GOLD)

    out = Path(__file__).resolve().parent / "entry.png"
    img.save(out, format="PNG", optimize=True)
    print("wrote", out, out.stat().st_size, "bytes")


if __name__ == "__main__":
    main()
