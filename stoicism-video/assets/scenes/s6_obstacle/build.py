"""Generates compositions/s6_obstacle.html (static output). Run: python3 assets/scenes/s6_obstacle/build.py"""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../s5_story"))
from inklib import *

P = "s6"
D = 10.54
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))

def g(id_, inner, attrs=""):
    return f'<g id="{id_}"{attrs}>{inner}</g>'

def clip(id_, start, dur, inner):
    return f'<g id="{id_}" class="clip" data-start="{start}" data-duration="{dur}">{inner}</g>'

def T(x, y, s, txt, size, fill=INK, w=900, fam="Playfair Display", italic=False, anchor="middle", extra=""):
    st = ' font-style="italic"' if italic else ""
    return f'<text x="{x}" y="{y}" font-family="{fam}" font-weight="{w}"{st} font-size="{size}" text-anchor="{anchor}" fill="{fill}"{extra}>{txt}</text>'

# ================= world A: Marcus's study (x 0..1080) =================
wallA = path("M-400 -300 H1100 V1082 H-400Z", "#E6D6B5", 0)
stones = "".join(path(wline([(x0, y), (x0 + 180, y + 3)], 300 + i, 2), sw=4, extra=' stroke-opacity=".3"') for i, (x0, y) in enumerate([(-200, 260), (60, 330), (700, 300), (-100, 640), (820, 700), (40, 900)]))
arch = (path(blob([(110, 640), (110, 420), (150, 330), (255, 290), (360, 330), (400, 420), (400, 640)], 301, 3), "#F0C98A") +
        path(ellipse(255, 520, 60, 60, 12, 302, 2), GOLD, 6) +
        path(blob([(110, 640), (180, 560), (260, 600), (330, 545), (400, 640)], 303, 3), OLIVE, 6) +
        path(blob([(318, 640), (336, 470), (352, 640)], 304, 2), "#4F5A33", 5))
column = path(rrect(880, 220, 110, 860, 6, 305), PAPER) + "".join(path(wline([(x, 260), (x, 1060)], 306 + x, 2), sw=4, extra=' stroke-opacity=".5"') for x in (912, 935, 958))
floorA = path("M-400 1080 H1100 V2200 H-400Z", "#D8BE8C", 0) + path(wline([(-400, 1080), (1100, 1080)], 307, 2), sw=8)
desk = (path(rrect(250, 800, 640, 40, 10, 310), "#B9824A") + path(rrect(285, 838, 570, 242, 8, 311), "#A87240") +
        path(wline([(300, 960), (840, 962)], 312, 2), sw=5, extra=' stroke-opacity=".5"'))
book = (path(blob([(560, 800), (585, 700), (720, 712), (720, 806)], 320, 2), PAPER, 6) +
        path(blob([(720, 806), (720, 712), (855, 700), (880, 800)], 321, 2), PAPER, 6) +
        path(wline([(720, 712), (720, 806)], 322, 0), sw=5) +
        "".join(f'<path id="s6-scrib{i}" d="{wline([(x0, y), (x0 + 110, y - 2)], 330 + i, 3)}" fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round" pathLength="1" stroke-dasharray="1 1.2" stroke-dashoffset="1.1"/>'
                for i, (x0, y) in enumerate([(598, 735), (594, 755), (590, 775), (736, 735), (738, 755)])) +
        T(640, 868, 0, "Meditations", 34, PAPER, 700, italic=True))
candle = path(rrect(810, 730, 34, 72, 6, 340), PAPER) + g("s6-flame", path("M827 690 Q845 712 836 726 Q827 734 818 726 Q810 712 827 690Z", GOLD, 5))
inkpot = path(rrect(500, 770, 40, 32, 8, 341), INK)
marcus = f'''<!-- CHAR:marcus -->
<g id="s6-marcus" transform="translate(420 1078) scale(1)">{ph_marcus(P, seated=True)}</g>
<!-- /CHAR:marcus -->'''
quill = g("s6-quill", path(blob([(0, 0), (40, -95), (58, -150), (36, -100), (8, -2)], 342, 1), PAPER, 5) + f'<circle cx="2" cy="2" r="16" fill="{SKIN}" stroke="{INK}" stroke-width="6"/>')
quill_arm = path(wline([(482, 760), (600, 760)], 343, 1), sw=40, stroke=INK) + path(wline([(482, 760), (600, 760)], 343, 1), sw=26, stroke=PAPER)

