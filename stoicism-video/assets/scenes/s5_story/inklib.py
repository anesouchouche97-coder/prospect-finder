"""Build-time helpers for Animator 3's scenes (s5_story, s6_obstacle).
Outputs static SVG path strings; seeded jitter at BUILD time only (the HTML is static)."""
import math
import random

INK = "#1E1A16"
PARCH = "#F3E9D2"
PAPER = "#FBF4E3"
TERRA = "#C65A3A"
GOLD = "#E0A84A"
OLIVE = "#7A8450"
TYRIAN = "#6B2D5C"
SKY = "#8DB1C4"
SKIN = "#EFC9A2"


def f(v):
    return f"{v:.1f}".rstrip("0").rstrip(".")


def blob(pts, seed=1, j=3.0, closed=True):
    """Smooth hand-drawn closed shape through pts (quadratic through midpoints), with jitter."""
    rnd = random.Random(seed)
    p = [(x + rnd.uniform(-j, j), y + rnd.uniform(-j, j)) for x, y in pts]
    n = len(p)
    if closed:
        mids = [((p[i][0] + p[(i + 1) % n][0]) / 2, (p[i][1] + p[(i + 1) % n][1]) / 2) for i in range(n)]
        d = f"M{f(mids[-1][0])} {f(mids[-1][1])}"
        for i in range(n):
            d += f" Q{f(p[i][0])} {f(p[i][1])} {f(mids[i][0])} {f(mids[i][1])}"
        return d + "Z"
    d = f"M{f(p[0][0])} {f(p[0][1])}"
    for i in range(1, n - 1):
        mx, my = (p[i][0] + p[i + 1][0]) / 2, (p[i][1] + p[i + 1][1]) / 2
        d += f" Q{f(p[i][0])} {f(p[i][1])} {f(mx)} {f(my)}"
    d += f" L{f(p[-1][0])} {f(p[-1][1])}"
    return d


def wline(pts, seed=1, j=2.5):
    """Wobbly polyline (open), each segment subdivided with jitter."""
    rnd = random.Random(seed)
    out = []
    for i in range(len(pts) - 1):
        (x0, y0), (x1, y1) = pts[i], pts[i + 1]
        seg = max(1, int(math.hypot(x1 - x0, y1 - y0) / 60))
        for k in range(seg):
            t = k / seg
            jj = j if (i or k) else 0
            out.append((x0 + (x1 - x0) * t + rnd.uniform(-jj, jj), y0 + (y1 - y0) * t + rnd.uniform(-jj, jj)))
    out.append(pts[-1])
    return blob(out, seed, 0, closed=False)


def rrect(x, y, w, h, r=18, seed=1, j=2.5):
    """Hand-drawn rounded rectangle."""
    pts = []
    for (cx, cy, a0) in [(x + w - r, y + r, -90), (x + w - r, y + h - r, 0), (x + r, y + h - r, 90), (x + r, y + r, 180)]:
        for k in range(3):
            a = math.radians(a0 + k * 45)
            pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    # add mid points on long edges
    full = []
    for i in range(len(pts)):
        full.append(pts[i])
        nx, ny = pts[(i + 1) % len(pts)]
        dist = math.hypot(nx - pts[i][0], ny - pts[i][1])
        if dist > 120:
            steps = int(dist / 110)
            for s in range(1, steps + 1):
                t = s / (steps + 1)
                full.append((pts[i][0] + (nx - pts[i][0]) * t, pts[i][1] + (ny - pts[i][1]) * t))
    return blob(full, seed, j)


def ellipse(cx, cy, rx, ry, n=14, seed=1, j=2.0):
    return blob([(cx + rx * math.cos(2 * math.pi * i / n), cy + ry * math.sin(2 * math.pi * i / n)) for i in range(n)], seed, j)


def cloud(cx, cy, rx, ry, n=11, bump=0.55, seed=1, j=4.0):
    """Bumpy thought-cloud outline."""
    rnd = random.Random(seed)
    pts = []
    for i in range(n):
        a = 2 * math.pi * i / n + rnd.uniform(-0.08, 0.08)
        pts.append((cx + rx * math.cos(a) + rnd.uniform(-j, j), cy + ry * math.sin(a) + rnd.uniform(-j, j)))
    d = f"M{f(pts[0][0])} {f(pts[0][1])}"
    for i in range(n):
        x1, y1 = pts[(i + 1) % n]
        x0, y0 = pts[i]
        r = math.hypot(x1 - x0, y1 - y0) * bump * rnd.uniform(0.9, 1.1)
        d += f" A{f(r)} {f(r)} 0 0 1 {f(x1)} {f(y1)}"
    return d + "Z"


def burst(cx, cy, r0, r1, n=12, seed=1):
    rnd = random.Random(seed)
    pts = []
    for i in range(2 * n):
        a = math.pi * i / n
        r = (r1 if i % 2 == 0 else r0) * rnd.uniform(0.88, 1.1)
        pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    return "M" + " L".join(f"{f(x)} {f(y)}" for x, y in pts) + "Z"


