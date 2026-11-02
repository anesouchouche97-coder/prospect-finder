# RIG_API: characters, props, boiling ink (contract for animators)

Owner: Character Designer. Code against this file now; the art behind it keeps improving without API changes.
Files: `assets/rig.js` (global `window.Rig`, loaded by index.html after GSAP), `characters/defs.svg`, `characters/{marcus,epictetus,seneca,alex}.svg`, `characters/props.svg`.

## 1. Coordinate system (same for all four characters)

- Every character is drawn in **character-local px with the anchor = feet baseline center at (0,0)**; up is negative y.
- You place a character with a STATIC wrapper `<g id="<scene>-<name>" transform="translate(X Y) scale(S)">` in your scene `<svg viewBox="0 0 1080 1920">`. (X,Y) is where the feet touch the ground. **Never tween that wrapper** if Rig drives the character (Rig tweens the inner `.char`); if you need camera/extra moves, wrap it in your own `<g id>` and tween that.
- `-l` / `-r` = **screen-left / screen-right** in the unflipped drawing (character faces the viewer, 3/4-front).
- Rotations are degrees, SVG convention: positive = clockwise on screen.

| Character | `viewBox` of the .svg file | natural height at scale 1 (feet → top) | width (approx) | notes |
|---|---|---|---|---|
| marcus | `-170 -580 340 600` | 545 (top of laurel) | 240 | laurel, beard, purple-trim toga |
| epictetus | `-170 -580 340 600` | 520 | 300 incl. crutch (crutch foot at x=+105) | slight stoop, crutch on screen-right |
| seneca | `-170 -580 340 600` | 505 | 280 (round) | bald, chubby, gold-trim toga / rough tunic |
| alex | `-170 -580 340 600` | 530 (top of hair) | 230 | hoodie, jeans, sneakers, phone |

Faces sit at local y ≈ -500…-370 (eyes y = -450, mouth y = -400). At scale 1 with feet at Y=1080 the face is at screen y ≈ 630–710. Good scales: hero close-up 1.4–1.8, two-shot 1.0–1.2, background 0.5–0.7.

## 2. Skeleton / pivots (character-local px, identical for all four)

| Part (class) | Pivot (svgOrigin) | Rig owns these props | Nesting |
|---|---|---|---|
| `.char` | (0,0) | `x` (walk/move), `scaleX` (flip, static) | root |
| `.shadow` | (0,0) | `scaleX/scaleY` (hop) | child of `.char`, sibling of `.body` |
| `.body` | (0,0) feet | `y` (bob/hop), `scaleX/scaleY` (squash), `rotation` (lean) | child of `.char`; has class `ink` |
| `.leg-l` / `.leg-r` | (-26,-150) / (26,-150) hips | `rotation` | in `.body` |
| `.torso` | (0,-150) hips | `scaleY/scaleX` (breathe), `rotation` | in `.body` |
| `.arm-l` / `.arm-r` | (-60,-330) / (60,-330) shoulders | `rotation`, `y` (shrug) | in `.torso` |
| `.forearm-l` / `.forearm-r` | (-66,-250) / (66,-250) elbows | `rotation` | in `.arm-*` |
| `.hand-l` / `.hand-r` | (-70,-175) / (70,-175) wrists | `rotation`, scale | in `.forearm-*`; contains `.hand-open`, `.hand-fist`, `.hand-point` (one visible) |
| `.head` | (0,-350) neck | `rotation` (tilt), `y` (breathe lag) | in `.body` (not in torso) |
| `.face` | — | — | in `.head` |
| `.eye-l` / `.eye-r` | (-30,-450) / (30,-450) | `scaleY` (squint/wide) | in `.face` |
| `.pupil-l` / `.pupil-r` | eye centers | `x`,`y` (look), `scale` | in `.eye-*` |
| `.lid-l` / `.lid-r` | top of eye (±30,-472) | `scaleY` 0 open → 1 closed (blink only) | in `.face`, over the eye |
| `.brow-l` / `.brow-r` | (-30,-488) / (30,-488) | `rotation`, `y` | in `.face` |
| `.mouth-rest .mouth-open .mouth-wide .mouth-o .mouth-smile .mouth-frown` | (0,-400) | `opacity` (exactly one = 1) | in `.face` |

Upper arm 80 px, forearm 75 px, hand ~28 px (wrist to fingertips). Shoulder height -330, hips -150.

Extras (all class-named, no ids):
- Marcus: `.laurel` (in `.head`), `.beard` (in `.head`, pivot (0,-395), Rig jiggles it with `talk`).
- Epictetus: `.beard` (in `.head`), `.crutch` (in `.body`, pivot = crutch foot (105,0); held under screen-right arm). His gestures default to the LEFT arm.
- Seneca: `.toga` (visible) and `.rough-tunic` (opacity 0) inside `.torso`; swap with `Rig.costume`.
- Alex: `.hoodie` (in `.torso`), `.phone` (in `.hand-r`, opacity 0 by default; show with `Rig.show`).