worldA = f'''<g class="ink">{wallA}{stones}{arch}{column}{floorA}</g>
<g id="s6-marcus-mv">{marcus}</g>
<g class="ink">{desk}{book}{candle}{inkpot}{quill_arm}<g transform="translate(610 762)">{quill}</g></g>'''

# ================= world B: the path (local x 0..1080, placed at +1080) =================
sky = path("M-300 -300 H1500 V1082 H-300Z", "#E9DCBC", 0)
hills = (path(blob([(-300, 1082), (-300, 820), (60, 700), (380, 800), (700, 690), (1100, 760), (1500, 700), (1500, 1082)], 400, 6), "#C9C58E", 6) +
         path(blob([(-300, 1082), (-300, 930), (200, 880), (520, 950), (900, 900), (1500, 960), (1500, 1082)], 401, 6), "#A9AE72", 6))
sun = path(ellipse(900, 380, 70, 70, 14, 402, 2), GOLD, 6)
cliff = path(blob([(980, 1082), (970, 640), (1010, 600), (1150, 590), (1500, 600), (1500, 1082)], 403, 4), "#B98F5E", 7) + path(wline([(985, 640), (1300, 630)], 404, 2), sw=6)
groundB = path("M-300 1080 H1500 V2200 H-300Z", "#D8BE8C", 0) + path(wline([(-300, 1080), (1500, 1080)], 405, 2), sw=8)
pathline = path(wline([(-300, 1110), (400, 1105)], 406, 3), sw=5, extra=' stroke-dasharray="18 22" stroke-opacity=".5"')
boulder = g("s6-boulder", path(blob([(400, 1080), (392, 860), (420, 760), (520, 718), (600, 740), (624, 840), (620, 1080)], 410, 4), "#9A9184") +
            path(wline([(470, 800), (500, 860), (480, 930)], 411, 2), sw=5) + path(wline([(560, 980), (590, 1020)], 412, 2), sw=5))
dust = "".join(g(f"s6-dust{i}", path(cloud(0, 0, 34, 22, 6, 0.6, 420 + i), PAPER, 5), f' transform="translate({x} 1060)"') for i, x in enumerate([600, 700, 860, 990]))
alex = f'''<g id="s6-alex-mv"><g id="s6-alex-lean"><!-- CHAR:alex -->
<g id="s6-alex" transform="translate(300 1078) scale(1)">{ph_alex(P)}</g>
<!-- /CHAR:alex --></g></g>'''
stars = g("s6-bonk-in", "".join(path(burst(x, y, 7, 18, 5, 430 + i), GOLD, 4) for i, (x, y) in enumerate([(330, 530), (380, 500), (420, 550)])))
sweat = g("s6-sweat-in", path("M230 560 Q250 590 240 605 Q225 615 217 600 Q215 585 230 560Z", SKY, 5))

# props (world-B coords), held at Alex's screen-left hand while he stands on the step (x 800, feet 860)
letter = g("s6-letter-in", path(blob([(470, 540), (690, 532), (700, 820), (478, 830)], 440, 3), PAPER) +
           "".join(path(wline([(500, y), (660, y + 2)], 441 + i, 2), sw=4, extra=' stroke-opacity=".5"') for i, y in enumerate([580, 610, 640, 760, 790])) +
           T(510, 600, 0, "Dear Alex,", 34, INK, 700, italic=True, anchor="start", extra=' opacity="0"') +
           g("s6-stamp", path(rrect(486, 662, 200, 70, 10, 442), "none", 7, TERRA) + T(586, 711, 0, "REJECTED", 36, TERRA, 900, "Inter"), ' transform="rotate(-10 586 697)"'))