def path(d, fill="none", sw=7, stroke=INK, extra=""):
    return f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" stroke-linejoin="round" stroke-linecap="round"{extra}/>'


# ---------------- placeholder characters (feet anchor 0,0; RIG_API faces at -500..-370) ----------------

def ph_person(pfx, name, hood, legs, skin=SKIN, seated=False, extra_head="", extra_body="", seed=3):
    """Placeholder adult ~530 tall, front view. ids: {pfx}-{name}-ph-*"""
    s = seed
    out = [f'<g class="ink ph-char" id="{pfx}-{name}-ph">']
    if seated:
        out.append(path(blob([(-62, -160), (62, -160), (78, -120), (70, -95), (-70, -95), (-78, -120)], s, 2), legs))
        out.append(path(blob([(-66, -110), (-24, -110), (-30, -10), (-62, -10)], s + 1, 2), legs))
        out.append(path(blob([(24, -110), (66, -110), (62, -10), (30, -10)], s + 2, 2), legs))
    else:
        out.append(path(blob([(-58, -165), (-6, -165), (-14, -16), (-52, -16)], s + 1, 2), legs))
        out.append(path(blob([(6, -165), (58, -165), (52, -16), (14, -16)], s + 2, 2), legs))
    out.append(path(blob([(-72, -24), (-10, -24), (-6, 2), (-80, 2)], s + 3, 1.5), INK))
    out.append(path(blob([(10, -24), (72, -24), (80, 2), (6, 2)], s + 4, 1.5), INK))
    # torso
    out.append(path(blob([(-82, -345), (82, -345), (96, -300), (86, -150), (-86, -150), (-96, -300)], s + 5, 3), hood))
    out.append(extra_body)
    # arms (static rest)
    out.append(path(blob([(-84, -335), (-58, -320), (-80, -185), (-104, -190)], s + 6, 2), hood))
    out.append(path(blob([(84, -335), (58, -320), (80, -185), (104, -190)], s + 7, 2), hood))
    out.append(path(ellipse(-92, -175, 18, 18, 8, s + 8, 1), skin, 6))
    out.append(path(ellipse(92, -175, 18, 18, 8, s + 9, 1), skin, 6))
    # head
    out.append(f'<g id="{pfx}-{name}-ph-head">')
    out.append(path(ellipse(0, -440, 84, 92, 16, s + 10, 2), skin))
    out.append(extra_head)
    out.append(f'<g id="{pfx}-{name}-ph-eyes">')
    for ex in (-30, 30):
        out.append(path(ellipse(ex, -450, 15, 19, 10, s + 11 + ex, 1), "#FFFDF6", 5))
        out.append(f'<circle cx="{ex + 3}" cy="-447" r="8" fill="{INK}"/>')
    out.append('</g>')
    out.append(path(wline([(-48, -486), (-14, -492)], s + 12, 1), sw=7))
    out.append(path(wline([(14, -492), (48, -486)], s + 13, 1), sw=7))
    out.append(f'<path id="{pfx}-{name}-ph-mouth" d="M-22 -400 Q0 -386 22 -400" fill="none" stroke="{INK}" stroke-width="7" stroke-linecap="round"/>')
    out.append('</g>')
    out.append('</g>')
    return "\n".join(out)


def ph_alex(pfx, seated=False):
    hair = path(blob([(-86, -470), (-70, -528), (-20, -546), (40, -540), (82, -500), (86, -462), (40, -500), (-30, -505)], 41, 3), INK)
    hoodstr = path(wline([(-20, -340), (-24, -290)], 42, 1), sw=5) + path(wline([(20, -340), (24, -290)], 43, 1), sw=5)
    return ph_person(pfx, "alex", GOLD, SKY, seated=seated, extra_head=hair, extra_body=hoodstr, seed=5)


def ph_marcus(pfx, seated=False):
    beard = path(blob([(-78, -430), (-60, -378), (-30, -350), (0, -342), (30, -350), (60, -378), (78, -430), (40, -398), (0, -392), (-40, -398)], 51, 3), "#5A4636")
    laurel = "".join(path(ellipse(x, y, 20, 10, 8, 52 + i, 1), OLIVE, 5, extra=f' transform="rotate({r} {x} {y})"')
                     for i, (x, y, r) in enumerate([(-74, -498), (-50, -524), (-20, -538), (20, -538), (50, -524), (74, -498)]))
    hair = path(blob([(-84, -466), (-70, -520), (0, -536), (70, -520), (84, -466), (40, -504), (-40, -504)], 53, 3), "#5A4636")
    stripe = path(blob([(-82, -340), (-50, -345), (70, -170), (40, -150)], 54, 2), TYRIAN, 5)
    return ph_person(pfx, "marcus", PAPER, PAPER, seated=seated, extra_head=hair + beard + laurel, extra_body=stripe, seed=7)
