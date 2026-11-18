#!/usr/bin/env python3
"""Draw the news-image-20261117 entry: a one-page newspaper front page
summing up the world's news of Tuesday 17 November 2026.

Flat vector-style illustration drawn with Pillow primitives, real rendered
text throughout (no AI-generated text, so nothing is garbled). Run it to
produce entry.png next to this file; the entry program (main.py) then only
copies that image. Deterministic: no randomness, no clock, no network.
"""
import math
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 242, 232)
INK = (22, 22, 22)
NAVY = (20, 33, 61)
NAVY_LIGHT = (38, 58, 96)
GOLD = (201, 162, 39)
RED = (176, 46, 46)
TEAL = (31, 111, 107)
CREAM = (247, 242, 232)
WHITE = (255, 253, 246)
GREY = (90, 88, 80)
SKY = (174, 205, 225)
SEA = (46, 98, 140)

FD = "/usr/share/fonts/truetype/dejavu"


def font(path, size):
    return ImageFont.truetype(path, size)


SERIF_B = font(f"{FD}/DejaVuSerif-Bold.ttf", 62)
SERIF_H = font(f"{FD}/DejaVuSerif-Bold.ttf", 44)
SERIF_P = font(f"{FD}/DejaVuSerif-Bold.ttf", 28)
SERIF_S = font(f"{FD}/DejaVuSerif.ttf", 23)
SANS_B = font(f"{FD}/DejaVuSans-Bold.ttf", 20)
SANS_K = font(f"{FD}/DejaVuSans-Bold.ttf", 17)
SANS = font(f"{FD}/DejaVuSans.ttf", 20)
SANS_SM = font(f"{FD}/DejaVuSans.ttf", 17)
SANS_XS = font(f"{FD}/DejaVuSans-Bold.ttf", 15)


def wrap(draw, text, fnt, width):
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = f"{cur} {w}".strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def starburst(draw, cx, cy, r_out, r_in, fill, outline):
    pts = []
    for i in range(16):
        ang = i * math.pi / 8
        r = r_out if i % 2 == 0 else r_in
        pts.append((cx + r * math.cos(ang), cy + r * math.sin(ang)))
    draw.polygon(pts, fill=fill, outline=outline)


def plane(draw, px, py, scale, color):
    draw.polygon([(px, py), (px + 46 * scale, py + 10 * scale),
                  (px, py + 12 * scale), (px + 8 * scale, py + 26 * scale),
                  (px + 2 * scale, py + 30 * scale),
                  (px - 8 * scale, py + 12 * scale)], fill=color)