dumbbell = g("s6-dumb-in", path(rrect(540, 672, 150, 18, 8, 450), "#6E6A63", 6) +
             path(rrect(510, 630, 42, 100, 10, 451), INK, 6) + path(rrect(678, 630, 42, 100, 10, 452), INK, 6))
reps = "".join(g(f"s6-rep{i}", T(620, 560, 0, str(i + 1), 72, GOLD, 900, extra=f' stroke="{INK}" stroke-width="6" paint-order="stroke"')) for i in range(2))
exam = g("s6-exam-in", path(blob([(470, 540), (690, 532), (700, 820), (478, 830)], 460, 3), PAPER) +
         T(500, 590, 0, "EXAM", 36, INK, 900, "Inter", anchor="start") +
         "".join(path(wline([(500, y), (580, y + 2)], 461 + i, 2), sw=4, extra=' stroke-opacity=".5"') for i, y in enumerate([640, 680, 720, 760])) +
         path(ellipse(632, 700, 62, 72, 12, 462, 3), "none", 7, TERRA) + T(632, 745, 0, "F", 130, TERRA, 900))
mapg = g("s6-map-in", path(blob([(450, 545), (520, 530), (600, 550), (700, 528), (712, 700), (704, 832), (620, 820), (530, 840), (462, 826), (456, 700)], 470, 4), "#EED39A") +
         f'<path id="s6-trail" d="{wline([(490, 800), (540, 760), (520, 700), (600, 680), (640, 620)], 471, 3)}" fill="none" stroke="{TERRA}" stroke-width="6" stroke-linecap="round" stroke-dasharray="14 14"/>' +
         path(wline([(470, 600), (520, 590), (540, 620)], 472, 2), sw=4, extra=' stroke-opacity=".5"') +
         g("s6-x1", path("M610 600 l40 40 M650 600 l-40 40", sw=9, stroke=TERRA) + T(632, 590, 0, "Ch. 4", 36, INK, 900)) +
         g("s6-x2", path("M498 700 l36 36 M534 700 l-36 36", sw=9, stroke=TERRA) + T(560, 780, 0, "Ch. 7", 36, INK, 900, anchor="start")))
sparkle = g("s6-sparkle-in", path(burst(660, 600, 10, 34, 4, 480), GOLD, 5))

worldB = f'''<g transform="translate(1080 0)">
<g id="s6-farB" class="ink">{sky}{sun}{hills}</g>
<g class="ink">{cliff}{groundB}{pathline}</g>
<g class="ink">{boulder}{dust}</g>
{alex}
<g class="ink">
  {clip("s6-bonk", 2.49, 0.6, stars)}
  {clip("s6-sweat", 2.7, 0.6, sweat)}
  {clip("s6-letter", 4.3, 1.45, letter)}
  {clip("s6-dumb", 5.55, 1.45, dumbbell)}
  {clip("s6-reps", 5.9, 1.0, reps)}
  {clip("s6-exam", 6.91, 1.34, exam)}
  {clip("s6-map", 8.17, round(D - 8.17, 2), mapg)}
  {clip("s6-sparkle", 10.1, 0.44, sparkle)}
</g>
</g>'''

# ================= screen-space lettering =================
rule = g("s6-rule-in", path(blob([(230, 290), (850, 270), (862, 500), (240, 515)], 500, 5), PAPER) +
         f'<text x="545" y="455" font-family="Playfair Display" font-weight="900" font-size="168" text-anchor="middle" fill="{INK}">RULE <tspan fill="{GOLD}" stroke="{INK}" stroke-width="7" paint-order="stroke">3</tspan></text>')
words1 = [("What", 0), ("stands", 1), ("in", 2), ("the", 3), ("way", 4)]
words2 = [("becomes", 5), ("the", 6), ("way.", 7)]
q1 = " ".join(f'<tspan id="s6-qw{i}" fill-opacity="0">{w}</tspan>' for w, i in words1)
q2 = " ".join(f'<tspan id="s6-qw{i}" fill-opacity="0">{w}</tspan>' for w, i in words2)
quote = g("s6-quote-in", path(blob([(80, 236), (720, 226), (732, 478), (88, 488)], 510, 5), PAPER) +
          T(98, 316, 0, "&#8220;", 110, GOLD, 900, anchor="start") +
          f'<text x="150" y="320" font-family="Playfair Display" font-style="italic" font-weight="700" font-size="56" fill="{INK}">{q1}</text>' +
          f'<text x="150" y="392" font-family="Playfair Display" font-style="italic" font-weight="700" font-size="56" fill="{INK}">{q2}</text>' +
          g("s6-cite", T(150, 450, 0, "Meditations 5.20", 34, TERRA, 700, italic=True, anchor="start")))