## 3. Scene setup (copy this)

```html
<!-- inside your scene's #root, in a .clip wrapper div -->
<svg id="s4-stage" viewBox="0 0 1080 1920" width="1080" height="1920" style="position:absolute;inset:0;overflow:visible">
  <defs>
    <!-- paste characters/defs.svg's <filter> with PFX replaced by your scene prefix (here s4) -->
    <filter id="s4-ink" class="ink-boil" x="-15%" y="-15%" width="130%" height="130%" color-interpolation-filters="sRGB">
      <feTurbulence class="ink-turb" type="fractalNoise" baseFrequency="0.035" numOctaves="2" seed="1" result="n"/>
      <feDisplacementMap in="SourceGraphic" in2="n" scale="5" xChannelSelector="R" yChannelSelector="G"/>
    </filter>
  </defs>
  <g id="s4-cam">                                   <!-- your camera group (tween this) -->
    <g class="ink"> …your environment art… </g>    <!-- class ink = boils with the characters -->
    <g id="s4-alex" transform="translate(540 1060) scale(1.3)"></g>   <!-- empty: Rig.mount fills it -->
    <g id="s4-epi"  transform="translate(780 1040) scale(1.0)"></g>
  </g>
</svg>
<script>
  const tl = gsap.timeline({ paused: true });
  const alex = Rig.mount(document.querySelector("#s4-alex"), "alex");          // returns the .char element
  const epi  = Rig.mount(document.querySelector("#s4-epi"), "epictetus", { flip: true });
  Rig.boil(tl, document.querySelector("#s4-stage"), 0, 12.79);   // whole scene, 12 fps
  Rig.idle(tl, alex, 0, 12.79, { seed: 4 });                     // breathe + blinks every 2-4 s
  Rig.emote(tl, alex, [[0, "neutral"], [1.2, "angry"], [6.8, "calm"]]);
  Rig.talk(tl, alex, words.slice(0, 5));                          // words = scenes.json words[] (scene-local)
  Rig.gesture(tl, alex, "fist", 3.1);
  Rig.walk(tl, epi, 0.2, 1.4, -180);
  window.__timelines["s4_traffic"] = tl;
</script>
```