def draw_bridge(draw, x, y, w, h):
    """A suspension bridge with a broken deck and a blast above the gap."""
    draw.rectangle([x, y, x + w, y + h], fill=SKY)
    draw.ellipse([x + w - 48, y + 8, x + w - 14, y + 42], fill=(250, 205, 90))
    deck_y = y + int(h * 0.48)
    tower_x0, tower_x1 = x + int(w * 0.22), x + int(w * 0.74)
    for tx in (tower_x0, tower_x1):
        draw.rectangle([tx - 5, y + 12, tx + 5, deck_y], fill=NAVY)
    for i in range(9):
        t = i / 8
        cx = tower_x0 + (tower_x1 - tower_x0) * t
        cy = y + 12 + int(34 * (1 - (2 * t - 1) ** 2))
        draw.line([tower_x0, y + 12, cx, cy], fill=NAVY, width=2)
        draw.line([cx, cy, cx, deck_y], fill=NAVY, width=1)
    gap = int(w * 0.16)
    mid = x + w // 2
    draw.rectangle([x + 6, deck_y, mid - gap // 2, deck_y + 8], fill=RED)
    draw.rectangle([mid + gap // 2, deck_y, x + w - 6, deck_y + 8], fill=RED)
    draw.line([mid - gap // 2, deck_y + 8, mid - gap // 2 + 12, deck_y + 22],
              fill=RED, width=4)
    starburst(draw, mid, deck_y - 26, 34, 15, (245, 158, 32), (176, 46, 46))
    draw.ellipse([mid - 12, deck_y - 38, mid + 12, deck_y - 14],
                 fill=(255, 226, 120))
    draw.rectangle([x, deck_y + 24, x + w, y + h], fill=SEA)
    wy = deck_y + 30
    if wy + 10 < y + h:
        for wx in range(x + 8, x + w - 8, 34):
            draw.arc([wx, wy, wx + 30, wy + 12], start=180, end=360,
                     fill=(255, 255, 255), width=3)


def draw_tanker(draw, x, y, w, h):
    """An oil tanker on fire near a strait, a carrier on the horizon."""
    draw.rectangle([x, y, x + w, y + h], fill=SKY)
    draw.ellipse([x + 12, y + 10, x + 44, y + 42], fill=(250, 205, 90))
    draw.rectangle([x + w - 140, y + 44, x + w - 24, y + 58],
                   fill=(70, 80, 95))
    draw.rectangle([x + w - 110, y + 30, x + w - 98, y + 44],
                   fill=(70, 80, 95))
    hy = y + int(h * 0.42)
    for i, (sx, sy, sr) in enumerate([(0, 0, 18), (12, -14, 22),
                                     (-10, -26, 26)]):
        cx, cy = x + int(w * 0.30) + sx, y + 56 + sy
        draw.ellipse([cx - sr, cy - sr, cx + sr, cy + sr],
                     fill=(80, 80, 80) if i % 2 else (105, 105, 105))
    hull = [(x + 14, hy), (x + w - 14, hy), (x + w - 32, hy + 32),
            (x + 32, hy + 32)]
    draw.polygon(hull, fill=(40, 40, 48))
    draw.rectangle([x + 28, hy - 26, x + w - 84, hy], fill=(176, 46, 46))
    for i in range(4):
        cx0 = x + 38 + i * 50
        draw.rectangle([cx0, hy - 40, cx0 + 42, hy - 26], fill=(201, 162, 39))
    draw.rectangle([x + w - 78, hy - 46, x + w - 38, hy], fill=(240, 240, 235))
    fx = x + int(w * 0.30)
    draw.polygon([(fx - 20, hy - 24), (fx - 8, hy - 52), (fx + 2, hy - 30),
                  (fx + 12, hy - 50), (fx + 22, hy - 24)],
                 fill=(245, 158, 32), outline=(176, 46, 46))
    draw.polygon([(fx - 9, hy - 24), (fx - 1, hy - 42), (fx + 8, hy - 24)],
                 fill=(255, 226, 120))
    draw.rectangle([x, hy + 34, x + w, y + h], fill=SEA)
    wy = hy + 40
    if wy + 10 < y + h:
        for wx in range(x + 8, x + w - 8, 40):
            draw.arc([wx, wy, wx + 34, wy + 12], start=180, end=360,
                     fill=(255, 255, 255), width=3)


def draw_summit(draw, x, y, w, h):
    """A flight route arcing between two pins: Manila and Shenzhen."""
    draw.rectangle([x, y, x + w, y + h], fill=(226, 236, 244))
    draw.ellipse([x + w - 52, y + 8, x + w - 18, y + 42], fill=(250, 205, 90))
    for cx, cy, cr in [(x + 60, y + 22, 16), (x + 84, y + 30, 20),
                       (x + 300, y + 16, 14)]:
        draw.ellipse([cx - cr, cy - cr // 2, cx + cr, cy + cr // 2],
                     fill=(255, 255, 255))
    # dotted route arc
    for i in range(24):
        t = i / 23
        ax = x + 60 + (w - 130) * t
        ay = y + h - 42 - int(52 * math.sin(t * math.pi))
        draw.ellipse([ax - 3, ay - 3, ax + 3, ay + 3], fill=NAVY)
    plane(draw, x + w - 118, y + 14, 0.9, NAVY)
    # pins (city labels only; the day is named in the panel text above)
    for px, label in [(x + 60, "MANILA"), (x + w - 70, "SHENZHEN")]:
        py = y + h - 34
        draw.ellipse([px - 13, py - 28, px + 13, py - 2], fill=RED,
                     outline=(255, 255, 255), width=2)
        draw.polygon([(px - 11, py - 5), (px + 11, py - 5), (px, py + 12)],
                     fill=RED)
        draw.ellipse([px - 5, py - 21, px + 5, py - 11], fill=(255, 255, 255))
        draw.text((px, py + 14), label, font=SANS_XS, fill=INK, anchor="ma")


def draw_flags_row(draw, x, y, w, h):
    """Five EU flags in a row above a plane flying toward a pin."""
    draw.rectangle([x, y, x + w, y + h], fill=(226, 236, 244))
    flag_defs = [
        ("DE", [(0, 0, 0), (221, 0, 0), (255, 206, 0)]),
        ("DK", [(198, 12, 48), (198, 12, 48), (198, 12, 48)]),
        ("AT", [(237, 41, 43), (255, 255, 255), (237, 41, 43)]),
        ("GR", [(13, 94, 175), (255, 255, 255), (13, 94, 175)]),
        ("NL", [(174, 28, 40), (255, 255, 255), (0, 57, 166)]),
    ]
    fw, fh = 64, 34
    gap = 14
    total = 5 * fw + 4 * gap
    fx = x + (w - total) // 2
    fy = y + 6
    for label, stripes in flag_defs:
        draw.rectangle([fx, fy, fx + fw, fy + fh], outline=INK, width=2)
        band = fh // 3
        for i, col in enumerate(stripes):
            draw.rectangle([fx + 1, fy + 1 + i * band, fx + fw - 1,
                            fy + 1 + (i + 1) * band], fill=col)
        if label == "DK":
            draw.rectangle([fx + 20, fy + 1, fx + 28, fy + fh - 1],
                           fill=(255, 255, 255))
            draw.rectangle([fx + 1, fy + 12, fx + fw - 1, fy + 20],
                           fill=(255, 255, 255))
        if label == "GR":
            draw.rectangle([fx + 1, fy + 1, fx + 22, fy + 19],
                           fill=(13, 94, 175))
            draw.rectangle([fx + 9, fy + 1, fx + 14, fy + 19],
                           fill=(255, 255, 255))
            draw.rectangle([fx + 1, fy + 8, fx + 22, fy + 12],
                           fill=(255, 255, 255))
        draw.text((fx + fw // 2, fy + fh + 4), label, font=SANS_XS,
                  fill=INK, anchor="ma")
        fx += fw + gap
    ry = y + h - 26
    for dx in range(x + 26, x + w - 110, 16):
        draw.ellipse([dx, ry - 2, dx + 5, ry + 3], fill=NAVY)
    # arrowhead at the end of the route, pointing at the pin
    ax = x + w - 92
    draw.polygon([(ax, ry - 9), (ax + 16, ry), (ax, ry + 9)], fill=RED)
    pin_x, pin_y = x + w - 44, y + h - 12
    draw.ellipse([pin_x - 13, pin_y - 28, pin_x + 13, pin_y - 2], fill=RED,
                 outline=(255, 255, 255), width=2)
    draw.polygon([(pin_x - 11, pin_y - 5), (pin_x + 11, pin_y - 5),
                  (pin_x, pin_y + 12)], fill=RED)
    draw.ellipse([pin_x - 5, pin_y - 21, pin_x + 5, pin_y - 11],
                 fill=(255, 255, 255))


def panel(img, draw, x, y, w, h, kicker, kcolor, headline, body, art):
    draw.rectangle([x, y, x + w, y + h], fill=WHITE, outline=INK, width=2)
    draw.rectangle([x, y, x + w, y + 32], fill=kcolor)
    draw.text((x + 12, y + 7), kicker, font=SANS_K, fill=(255, 255, 255))
    ty = y + 42
    for line in wrap(draw, headline, SERIF_P, w - 24):
        draw.text((x + 12, ty), line, font=SERIF_P, fill=INK)
        ty += 34
    by = ty + 4
    for line in wrap(draw, body, SANS, w - 24):
        draw.text((x + 12, by), line, font=SANS, fill=(40, 40, 40))
        by += 26
    art_y = by + 8
    art_h = y + h - 10 - art_y
    if art_h > 40:
        # Draw the illustration on its own layer so anything past its box
        # is clipped instead of spilling over the panel border.
        layer = Image.new("RGB", (w - 24, art_h), WHITE)
        art(ImageDraw.Draw(layer), 0, 0, w - 24, art_h)
        img.paste(layer, (x + 12, art_y))


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    # outer frame
    d.rectangle([6, 6, W - 7, H - 7], outline=NAVY, width=4)
    # masthead
    d.rectangle([10, 10, W - 11, 130], fill=NAVY)
    title = "THE DAILY WORLD"
    tw = d.textlength(title, font=SERIF_B)
    d.text(((W - tw) / 2, 20), title, font=SERIF_B, fill=CREAM)
    d.rectangle([10, 130, W - 11, 134], fill=GOLD)
    dateline = "TUESDAY  ·  17 NOVEMBER 2026  ·  THE WORLD IN ONE DAY"
    dw = d.textlength(dateline, font=SANS_B)
    d.text(((W - dw) / 2, 144), dateline, font=SANS_B, fill=NAVY)
    d.line([40, 174, W - 40, 174], fill=NAVY, width=2)
    # main headline
    head = "A DAY OF BRIDGES AND SUMMITS"
    hw = d.textlength(head, font=SERIF_H)
    d.text(((W - hw) / 2, 184), head, font=SERIF_H, fill=INK)
    sub = ("Ukraine strikes the Kerch Bridge again as Russia hits Kyiv's crossings; "
           "mines hit tankers at Hormuz; Trump flies to Asia for talks with Xi and Putin.")
    sy = 238
    for line in wrap(d, sub, SERIF_S, W - 120):
        lw = d.textlength(line, font=SERIF_S)
        d.text(((W - lw) / 2, sy), line, font=SERIF_S, fill=(60, 58, 52))
        sy += 30
    d.line([40, sy + 6, W - 40, sy + 6], fill=NAVY, width=2)
    # 2 x 2 panels
    top = sy + 20
    pw, ph = 462, 288
    gap = 14
    px0, px1 = 40, 40 + pw + gap
    panel(img, d, px0, top, pw, ph, "EUROPE  ·  WAR", RED,
          "KERCH BRIDGE HIT AGAIN",
          "Ukraine hits the bridge to Crimea again; a road span collapses.",
          draw_bridge)
    panel(img, d, px1, top, pw, ph, "MIDDLE EAST  ·  SHIPPING", TEAL,
          "TANKERS HIT AT HORMUZ",
          "Two tankers strike mines and burn near the strait as a third "
          "US carrier arrives.", draw_tanker)
    panel(img, d, px0, top + ph + gap, pw, ph, "ASIA  ·  DIPLOMACY", NAVY_LIGHT,
          "TRUMP HEADS TO ASIA SUMMIT",
          "Trump lands in Manila for ASEAN; he meets Xi and Putin in "
          "Shenzhen on Thursday.", draw_summit)
    panel(img, d, px1, top + ph + gap, pw, ph, "EUROPE  ·  MIGRATION",
          (122, 90, 20), "EUROPE PLANS RWANDA HUB",
          "Five states agree a joint return facility in Rwanda for rejected "
          "asylum seekers.", draw_flags_row)
    # bottom strip
    by = top + 2 * ph + gap + 14
    d.rectangle([40, by, W - 40, by + 58], fill=NAVY)
    d.text((56, by + 7), "ALSO TODAY", font=SANS_K, fill=GOLD)
    items = ("Pentagon fails audit, ninth year  •  Estonia shuts Russia crossings  "
             "•  JPMorgan blames bug for outage")
    d.text((56, by + 32), items, font=SANS_SM, fill=CREAM)
    foot = "The world's news of Tuesday 17 November 2026, in one image."
    fw = d.textlength(foot, font=SANS_SM)
    d.text(((W - fw) / 2, H - 32), foot, font=SANS_SM, fill=GREY)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    img.save(out, "PNG", optimize=True)
    print(out, os.path.getsize(out), "bytes")


if __name__ == "__main__":
    main()