wipe_d = "M0 -100 H1300 L1240 200 L1330 520 L1250 840 L1320 1180 L1240 1500 L1310 1820 L1260 2050 H0Z"

svg = f'''<svg id="s6-stage" viewBox="0 0 1080 1920" width="1080" height="1920" style="position:absolute;inset:0;overflow:hidden">
  <defs>
    <filter id="s6-ink" class="ink-boil" x="-15%" y="-15%" width="130%" height="130%" color-interpolation-filters="sRGB">
      <feTurbulence class="ink-turb" type="fractalNoise" baseFrequency="0.035" numOctaves="2" seed="1" result="n"/>
      <feDisplacementMap in="SourceGraphic" in2="n" scale="5" xChannelSelector="R" yChannelSelector="G"/>
    </filter>
    <filter id="s6-whipblur" x="-20%" y="-5%" width="140%" height="110%"><feGaussianBlur id="s6-whipblur-b" stdDeviation="0 0"/></filter>
  </defs>
  <g id="s6-whip" filter="url(#s6-whipblur)">
  <g id="s6-shake"><g id="s6-cam"><g id="s6-pan">
    {worldA}
    {worldB}
  </g></g></g>
  <g class="ink">{clip("s6-rule", 0.12, 1.6, rule)}{clip("s6-quote", 1.7, 2.85, quote)}</g>
  </g>
  {clip("s6-wipe-in", 0, 0.32, f'<path id="s6-wipe-in-p" d="{wipe_d}" fill="{INK}"/>')}
  {clip("s6-wipe-out", 10.23, 0.31, f'<g transform="scale(-1 1) translate(-1080 0)"><path id="s6-wipe-out-p" d="{wipe_d}" fill="{INK}"/></g>')}
</svg>'''

