"""Generates compositions/s5_story.html (static output). Run: python3 assets/scenes/s5_story/build.py"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from inklib import *

P = "s5"
D = 12.51
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))

def g(id_, inner, cls="", attrs=""):
    c = f' class="{cls}"' if cls else ""
    return f'<g id="{id_}"{c}{attrs}>{inner}</g>'

def clip(id_, start, dur, inner):
    return f'<g id="{id_}" class="clip" data-start="{start}" data-duration="{dur}">{inner}</g>'

# ---------------- environment ----------------
wall = path(f"M-300 -300 H1380 V1082 H-300Z", "#EBDDC0", 0)
stripes = "".join(f'<path d="M{x} -300 V1080" stroke="{GOLD}" stroke-opacity=".22" stroke-width="10"/>' for x in range(-260, 1400, 92))
floor = path("M-300 1080 H1380 V2200 H-300Z", "#DCC59A", 0)
planks = "".join(path(wline([(-300, y), (1380, y + 6)], 60 + i, 3), sw=4, stroke=INK, extra=' stroke-opacity=".35"') for i, y in enumerate([1180, 1320, 1500, 1720]))
base = path(wline([(-300, 1080), (1380, 1080)], 61, 2), sw=8)
window = (path(rrect(650, 285, 250, 270, 14, 62), "#55707F") +
          path(ellipse(800, 360, 34, 34, 12, 63, 1), PAPER, 5) + path(ellipse(814, 352, 30, 30, 12, 64, 1), "#55707F", 0) +
          "".join(f'<path d="M{x-7} {y}h14M{x} {y-7}v14" stroke="{PAPER}" stroke-width="4" stroke-linecap="round"/>' for x, y in [(700, 330), (730, 470), (860, 480), (690, 410)]) +
          path(wline([(775, 285), (775, 555)], 65, 1), sw=7) + path(wline([(650, 420), (900, 420)], 66, 1), sw=7) +
          path(blob([(630, 270), (680, 270), (670, 580), (622, 590)], 67, 3), TERRA) + path(blob([(870, 270), (920, 270), (928, 590), (880, 580)], 68, 3), TERRA))
frame = path(rrect(260, 300, 170, 140, 8, 69), PAPER) + path(wline([(280, 420), (330, 360), (360, 390), (410, 330)], 70, 2), sw=6)
plant = (path(blob([(905, 1000), (985, 1000), (975, 1078), (915, 1078)], 71, 2), TERRA) +
         "".join(path(ellipse(x, y, 22, 52, 10, 72 + i, 2), OLIVE, 6, extra=f' transform="rotate({r} {x} {y})"') for i, (x, y, r) in enumerate([(925, 930, -25), (948, 905, 0), (972, 930, 25)])))
couch_back = path(rrect(220, 755, 600, 160, 40, 80), OLIVE)
couch_front = (path(rrect(250, 878, 540, 90, 28, 81), "#8E9A62") + path(rrect(190, 830, 95, 190, 30, 82), OLIVE) +
               path(rrect(755, 830, 95, 190, 30, 83), OLIVE) + path(rrect(205, 960, 630, 85, 20, 84), OLIVE) +
               path(rrect(230, 1040, 26, 38, 6, 85), INK) + path(rrect(785, 1040, 26, 38, 6, 86), INK))
meter = (f'<text x="137" y="614" font-family="Inter" font-weight="900" font-size="36" text-anchor="middle" letter-spacing="2" fill="{INK}">PAIN</text>' +
         path(rrect(110, 632, 54, 368, 26, 87), PAPER) +
         "".join(path(wline([(166, y), (186, y)], 88 + y, 1), sw=5) for y in range(680, 990, 60)) +
         f'<rect id="s5-pain-fill" x="124" y="642" width="26" height="360" rx="12" fill="{TERRA}"/>' +
         f'<circle id="s5-pain-bulb" cx="137" cy="1020" r="36" fill="{TERRA}" stroke="{INK}" stroke-width="7"/>')

# ---------------- characters (placeholders; Step B: Rig.mount into the static wrappers) ----------------
alex = f'''<g id="s5-alex-mv"><!-- CHAR:alex -->
<g id="s5-alex" transform="translate(470 931) scale(1.15)"></g>
<!-- /CHAR:alex --></g>'''
phone = '<g transform="translate(470 805)">' + g("s5-phone", path(rrect(-28, -50, 56, 100, 10, 90), INK) + f'<rect x="-20" y="-40" width="40" height="76" rx="5" fill="{SKY}"/>') + '</g>'
phone_glow = ""
marcus = f'''<g clip-path="url(#s5-behind-couch)"><g id="s5-marcus-mv"><!-- CHAR:marcus -->
<g id="s5-marcus" transform="translate(735 1080) scale(1.1)"></g>
<!-- /CHAR:marcus -->
</g></g>'''

# ---------------- props / beats ----------------
rule = g("s5-rule-in", path(blob([(230, 290), (850, 270), (862, 500), (240, 515)], 100, 5), PAPER) +
         f'<text x="545" y="455" font-family="Playfair Display" font-weight="900" font-size="168" text-anchor="middle" fill="{INK}">RULE <tspan fill="{GOLD}" stroke="{INK}" stroke-width="7" paint-order="stroke">2</tspan></text>' +
         f'<path id="s5-rule-ul" d="{wline([(320, 485), (560, 478), (770, 470)], 101, 3)}" fill="none" stroke="{TERRA}" stroke-width="16" stroke-linecap="round" pathLength="1" stroke-dasharray="1 1.2" stroke-dashoffset="1.1"/>',
         attrs="")
ding = g("s5-ding-in", path(rrect(-46, -36, 92, 72, 22, 110), GOLD) + path("M-10 34 L-22 58 L10 36", GOLD, 6) +
         "".join(f'<circle cx="{x}" cy="0" r="8" fill="{INK}"/>' for x in (-22, 0, 22)))
boink = g("s5-boink-in", "".join(path(wline([(470 + 40 * __import__('math').cos(a), 520 + 40 * __import__('math').sin(a)), (470 + 70 * __import__('math').cos(a), 520 + 70 * __import__('math').sin(a))], 111, 0), sw=6) for a in (-2.6, -2.0, -1.2, -0.5)))
puffs = (g("s5-puff1", path(ellipse(420, 440, 12, 11, 8, 120, 1), PAPER, 5)) + g("s5-puff2", path(ellipse(380, 402, 18, 16, 8, 121, 1), PAPER, 6)) +
         g("s5-cloud-small", path(cloud(290, 320, 85, 62, 9, 0.6, 122), PAPER) + path(wline([(245, 320), (265, 300), (285, 335), (308, 300), (330, 325)], 123, 2), sw=6, stroke=TERRA)))
chat = (path(rrect(570, 268, 410, 392, 26, 130), PAPER) + path("M640 655 L540 790 L700 655", PAPER, 7) +
        f'<rect x="580" y="655" width="140" height="10" fill="{PAPER}"/>' +
        path(wline([(575, 362), (975, 362)], 131, 1), sw=5) +
        f'<circle cx="622" cy="316" r="26" fill="{TERRA}" stroke="{INK}" stroke-width="6"/>' +
        f'<text x="664" y="330" font-family="Inter" font-weight="900" font-size="38" fill="{INK}">Sam</text>' +
        path(rrect(612, 395, 348, 135, 26, 132), GOLD) +
        f'<text x="634" y="450" font-family="Inter" font-weight="700" font-size="36" fill="{INK}">are we still on</text>' +
        f'<text x="634" y="500" font-family="Inter" font-weight="700" font-size="36" fill="{INK}">for tonight?</text>' +
        g("s5-read-in", path("M760 590 l10 12 l20 -24 M784 590 l10 12 l20 -24", sw=5, stroke=SKY) +
          f'<text x="956" y="604" font-family="Inter" font-weight="700" font-size="36" text-anchor="end" fill="{INK}" fill-opacity=".75">Read 9:41 PM</text>'))
event_tag = g("s5-event-in", path(rrect(625, 958, 360, 84, 14, 140), PAPER) +
              f'<text x="648" y="1012" font-family="Inter" font-weight="900" font-size="34" letter-spacing="2" fill="{INK}">EVENT:</text>' +
              f'<text id="s5-noreply" x="790" y="1014" font-family="Playfair Display" font-style="italic" font-weight="700" font-size="46" fill="{INK}">no reply</text>')
import math
rain = "".join(f'<path d="M{x} {y} l-8 26" stroke="{SKY}" stroke-width="5" stroke-linecap="round"/>' for x in range(700, 860, 26) for y in (360, 420, 480))
story_inner = (
    # friends laughing (left)
    "".join(path(ellipse(x, 400, 34, 36, 10, 150 + i, 2), SKIN if i == 1 else INK, 6) +
            path(blob([(x - 40, 440), (x + 40, 440), (x + 46, 520), (x - 46, 520)], 160 + i, 3), TERRA if i == 1 else INK, 6) +
            path(f"M{x-14} 408 Q{x} 428 {x+14} 408Z", INK if i == 1 else PAPER, 3)
            for i, x in enumerate([215, 320, 425])) +
    g("s5-haha", f'<text x="320" y="330" font-family="Playfair Display" font-style="italic" font-weight="900" font-size="58" text-anchor="middle" fill="{TERRA}" transform="rotate(-6 320 330)">HA HA HA</text>') +
    path(wline([(560, 250), (548, 360), (566, 440), (552, 540)], 170, 4), sw=6) +
    # lonely Alex in the rain (right)
    g("s5-rain", rain) +
    path(cloud(770, 318, 90, 34, 7, 0.6, 171), "#55707F", 6) +
    path(ellipse(770, 430, 32, 34, 10, 172, 2), SKIN, 6) + path(blob([(730, 466), (810, 466), (816, 530), (724, 530)], 173, 3), GOLD, 6) +
    path("M756 448 Q770 438 784 448", sw=5) + path("M752 420 l8 4 M788 420 l-8 4", sw=4)
)
story = g("s5-story-in", path(cloud(540, 365, 450, 150, 13, 0.55, 180), PAPER, 8) +
          f'<g clip-path="url(#s5-story-clip)"><g transform="translate(0 -22)">{story_inner}</g></g>')
story_tag = g("s5-storytag-in", path(rrect(578, 560, 410, 92, 14, 190), TERRA) +
              f'<text x="596" y="618" font-family="Inter" font-weight="900" font-size="32" letter-spacing="2" fill="{PAPER}">STORY:</text>' +
              "".join(f'<text id="s5-hate-{i}" x="{x}" y="622" font-family="Playfair Display" font-style="italic" font-weight="900" font-size="40" fill="{PAPER}">{w}</text>'
                      for i, (x, w) in enumerate([(738, "they"), (822, "hate"), (915, "me")])))
# note: "me" ends at ~990 ; tag shakes
pop = g("s5-pop-in", path(burst(775, 470, 60, 130, 10, 200), GOLD, 7) +
        f'<text x="775" y="500" font-family="Playfair Display" font-weight="900" font-size="88" text-anchor="middle" fill="{INK}">POP!</text>')
shards = "".join(g(f"s5-shard{i}", path(ellipse(540 + 300 * math.cos(a) * 0.15, 385 + 120 * math.sin(a) * 0.15, 22, 14, 8, 210 + i, 3), PAPER, 6))
                 for i, a in enumerate([k * math.pi / 4 + 0.3 for k in range(8)]))
truth = g("s5-truth-in", path(ellipse(395, 455, 12, 11, 8, 220, 1), PAPER, 5) + '<g transform="translate(0 -40)">' +
          path(cloud(330, 370, 240, 125, 11, 0.55, 221), PAPER, 7) +
          path(rrect(170, 400, 300, 70, 14, 222), "#55707F", 6) + path(rrect(175, 380, 80, 40, 14, 223), PAPER, 6) +
          path(ellipse(225, 375, 34, 32, 10, 224, 2), SKIN, 6) + path("M208 376 q8 6 16 0 M232 376 q8 6 16 0", sw=4) +
          path(blob([(250, 390), (470, 392), (466, 440), (250, 440)], 225, 3), TERRA, 6) +
          path(rrect(480, 420, 70, 60, 8, 226), GOLD, 6) + path(rrect(492, 408, 46, 14, 4, 227), INK, 3) +
          g("s5-zzz", "".join(f'<text x="{x}" y="{y}" font-family="Playfair Display" font-style="italic" font-weight="900" font-size="{s}" fill="{INK}">z</text>'
                              for x, y, s in [(290, 340, 40), (325, 310, 50), (368, 275, 60)])) + '</g>')
exhale = '<g transform="translate(420 600)">' + g("s5-exhale-in", path(cloud(0, 0, 44, 26, 7, 0.6, 230), PAPER, 6)) + '</g>'
sweat = g("s5-sweat-in", path("M575 500 Q595 530 585 545 Q570 555 562 540 Q560 525 575 500Z", SKY, 5))

wipe_d = "M0 -100 H1300 L1240 200 L1330 520 L1250 840 L1320 1180 L1240 1500 L1310 1820 L1260 2050 H0Z"
wipe_in = f'<path id="s5-wipe-in-p" d="{wipe_d}" fill="{INK}"/>'
wipe_out = f'<path id="s5-wipe-out-p" d="{wipe_d}" fill="{INK}" transform="scale(-1 1) translate(-1080 0)"/>'

svg = f'''<svg id="s5-stage" viewBox="0 0 1080 1920" width="1080" height="1920" style="position:absolute;inset:0;overflow:hidden">
  <defs>
    <filter id="s5-ink" class="ink-boil" x="-15%" y="-15%" width="130%" height="130%" color-interpolation-filters="sRGB">
      <feTurbulence class="ink-turb" type="fractalNoise" baseFrequency="0.035" numOctaves="2" seed="1" result="n"/>
      <feDisplacementMap in="SourceGraphic" in2="n" scale="5" xChannelSelector="R" yChannelSelector="G"/>
    </filter>
    <filter id="s5-whipblur" x="-20%" y="-5%" width="140%" height="110%"><feGaussianBlur id="s5-whipblur-b" stdDeviation="0 0"/></filter>
    <clipPath id="s5-behind-couch"><rect x="-300" y="-300" width="1680" height="1095"/></clipPath>
    <clipPath id="s5-story-clip"><path d="{cloud(540, 365, 438, 140, 13, 0.55, 180)}"/></clipPath>
  </defs>
  <g id="s5-whip" filter="url(#s5-whipblur)">
  <g id="s5-shake"><g id="s5-cam">
    <g id="s5-bg" class="ink">{wall}{stripes}{floor}{planks}{base}{window}{frame}{plant}</g>
    <g class="ink">{meter}</g>
    {clip("s5-marcus-clip", 8.9, round(D - 8.9, 2), marcus)}
    <g class="ink">{couch_back}</g>
    {phone_glow}
    {alex}
    <g class="ink">{couch_front}</g>
    
    <g class="ink">
      {clip("s5-sweat", 5.6, 1.9, sweat)}
      {clip("s5-event", 6.2, round(D - 6.2, 2), event_tag)}
      {clip("s5-puffs", 2.4, 5.4, puffs)}
      {clip("s5-chat", 4.18, 3.35, g("s5-chat-in", chat))}
      {clip("s5-story", 7.57, 2.0, story)}
      {clip("s5-storytag", 7.57, 1.9, story_tag)}
      {clip("s5-shards", 9.47, 0.6, shards)}
      {clip("s5-truth", 9.66, round(D - 9.66, 2), truth)}
      {clip("s5-pop", 9.47, 0.7, pop)}
      {clip("s5-exhale", 11.17, 1.2, exhale)}
      {clip("s5-boink", 1.31, 0.5, boink)}
      {clip("s5-ding", 0.9, 1.3, '<g transform="translate(470 300)">' + g("s5-ding-mv", ding) + '</g>')}
    </g>
  </g></g>
  <g class="ink" transform="translate(0 -75)">{clip("s5-rule", 0.1, 2.3, rule)}</g>
  </g>
  {clip("s5-wipe-in", 0, 0.32, wipe_in)}
  {clip("s5-wipe-out", 12.2, 0.31, wipe_out)}
</svg>'''

script = r'''
  (function () {
    const D = 12.51;
    const tl = gsap.timeline({ paused: true });
    const seen = new Set();
    // fromTo helper: first tween per target+prop renders immediately, later ones don't (seek-safe chains)
    function F(sel, from, to, at) {
      const keys = Object.keys(from).filter(k => k !== "svgOrigin" && k !== "transformOrigin");
      const fresh = keys.every(k => !seen.has(sel + "|" + k));
      keys.forEach(k => seen.add(sel + "|" + k));
      tl.fromTo(sel, from, Object.assign({ immediateRender: fresh }, to), at);
    }
    // deterministic keyed shake on #s5-shake
    function shake(t0, amps) {
      amps.concat([[0, 0]]).forEach((a, i) => F("#s5-shake", { x: i ? amps[i - 1][0] : 0, y: i ? amps[i - 1][1] : 0 }, { x: a[0], y: a[1], duration: 1 / 30, ease: "none" }, t0 + i / 30));
    }

    // ---- boil: real rig when present, local 12 fps seed cycle otherwise ----
    const stage = document.querySelector("#s5-stage");
    if (window.Rig && !Rig.__stub) {
      Rig.boil(tl, stage, 0, D);
    } else {
      stage.querySelectorAll(".ink").forEach(el => el.setAttribute("filter", "url(#s5-ink)"));
      for (let i = 0; i < Math.ceil(D * 12); i++) tl.set("#s5-ink .ink-turb", { attr: { seed: [1, 4, 9][i % 3] } }, i / 12);
    }

    // ---- transition in: ink wipe leaves left + whip ----
    F("#s5-wipe-in-p", { x: 0 }, { x: -1400, duration: 0.3, ease: "power2.in" }, 0);
    F("#s5-cam", { x: 160, scale: 1, svgOrigin: "540 800" }, { x: 0, scale: 1.0, duration: 0.42, ease: "power3.out" }, 0);
    F("#s5-whipblur-b", { attr: { stdDeviation: "18 0" } }, { attr: { stdDeviation: "0 0" }, duration: 0.3, ease: "power2.out" }, 0);

    // ---- RULE 2 stamp ----
    F("#s5-rule-in", { opacity: 0, scale: 1.5, rotation: -9, svgOrigin: "545 390" }, { opacity: 1, scale: 1, rotation: -4, duration: 0.32, ease: "back.out(2.2)" }, 0.12);
    F("#s5-rule-ul", { attr: { "stroke-dashoffset": 1.1 } }, { attr: { "stroke-dashoffset": 0 }, duration: 0.3, ease: "power2.out" }, 0.42);
    F("#s5-rule-in", { opacity: 1, y: 0 }, { opacity: 0, y: -40, duration: 0.24, ease: "power2.in" }, 2.08);

    // ---- camera: slow push, then to the phone, back for the bubble ----
    F("#s5-cam", { scale: 1.0 }, { scale: 1.04, duration: 3.6, ease: "sine.inOut" }, 0.42);
    F("#s5-cam", { x: 0, y: 0, scale: 1.04 }, { x: -40, y: 30, scale: 1.08, duration: 0.5, ease: "power2.inOut" }, 4.1);
    F("#s5-cam", { x: -40, y: 30, scale: 1.08 }, { x: 0, y: 0, scale: 1.0, duration: 0.4, ease: "power2.inOut" }, 7.3);
    F("#s5-cam", { scale: 1.0 }, { scale: 1.05, duration: 0.3, ease: "power3.out" }, 8.35);
    F("#s5-cam", { scale: 1.05 }, { scale: 1.02, duration: 2.2, ease: "power2.inOut" }, 9.7);

    // ---- ambient: phone glow flicker (keyed), Alex breath ----
    // (phone glow removed)

    // ---- "events don't hurt you": a notification bonks him, harmless ----
    F("#s5-ding-in", { scale: 0, svgOrigin: "0 0" }, { scale: 1, duration: 0.25, ease: "back.out(3)" }, 0.9);
    F("#s5-ding-mv", { x: 0, y: 0 }, { x: 0, y: 225, duration: 0.2, ease: "power2.in" }, 1.13);
    F("#s5-ding-mv", { x: 0, y: 225, rotation: 0 }, { x: 260, y: -40, rotation: 40, duration: 0.55, ease: "power2.out" }, 1.33);
    F("#s5-ding-in", { opacity: 1 }, { opacity: 0, duration: 0.25 }, 1.9);
    F("#s5-boink-in", { scale: 0.4, opacity: 1, svgOrigin: "470 520" }, { scale: 1.2, opacity: 0, duration: 0.45, ease: "power2.out" }, 1.33);

    // ---- "your story about them does": thought puffs + pain rises ----
    F("#s5-puff1", { scale: 0, svgOrigin: "420 440" }, { scale: 1, duration: 0.2, ease: "back.out(3)" }, 2.4);
    F("#s5-puff2", { scale: 0, svgOrigin: "380 402" }, { scale: 1, duration: 0.2, ease: "back.out(3)" }, 2.52);
    F("#s5-cloud-small", { scale: 0, svgOrigin: "290 320" }, { scale: 1, duration: 0.3, ease: "back.out(2.5)" }, 2.66);
    F("#s5-pain-fill", { scaleY: 0.06, svgOrigin: "137 1002" }, { scaleY: 0.32, duration: 0.35, ease: "back.out(2)" }, 3.36);

    // ---- "your friend leaves you on read": chat panel pops out of the phone ----
    F("#s5-chat-in", { scale: 0.08, opacity: 0, svgOrigin: "540 790" }, { scale: 1, opacity: 1, duration: 0.35, ease: "back.out(1.8)" }, 4.18);
    F("#s5-read-in", { opacity: 0, x: 20 }, { opacity: 1, x: 0, duration: 0.18, ease: "power3.out" }, 5.37);
    F("#s5-sweat-in", { scale: 0, svgOrigin: "575 540" }, { scale: 1, duration: 0.2, ease: "back.out(3)" }, 5.6);
    F("#s5-sweat-in", { y: 0 }, { y: 40, duration: 1.6, ease: "power1.in" }, 5.8);

    // ---- "the event: no reply" plain tag ----
    F("#s5-event-in", { scale: 1.4, opacity: 0, svgOrigin: "805 1000" }, { scale: 1, opacity: 1, duration: 0.25, ease: "back.out(2)" }, 6.2);
    F("#s5-noreply", { opacity: 0 }, { opacity: 1, duration: 0.15 }, 6.64);
    F("#s5-chat-in", { scale: 1, opacity: 1 }, { scale: 0.08, opacity: 0, duration: 0.24, ease: "power3.in" }, 7.31);

    // ---- "the story: they hate me": the bubble balloons into a melodrama ----
    F("#s5-cloud-small", { scale: 1 }, { scale: 2.2, opacity: 0, duration: 0.22, ease: "power2.in" }, 7.57);
    F("#s5-story-in", { scale: 0.18, svgOrigin: "290 320" }, { scale: 1, duration: 0.45, ease: "elastic.out(1, 0.55)" }, 7.57);
    F("#s5-haha", { scale: 0.5, opacity: 0, svgOrigin: "320 320" }, { scale: 1, opacity: 1, duration: 0.25, ease: "back.out(3)" }, 7.85);
    [0, 1, 2, 3, 4, 5].forEach(i => F("#s5-haha", { y: i % 2 ? -8 : 0 }, { y: i % 2 ? 0 : -8, duration: 0.16, ease: "sine.inOut" }, 8.1 + i * 0.16));
    F("#s5-rain", { y: 0 }, { y: 60, duration: 0.25, ease: "none", repeat: 7 }, 7.57);
    F("#s5-pain-fill", { scaleY: 0.32 }, { scaleY: 0.6, duration: 0.3, ease: "back.out(2)" }, 7.62);
    F("#s5-storytag-in", { x: 420 }, { x: 0, duration: 0.3, ease: "power4.out" }, 7.57);
    [["#s5-hate-0", 8.05], ["#s5-hate-1", 8.35], ["#s5-hate-2", 8.65]].forEach(([s, t]) => F(s, { opacity: 0, scale: 1.6, svgOrigin: "880 610" }, { opacity: 1, scale: 1, duration: 0.18, ease: "back.out(3)" }, t));
    F("#s5-pain-fill", { scaleY: 0.6 }, { scaleY: 0.92, duration: 0.3, ease: "back.out(2.5)" }, 8.35);
    shake(8.35, [[7, -5], [-6, 4], [5, 6], [-4, -3], [3, 2]]);
    [[6, -2], [-5, 3], [4, 1], [-6, -2], [5, 2], [-3, -1], [0, 0]].forEach((a, i, arr) => F("#s5-storytag-in", { rotation: i ? arr[i - 1][0] * .5 : 0, svgOrigin: "785 606" }, { rotation: a[0] * .5, duration: 1 / 15, ease: "none" }, 8.4 + i / 15));

    // ---- "drop the story": tag drops, Marcus pops up from behind the couch, pins the bubble ----
    F("#s5-storytag-in", { y: 0, rotation: 0 }, { y: 900, rotation: 28, duration: 0.5, ease: "power2.in" }, 8.95);
    F("#s5-story-in", { scale: 1 }, { scale: 1.06, duration: 0.05, ease: "power2.out" }, 9.42);
    F("#s5-story-in", { opacity: 1 }, { opacity: 0, duration: 0.05, ease: "none" }, 9.47);
    for (let i = 0; i < 8; i++) {
      const a = i * Math.PI / 4 + 0.3;
      F("#s5-shard" + i, { x: 0, y: 0, opacity: 1 }, { x: Math.cos(a) * 520, y: Math.sin(a) * 260, opacity: 0, duration: 0.55, ease: "power2.out" }, 9.47);
    }
    F("#s5-pop-in", { scale: 0.3, rotation: -10, svgOrigin: "775 470" }, { scale: 1, rotation: 6, duration: 0.2, ease: "back.out(3)" }, 9.47);
    F("#s5-pop-in", { opacity: 1 }, { opacity: 0, duration: 0.2, ease: "power2.in" }, 9.95);
    shake(9.47, [[-8, 6], [7, -5], [-5, 4], [4, -2]]);

    // ---- the plain fact: friend asleep ----
    F("#s5-truth-in", { scale: 0.6, opacity: 0, svgOrigin: "395 455" }, { scale: 1, opacity: 1, duration: 0.4, ease: "back.out(1.6)" }, 9.66);
    [0, 1, 2, 3, 4, 5].forEach(i => F("#s5-zzz", { y: i % 2 ? -10 : 0 }, { y: i % 2 ? 0 : -10, duration: 0.45, ease: "sine.inOut" }, 9.9 + i * 0.45));

    // ---- "most of the pain goes with it": meter drains, Alex exhales ----
    F("#s5-pain-fill", { scaleY: 0.92 }, { scaleY: 0.15, duration: 1.5, ease: "power2.inOut" }, 10.31);
    F("#s5-pain-fill", { fill: "#C65A3A" }, { fill: "#7A8450", duration: 1.5, ease: "power1.inOut" }, 10.31);
    F("#s5-pain-bulb", { fill: "#C65A3A" }, { fill: "#7A8450", duration: 1.5, ease: "power1.inOut" }, 10.31);
    F("#s5-alex-mv", { y: 0 }, { y: 10, duration: 0.5, ease: "power2.out" }, 11.17);
    F("#s5-exhale-in", { x: 0, scale: 0.3, opacity: 1, svgOrigin: "0 0" }, { x: -140, scale: 1.3, opacity: 0, duration: 1.1, ease: "power2.out" }, 11.17);


    // ================= RIG acting (Step B) =================
    if (window.Rig && !Rig.__stub) {
      const alex = Rig.mount(document.querySelector("#s5-alex"), "alex");
      const marcus = Rig.mount(document.querySelector("#s5-marcus"), "marcus", { flip: true });
      // Marcus's pin: static drawing inside his hand (follows the arm)
      const mh = Rig.get(marcus, ".hand-r");
      if (mh && !mh.querySelector(".s5-pin")) mh.insertAdjacentHTML("beforeend", '<g class="s5-pin"><path d="M70 -168 L70 -40" stroke="#1E1A16" stroke-width="5" stroke-linecap="round"/><circle cx="70" cy="-176" r="12" fill="#E0A84A" stroke="#1E1A16" stroke-width="5"/></g>');
      Rig.sit(tl, alex, 0, { dur: 0.05 });
      Rig.idle(tl, alex, 0.3, D, { seed: 5 });
      Rig.emote(tl, alex, [[0, "calm"], [1.36, "neutral"], [3.36, "sad"], [5.42, "shocked"], [6.3, "sad"], [8.05, "scared"], [9.5, "shocked"], [10.35, "calm"], [11.5, "happy"]]);
      Rig.show(tl, alex, ".phone", 0, true, 0.01);
      Rig.gesture(tl, alex, "hold", 0, { hold: 11.0 });
      Rig.look(tl, alex, 0.3, 0, 0.6);
      Rig.look(tl, alex, 1.1, 0, -1, 0.1);
      Rig.look(tl, alex, 1.6, 0, 0.6);
      Rig.look(tl, alex, 2.5, -0.7, -0.8);
      Rig.look(tl, alex, 3.9, 0.3, 0.8);
      Rig.look(tl, alex, 7.6, -0.4, -1);
      Rig.look(tl, alex, 9.3, 1, -0.4);
      Rig.look(tl, alex, 9.8, -0.7, -0.9);
      Rig.look(tl, alex, 11.2, 0, 0);
      Rig.squash(tl, alex, 1.33, { amt: 0.06 });
      Rig.tremble(tl, alex, 8.35, 9.4, { amp: 3 });
      Rig.tilt(tl, alex, 5.5, 5);
      Rig.tilt(tl, alex, 8.4, -4);
      Rig.tilt(tl, alex, 11.17, -8, 0.5);
      Rig.mouth(tl, alex, 11.17, "o");
      Rig.mouth(tl, alex, 11.75, "smile");
      // Marcus pops up from behind the couch on "drop"
      F("#s5-marcus-mv", { y: 380 }, { y: 0, duration: 0.3, ease: "back.out(1.6)" }, 8.95);
      Rig.idle(tl, marcus, 8.95, D, { seed: 2 });
      Rig.emote(tl, marcus, [[8.95, "smug"], [10.0, "happy"]]);
      Rig.look(tl, marcus, 9.05, 0.3, -1);
      Rig.reach(tl, marcus, "r", 9.1, [80, -440], { hand: "fist", dur: 0.2 });
      Rig.reach(tl, marcus, "r", 9.38, [60, -500], { hand: "fist", dur: 0.09, ease: "power3.in" });
      Rig.rest(tl, marcus, "r", 10.0, { dur: 0.4 });
      Rig.look(tl, marcus, 10.0, -1, 0.2);
      Rig.tilt(tl, marcus, 10.4, 6);
    }

    // ---- transition out: ink wipe from the right + whip ----
    F("#s5-wipe-out-p", { x: 1400 }, { x: 0, duration: 0.27, ease: "power2.in" }, 12.2);
    F("#s5-cam", { x: 0 }, { x: -160, duration: 0.3, ease: "power3.in" }, 12.2);
    F("#s5-whipblur-b", { attr: { stdDeviation: "0 0" } }, { attr: { stdDeviation: "18 0" }, duration: 0.28, ease: "power2.in" }, 12.2);

    window.__timelines["s5_story"] = tl;
  })();
'''

html = f'''<template>
  <style>
    #root {{ position: absolute; inset: 0; }}
    #s5-world {{ position: absolute; inset: 0; }}
  </style>
  <div id="root" data-composition-id="s5_story" data-width="1080" data-height="1920">
    <div id="s5-world" class="clip" data-start="0" data-duration="{D}">
{svg}
    </div>
  </div>
  <script>{script}</script>
</template>
'''
open(os.path.join(ROOT, "compositions/s5_story.html"), "w").write(html)
print("wrote s5_story.html", len(html))