- `Rig.mount(target, name, opts)` injects the character markup synchronously (single source of truth = rig.js, so art fixes reach every scene). `name`: `"marcus" | "epictetus" | "seneca" | "alex"`. `opts.flip:true` mirrors it (faces the other way; `-l/-r` then refer to the mirrored drawing). Returns the `.char` element. Fallback if you want static markup: paste the `<g class="char …">` from `characters/<name>.svg` into the wrapper; every helper works the same.
- `Rig.prop(target, name)` injects a prop the same way (see §6). Returns the prop root `<g>`.
- Every `charSel` argument below accepts the `.char` element, its wrapper element, or a unique selector string (`"#s4-alex"`). Pass elements from your scoped `document.querySelector` when in doubt.
- **Call order per character = chronological, and `emote` before `talk`/`gesture`** (talk returns to the mood's resting mouth; walk accumulates x).

## 4. Helpers (all only add `set`/`fromTo` to `tl` at explicit times; deterministic and seekable; all return `tl`)

| Signature | Behavior |
|---|---|
| `Rig.boil(tl, scope, t0, dur, {fps=12, scale=5})` | Links every `.ink` inside `scope` to scope's `.ink-boil` filter (static `filter` attribute) and steps its `feTurbulence` `seed` through a 3-drawing cycle every 1/fps s from t0 to t0+dur (`tl.set(turb,{attr:{seed}},t)`). Call once per scene over the full duration. |
| `Rig.blink(tl, c, times[])` | Each time: both lids close 0.06 s, hold 0.04, open 0.08 (right lid lags 0.015 s). |
| `Rig.idle(tl, c, t0, t1, {seed=1, blink=true, breathe=true})` | `breathe` + seeded blinks every 2–4 s. The cheap way to keep anyone alive. |
| `Rig.breathe(tl, c, t0, t1, {period=2.6, amt=0.018})` | Torso scaleY 1↔1+amt (sine), head y 0↔-3 lagging 0.18 s. |
| `Rig.talk(tl, c, words[], offset=0)` | `words` = `[{text,start,end}]` scene-local (straight from scenes.json). Mouth shapes per word from its letters (a → wide, o/u/w → o, e/i/y → open, m/b/p start → closed), ~0.09–0.13 s each, beard/head nod lightly on stressed words; returns to the current mood's resting mouth in gaps ≥ 0.15 s and after the last word. Times are `start+offset`. |
| `Rig.emote(tl, c, keys)` | `keys = [[t,"neutral"\|"happy"\|"angry"\|"sad"\|"shocked"\|"smug"\|"calm"], …]`. Each change is a take: 0.08 s squash anticipation on `.body` (shocked: squash then stretch), brows lead (t+0.02), eyes/pupils (t+0.05), mouth (t+0.08), head tilt (t+0.06, 0.3 s), body settles with overshoot by t+0.45. First key snaps (no take). Hold reactions ≥ 0.6 s. |
| `Rig.mouth(tl, c, t, shape)` | Raw switch: `"rest"\|"open"\|"wide"\|"o"\|"smile"\|"frown"`. |
| `Rig.look(tl, c, t, dx, dy=0, dur=0.15)` | Pupils to dx,dy in -1…1 (1 = 9 px), both eyes, right eye lags 0.02 s. Look at what matters. |
| `Rig.gesture(tl, c, name, t, {side, hold=0.8})` | Arm action that starts at `t`, holds `hold` s, returns to rest. Total ≈ 0.3 in + hold + 0.35 out (wave/write add their cycles inside the hold). `side` `"r"` (default; Epictetus `"l"`) or `"l"`; `shrug` uses both. Names: `wave`, `point` (arm out to the side, finger), `shrug` (both palms up + head tilt), `facepalm` (hand to face, head drops), `think` (hand to chin, eyes up), `present` (open palm out at chest height), `fist` (raised shaking fist), `write` (hand in front of chest scribbling; pair with a scroll prop), `hold` (forearm up, hand at chest: holding a phone/cup), `sip` (hand to mouth and back), `push` (both arms forward-out, body leans 8°). |
| `Rig.reach(tl, c, side, t, [x,y], {dur=0.3, ease="power2.out", hand="open"})` | 2-bone IK: puts that wrist at character-local (x,y) (elbow bends outward). Use for custom poses; `Rig.rest(tl,c,side,t,{dur})` returns the arm. |
| `Rig.hand(tl, c, side, t, pose)` | `"open"\|"fist"\|"point"`. |
| `Rig.walk(tl, c, t0, t1, dx, {step=0.36})` | Moves `.char` x by dx (from its accumulated x) linearly over t0..t1; legs swing ±20°, arms counter-swing (lagging), body bobs 6 px on each contact and leans 3° into travel. Ends with feet planted and a small settle. |
| `Rig.move(tl, c, t, dur, dx, ease="power2.inOut")` | Slide x by dx without steps (for sitting in a car, being carried…). |
| `Rig.hop(tl, c, t, {height=60})` | 0.1 s squash, 0.32 s jump with stretch, land squash, settle: total 0.6 s. Shadow shrinks while airborne. |
| `Rig.squash(tl, c, t, {amt=0.08, dur=0.35})` | One squash-and-settle (impacts, surprise). |
| `Rig.lean(tl, c, t, deg, dur=0.3)` | Body rotation about the feet (hold until the next lean). |
| `Rig.tilt(tl, c, t, deg, dur=0.25)` | Head rotation about the neck. |
| `Rig.show(tl, c, partSel, t, on=true, dur=0.12)` | Opacity fade of any part inside the char, e.g. `".phone"`, `".laurel"`. |
| `Rig.costume(tl, c, t, "rich"\|"rough")` | Seneca: swaps `.toga` ↔ `.rough-tunic` with a 0.1 s squash pop. |
| `Rig.get(c, partSel)` | Returns the part element (for your own tweens; don't fight Rig's props listed in §2). |

Rules the helpers follow (so you don't have to): `fromTo`/`set` only, explicit times, no `Math.random`/`Date.now`/timers/`repeat:-1`; origins via `gsap.set(el,{svgOrigin})` at mount time (never CSS transforms); parts offset (head leads, arms follow, right side lags), never both arms in unison.

## 5. Boil

One filter per scene (`<filter id="<pfx>-ink" class="ink-boil">` from `characters/defs.svg`), referenced by every `.ink` group in that scene's svg; characters/props carry class `ink` on their root drawing group already. `Rig.boil` makes the whole frame boil at 12 fps. To boil an HTML element (not SVG), give it `style="filter:url(#<pfx>-ink)"` yourself.

## 6. Props (`Rig.prop(target, name)` or paste from `characters/props.svg`)

Each prop is `<g class="prop prop-<name> ink">` drawn around its own anchor (listed), size at scale 1:

| name | anchor | size |
|---|---|---|
| `phone` | center | 46×84 |
| `car` (small hatchback, side view, faces right) | ground center | 300×150; `.car-wheel` parts pivot at their centers (rotate them), `.car-window` area at x -40…70, y -120…-70 for a passenger head |
| `coin` | center | 56 diameter |
| `bread` | bottom center | 120×60 |
| `tunic` (rough folded tunic) | bottom center | 120×110 |
| `scroll` (open journal/scroll) | center | 200×130 |
| `crutch` | foot | 40×300 |
| `boulder` | ground center | 260×200 |
| `laurel` (gold wreath, big) | center | 220×150 |
| `cup` (drinking cup / coffee mug) | bottom center | 50×60 |