script = r'''
  (function () {
    const D = 10.54;
    const tl = gsap.timeline({ paused: true });
    const seen = new Set();
    function F(sel, from, to, at) {
      const keys = Object.keys(from).filter(k => k !== "svgOrigin" && k !== "transformOrigin");
      const fresh = keys.every(k => !seen.has(sel + "|" + k));
      keys.forEach(k => seen.add(sel + "|" + k));
      tl.fromTo(sel, from, Object.assign({ immediateRender: fresh }, to), at);
    }
    function shake(t0, amps) {
      amps.concat([[0, 0]]).forEach((a, i) => F("#s6-shake", { x: i ? amps[i - 1][0] : 0, y: i ? amps[i - 1][1] : 0 }, { x: a[0], y: a[1], duration: 1 / 30, ease: "none" }, t0 + i / 30));
    }
    const stage = document.querySelector("#s6-stage");
    if (window.Rig && !Rig.__stub) {
      Rig.boil(tl, stage, 0, D);
    } else {
      stage.querySelectorAll(".ink").forEach(el => el.setAttribute("filter", "url(#s6-ink)"));
      for (let i = 0; i < Math.ceil(D * 12); i++) tl.set("#s6-ink .ink-turb", { attr: { seed: [1, 4, 9][i % 3] } }, i / 12);
    }

    // ---- in: ink wipe + whip ----
    F("#s6-wipe-in-p", { x: 0 }, { x: -1400, duration: 0.3, ease: "power2.in" }, 0);
    F("#s6-cam", { x: 160, scale: 1, svgOrigin: "540 800" }, { x: 0, scale: 1, duration: 0.42, ease: "power3.out" }, 0);
    F("#s6-whipblur-b", { attr: { stdDeviation: "18 0" } }, { attr: { stdDeviation: "0 0" }, duration: 0.3, ease: "power2.out" }, 0);

    // ---- RULE 3 ----
    F("#s6-rule-in", { opacity: 0, scale: 1.5, rotation: 8, svgOrigin: "545 390" }, { opacity: 1, scale: 1, rotation: 3, duration: 0.32, ease: "back.out(2.2)" }, 0.15);
    F("#s6-rule-in", { opacity: 1, y: 0 }, { opacity: 0, y: -40, duration: 0.22, ease: "power2.in" }, 1.45);

    // ---- "Marcus wrote": quill scribbles, lines ink in ----
    F("#s6-flame", { scaleY: 1, svgOrigin: "827 726" }, { scaleY: 1.15, duration: 0.3, yoyo: true, repeat: 5, ease: "sine.inOut" }, 0);
    F("#s6-marcus-mv", { y: 0 }, { y: 6, duration: 0.25, ease: "power2.out" }, 0.73);
    const qk = [[0, 0], [30, -4], [12, 6], [50, 2], [26, 10], [70, 4], [44, 14], [90, 10], [60, 18]];
    qk.forEach((k, i) => { if (i) F("#s6-quill", { x: qk[i - 1][0], y: qk[i - 1][1] }, { x: k[0], y: k[1], duration: 0.065, ease: "none" }, 1.19 + (i - 1) * 0.065); });
    [0, 1, 2, 3, 4].forEach(i => F("#s6-scrib" + i, { attr: { "stroke-dashoffset": 1.1 } }, { attr: { "stroke-dashoffset": 0 }, duration: 0.12, ease: "none" }, 1.19 + i * 0.1));

    // ---- whip pan to the path ----
    F("#s6-pan", { x: 0 }, { x: -1080, duration: 0.38, ease: "power3.inOut" }, 1.6);
    F("#s6-whipblur-b", { attr: { stdDeviation: "0 0" } }, { attr: { stdDeviation: "22 0" }, duration: 0.19, ease: "power2.in" }, 1.6);
    F("#s6-whipblur-b", { attr: { stdDeviation: "22 0" } }, { attr: { stdDeviation: "0 0" }, duration: 0.19, ease: "power2.out" }, 1.79);
    F("#s6-farB", { x: 120 }, { x: 0, duration: 0.6, ease: "power3.out" }, 1.6);

    // ---- quote writes itself, word by word on the voice ----
    F("#s6-quote-in", { opacity: 0, y: 20 }, { opacity: 1, y: 0, duration: 0.2, ease: "power3.out" }, 1.66);
    [1.72, 2.03, 2.49, 2.64, 2.87, 3.10, 3.58, 3.86].forEach((t, i) => F("#s6-qw" + i, { attr: { "fill-opacity": 0 } }, { attr: { "fill-opacity": 1 }, duration: 0.12 }, t));
    F("#s6-cite", { opacity: 0 }, { opacity: 1, duration: 0.2 }, 3.9);
    F("#s6-quote-in", { opacity: 1 }, { opacity: 0, y: -30, duration: 0.25, ease: "power2.in" }, 4.26);

    // ---- Alex walks in and bonks the boulder ("stands in the way") ----
    for (let i = 0; i < 4; i++) F("#s6-alex-mv", { x: -450 + i * 112, y: 0 }, { x: -450 + (i + 1) * 112 - 4, y: -10, duration: 0.09, ease: "power1.out" }, 1.75 + i * 0.18);
    for (let i = 0; i < 4; i++) F("#s6-alex-mv", { x: -450 + (i + 1) * 112 - 4, y: -10 }, { x: -450 + (i + 1) * 112, y: 0, duration: 0.09, ease: "power1.in" }, 1.84 + i * 0.18);
    F("#s6-alex-mv", { x: -2 }, { x: 0, duration: 0.03 }, 2.46);
    F("#s6-alex-lean", { scaleX: 1, scaleY: 1, svgOrigin: "300 1078" }, { scaleX: 0.9, scaleY: 1.06, duration: 0.06, yoyo: true, repeat: 1, ease: "power2.out" }, 2.49);
    F("#s6-alex-mv", { x: 0 }, { x: -30, duration: 0.18, ease: "power2.out" }, 2.5);
    F("#s6-bonk-in", { scale: 0.3, rotation: 0, svgOrigin: "380 530" }, { scale: 1, rotation: 40, duration: 0.5, ease: "power2.out" }, 2.49);
    shake(2.49, [[6, -3], [-5, 2], [3, 3]]);
    // push ("the way")
    F("#s6-alex-mv", { x: -30 }, { x: 0, duration: 0.15, ease: "power2.out" }, 2.72);
    F("#s6-alex-lean", { rotation: 0 }, { rotation: 12, duration: 0.15, ease: "power2.out" }, 2.72);
    F("#s6-sweat-in", { scale: 0, svgOrigin: "230 600" }, { scale: 1, duration: 0.15, ease: "back.out(3)" }, 2.75);
    [[2], [-2], [2.5], [-1], [0]].forEach((r, i, a) => F("#s6-boulder", { rotation: i ? a[i - 1][0] : 0, svgOrigin: "620 1080" }, { rotation: r[0], duration: 0.07, ease: "none" }, 2.75 + i * 0.07));
    // "becomes": tips over into a step
    F("#s6-boulder", { rotation: 0 }, { rotation: 90, duration: 0.33, ease: "power2.in" }, 3.10);
    F("#s6-boulder", { rotation: 90 }, { rotation: 87, duration: 0.08, yoyo: true, repeat: 1, ease: "power2.out" }, 3.43);
    F("#s6-alex-lean", { rotation: 12 }, { rotation: 0, duration: 0.25, ease: "back.out(2)" }, 3.15);
    [0, 1, 2, 3].forEach(i => F("#s6-dust" + i, { scale: 0, opacity: 1, svgOrigin: "0 0" }, { scale: 1.3, opacity: 0, duration: 0.5, ease: "power2.out" }, 3.43 + i * 0.03));
    shake(3.43, [[0, 8], [0, -6], [0, 4], [0, -2]]);
    // "the way": climb onto the step
    F("#s6-alex-lean", { scaleY: 1, scaleX: 1 }, { scaleY: 0.9, scaleX: 1.05, duration: 0.1, ease: "power2.out" }, 3.5);
    F("#s6-alex-lean", { scaleY: 0.9, scaleX: 1.05 }, { scaleY: 1.06, scaleX: 0.96, duration: 0.15, ease: "power2.out" }, 3.6);
    F("#s6-alex-mv", { x: 0 }, { x: 500, duration: 0.55, ease: "power1.inOut" }, 3.58);
    F("#s6-alex-mv", { y: 0 }, { y: -320, duration: 0.3, ease: "power2.out" }, 3.58);
    F("#s6-alex-mv", { y: -320 }, { y: -220, duration: 0.25, ease: "power2.in" }, 3.88);
    F("#s6-alex-lean", { scaleY: 1.06, scaleX: 0.96 }, { scaleY: 1, scaleX: 1, duration: 0.3, ease: "back.out(3)" }, 4.13);

    // ---- camera pushes in on Alex atop the step for the gags ----
    F("#s6-cam", { scale: 1, x: 0, y: 0 }, { scale: 1.1, x: -30, y: 10, duration: 0.6, ease: "power2.inOut" }, 4.2);

    // ---- "rejected" -> "reps" ----
    F("#s6-letter-in", { y: -520, rotation: -20, svgOrigin: "585 685" }, { y: 0, rotation: 0, duration: 0.32, ease: "power2.out" }, 4.3);
    F("#s6-stamp", { scale: 1.8, opacity: 0, svgOrigin: "586 697" }, { scale: 1, opacity: 1, duration: 0.15, ease: "power3.in" }, 4.62);
    shake(4.77, [[4, -2], [-3, 2]]);
    F("#s6-alex-mv", { y: -220 }, { y: -208, duration: 0.3, ease: "power2.out" }, 4.7);
    F("#s6-letter-in", { scaleX: 1, scaleY: 1 }, { scaleX: 0.2, scaleY: 0.08, duration: 0.15, ease: "power3.in" }, 5.42);
    F("#s6-dumb-in", { scale: 0.2, svgOrigin: "615 680" }, { scale: 1, duration: 0.2, ease: "back.out(3)" }, 5.55);
    F("#s6-alex-mv", { y: -208 }, { y: -220, duration: 0.2, ease: "power2.out" }, 5.55);
    [[5.67, 0], [6.1, 1]].forEach(([t, i]) => {
      F("#s6-dumb-in", { y: 0 }, { y: -150, duration: 0.2, ease: "power2.out" }, t);
      F("#s6-dumb-in", { y: -150 }, { y: 0, duration: 0.2, ease: "power2.in" }, t + 0.22);
      F("#s6-rep" + i, { opacity: 0, scale: 0.4, y: 0, svgOrigin: "620 540" }, { opacity: 1, scale: 1, y: -40, duration: 0.25, ease: "back.out(3)" }, t + 0.18);
      F("#s6-rep" + i, { opacity: 1 }, { opacity: 0, duration: 0.15 }, t + 0.4);
    });
    F("#s6-dumb-in", { y: 0 }, { y: -170, duration: 0.25, ease: "back.out(2)" }, 6.55);

    // ---- "failed an exam" -> treasure map ----
    F("#s6-exam-in", { x: -500, rotation: -30, svgOrigin: "585 685" }, { x: 0, rotation: 0, duration: 0.2, ease: "power3.out" }, 6.91);
    shake(7.1, [[5, 2], [-4, -2], [2, 1]]);
    F("#s6-alex-mv", { y: -220 }, { y: -206, duration: 0.3, ease: "power2.out" }, 7.12);
    F("#s6-exam-in", { scaleX: 1 }, { scaleX: 0, duration: 0.12, ease: "power2.in" }, 8.05);
    F("#s6-map-in", { scaleX: 0, svgOrigin: "585 685" }, { scaleX: 1, duration: 0.14, ease: "power2.out" }, 8.17);
    F("#s6-alex-mv", { y: -206 }, { y: -240, duration: 0.18, ease: "power2.out" }, 8.53);
    F("#s6-alex-mv", { y: -240 }, { y: -220, duration: 0.22, ease: "bounce.out" }, 8.71);
    F("#s6-x1", { scale: 0, svgOrigin: "630 620" }, { scale: 1, duration: 0.2, ease: "back.out(3)" }, 8.86);
    F("#s6-x2", { scale: 0, svgOrigin: "516 718" }, { scale: 1, duration: 0.2, ease: "back.out(3)" }, 9.12);
    F("#s6-trail", { attr: { "stroke-dashoffset": 120 } }, { attr: { "stroke-dashoffset": 0 }, duration: 0.8, ease: "none" }, 9.38);
    F("#s6-sparkle-in", { scale: 0, rotation: 0, svgOrigin: "660 600" }, { scale: 1.2, rotation: 45, duration: 0.3, ease: "back.out(2)" }, 10.1);
    F("#s6-cam", { scale: 1.1 }, { scale: 1.14, duration: 1.4, ease: "sine.inOut" }, 8.8);

    // ---- out: ink wipe from the right + whip ----
    F("#s6-wipe-out-p", { x: -1400 }, { x: 0, duration: 0.27, ease: "power2.in" }, 10.23);
    F("#s6-whipblur-b", { attr: { stdDeviation: "0 0" } }, { attr: { stdDeviation: "18 0" }, duration: 0.28, ease: "power2.in" }, 10.23);

    window.__timelines["s6_obstacle"] = tl;
  })();
'''

html = f'''<template>
  <style>
    #root {{ position: absolute; inset: 0; }}
    #s6-world {{ position: absolute; inset: 0; }}
  </style>
  <div id="root" data-composition-id="s6_obstacle" data-width="1080" data-height="1920">
    <div id="s6-world" class="clip" data-start="0" data-duration="{D}">
{svg}
    </div>
  </div>
  <script>{script}</script>
</template>
'''
open(os.path.join(ROOT, "compositions/s6_obstacle.html"), "w").write(html)
print("wrote s6_obstacle.html", len(html))
