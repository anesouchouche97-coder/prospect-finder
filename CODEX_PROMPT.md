# Prompt for Codex: "Stoicism in 90 Seconds", a character-animated vertical short

> Paste everything below the line into Codex. It is self-contained.

---

## Role and goal

You are a senior motion designer and creative coder. Produce a **finished MP4**: an educational, **character-animated cartoon** (not a motion-graphics or kinetic-type video) that makes a viewer understand **Stoicism** and stay excited enough to watch to the end. It has burned-in subtitles and an American-accent voiceover, and runs about 93 seconds.

Work in the GitHub repo `anesouchouche97-coder/prospect-finder`. Start from branch `ccr-d368c765-7nbo3q` (it has the shared foundation listed below), create your own branch `codex/stoicism-video`, and put your entire project in a new folder **`stoicism-video-codex/`**. Do not modify `stoicism-video/` (another team's version, kept for comparison). Commit and push your branch when done.

## Hard requirements (acceptance criteria)

1. **Output:** `stoicism-video-codex/renders/stoicism-in-90-seconds.mp4`, H.264, 1080×1920 (9:16 vertical), 30 fps, 93.26 s (±0.1 s), AAC audio.
2. **Real character animation:** recurring, recognizable characters that act, with blinks, lip-sync to the narration when a character speaks on screen, expression changes, gestures, walking, squash and stretch, anticipation and follow-through. Characters must be on screen in every scene. Animated text alone is a fail.
3. **Trending style:** hand-drawn 2D cartoon with **"boiling" ink lines** (the outline wobble redraws 12 times per second) on warm parchment, the look of the popular faceless philosophy/psychology shorts. The wobble must be **deterministic** (seeded from `Math.floor(t * 12)`, never unseeded `Math.random()`), so renders are reproducible.
4. **Voiceover:** use the existing American male narration `stoicism-video/assets/voice/narration.wav` (copy it into your folder). Do not change the script. If you prefer to regenerate, use an American English voice and keep the exact script and the scene slot timings below.
5. **Subtitles:** burned in, word-synced, trending "word-pop" style. Groups of 2–3 words, bold uppercase sans (Inter 900 or similar), white/ivory text with a thick dark outline, and the **currently spoken word highlighted** (gold `#E0A84A`, scale 1.12). One group on screen at a time, inside the band y = 1120–1340 px, never clipped at the frame edges.
6. **Music and SFX:** an original, royalty-free ambient cinematic bed (synthesize it yourself, e.g. with numpy: D minor pads resolving to major in the final scene, soft pulse at about 72–84 BPM), about 18–22 LU under the voice. Tasteful SFX on visible actions (whooshes on scene changes, impacts on stamps, pops, clicks). Pixabay-licensed SFX are available in `stoicism-video/assets/sfx/` (see its `CREDITS.md`). Mix true peak ≤ −1 dBTP, narration around −16 LUFS.
7. **Platform safe zones (1080×1920):** nothing readable above y = 200 px. Faces and key action framed in y = 250–1100. The caption band y = 1120–1340 stays clear of faces and key action. Nothing important below y = 1340 (app UI covers it). Keep x within 90–990.
8. **Accuracy:** every historical claim must be correct (see "Facts" below).
9. **No black frame 0:** frame 0 is the thumbnail and must already show the hook.
10. **Deterministic and offline at render time:** no network fetches during render, and no `Date.now()`, timers or unseeded randomness.

## Shared foundation already in the repo (reuse it)

- `stoicism-video/script/s1_hook.txt … s8_close.txt`: the 8 voice lines (below).
- `stoicism-video/assets/voice/narration.wav`: the final narration (Kokoro TTS voice `am_michael`, American male), 93.26 s, already placed with the gaps between scenes.
- `stoicism-video/script/scenes.json`: the 8 scene slots (`start`, `duration`) and **scene-local word timings** (`words[]` with `start`/`end` in seconds). Use them to sync every visual beat, the lip-sync and the captions.
- `stoicism-video/script/words_global.json`: all 236 words with global timestamps (for captions and SFX).
- `stoicism-video/assets/sfx/*.mp3`: SFX.

## Recommended stack (you may choose another if the output is equal or better)

**HyperFrames** (open-source by HeyGen: HTML + CSS + GSAP compositions rendered frame by frame to MP4):
- `npx hyperframes@0.8.229 init stoicism-video-codex --resolution portrait --non-interactive --skip-skills`
- Read the docs and skills first: `git clone --depth 1 https://github.com/heygen-com/hyperframes` and read `skills/hyperframes/SKILL.md`, then `references/types/character.md`, `motion.md`, `format.md`, `captions.md`, `sound.md`, `review.md`, `types/vertical.md`. The registry (`registry/blocks`, `registry/components`) has ready-made transitions (whip-pan, ink/iris reveals, camera shake).
- Contract: one root `index.html` mounting one sub-composition per scene (`compositions/<scene-id>.html`, everything inside `<template>`, root styled as `#root`). Every timed element has `class="clip"`, an `id`, `data-start` and `data-duration`. Each composition registers one paused GSAP timeline: `window.__timelines["<id>"] = tl`. Use `fromTo`, not `from`. Never tween `display`/`visibility` on a `.clip`, and no CSS `transform` on GSAP-animated elements. Every `<audio>` has an `id`.
- Gate: `npx hyperframes lint` and `npx hyperframes check --json` with zero errors, then `npx hyperframes snapshot --review` and look at every frame, then `npx hyperframes render` (high quality).
- Alternative: Remotion (React) is acceptable if you prefer it.

**Character technique:** inline SVG characters with class-named parts (`.head .eye-l .eye-r .lid-l .lid-r .brow-l .brow-r .mouth-rest .mouth-open .mouth-wide .mouth-o .mouth-smile .torso .arm-l .forearm-l .hand-l .arm-r … .leg-l .leg-r`). Write a shared deterministic rig helper (`assets/rig.js`) exposing, for example, `Rig.boil`, `Rig.blink`, `Rig.talk(words)` (mouth shapes from word timings: vowels like a/o open wide or O, consonants half-open, pauses rest), `Rig.emote([[t,"angry"],[t,"calm"]])`, `Rig.gesture`, `Rig.walk`, `Rig.breathe`. Every helper only adds tweens/sets to the passed GSAP timeline, so it can be seeked. For boiling lines, either an SVG `feTurbulence` + `feDisplacementMap` filter whose `seed` attribute steps every 1/12 s via `tl.set`, or two or three alternate path sets swapped 12×/s.

## Workflow (to compare fairly, work as a structured parallel pipeline if you can)

1. **Direction:** write `production/BIBLE.md` (palette, line weights, boil method, proportions, expressions, mouth shapes, camera grammar, transitions), `production/RIG_API.md` (character contract: viewBox, feet-baseline anchor and part names), and `production/STORYBOARD.md` (shots per scene tied to the word timings).
2. **In parallel:** (a) character designer: `characters/*.svg` + `assets/rig.js` + an expression/lip-sync test sheet; (b) four scene animators (scenes 1–2, 3–4, 5–6, 7–8): backgrounds, props, camera and timing with placeholder characters at the RIG_API anchors, then drop in the real rigs; (c) captions; (d) music and SFX cue sheet.
3. **Integration:** assemble, add audio cues, run the checks, review the frames at every scene start, middle and cut, check the lip-sync against the words, then render.
4. **Final QA pass:** review the rendered MP4 frame by frame (extract frames with ffmpeg every 0.5 s and at every cut). Check every caption against the voice, safe zones, spelling, facts, audio levels, black or blank frames, stale captions, overlapping text, clipped elements, characters popping or snapping, missing blinks, and lip-sync drift. Fix everything, even small issues, and re-render. Write `REVIEW.md` listing what you checked and fixed.

## Look and cast

- **Palette:** parchment ground `#F3E9D2` with paper grain and a soft vignette; ink `#1E1A16`; terracotta `#C65A3A`; ochre gold `#E0A84A`; olive `#7A8450`; Tyrian purple `#6B2D5C` (the emperor only); muted sky `#8DB1C4` (sparingly). Flat fills, 6–8 px ink outlines that boil.
- **Proportions:** big expressive heads (about 1:3), readable silhouettes, hand-lettered words only for a few emphasis moments (the characters carry the story).
- **Camera:** push-ins on emphasis, pans across a scene, parallax layers, and an ink-wipe or whip-pan transition between scenes. A new visual beat every 2–4 s and a visual joke or surprise about every 5 s.
- **Cast:**
  - **Marcus Aurelius:** the host/guide. Laurel wreath, curly beard, purple-trimmed toga, calm and warm. Lip-synced whenever he narrates on screen.
  - **Epictetus:** bearded, simple worn tunic, leans on a crutch (he was lame), sharp and witty.
  - **Seneca:** bald, round face, rich toga, then rough clothes.
  - **Alex:** the modern everyday viewer-avatar. Hoodie, phone, very expressive (panic, anger, relief). Lives through every example.
  - **Extras:** cars and a traffic jam, a friend's chat avatar, a silhouette crowd, an interviewer or exam desk.

## Script and storyboard (keep these slots; times are global seconds)

| # | Slot | Voice line | What we see (suggested; improve it) |
|---|---|---|---|
| 1 `s1_hook` | 0.00–11.14 | "The most powerful man on Earth wrote himself a warning every morning. Today, I will meet rude, ungrateful, selfish people. And he was totally fine with it." | Frame 0: Marcus on a throne at dawn in a Roman palace, hand-lettered "THE MOST POWERFUL MAN ON EARTH". He writes in a journal by candlelight. As each of "rude", "ungrateful", "selfish" is spoken, a cartoon character of that type pops up around him (a rude senator, an ungrateful servant, a selfish courtier grabbing food). On "totally fine with it": Marcus calmly sips his drink, unbothered, with a smug smile and a slow push-in. |
| 2 `s2_what` | 11.14–21.06 | "That man was Marcus Aurelius, Roman emperor. His secret? Stoicism. A two-thousand-year-old operating system for your mind." | Name card painted as a scroll banner: "MARCUS AURELIUS, Emperor 161–180 AD". Marcus leans in to whisper "Stoicism" to camera. Gag: he taps Alex's head (modern Alex appears), and a cartoon brain opens like a computer, with a loading bar "Installing STOICISM… 100%". |
| 3 `s3_control` | 21.06–33.83 | "Rule one comes from Epictetus, a man born a slave. Split your life into two piles. What you control: your thoughts, your effort, your actions. And what you don't: the weather, other people, the past." | Big hand-lettered "RULE 1". Epictetus hobbles in on his crutch, chains breaking off his ankles ("born a slave"). He sorts objects into two baskets with Alex: gold basket "YOURS" (a thought bubble, a sweat drop/dumbbell for effort, a hand for actions), terracotta basket "NOT YOURS" (a storm cloud raining on Alex, other people as gossiping silhouettes, a clock running backwards). Each item lands exactly when spoken. |
| 4 `s4_traffic` | 33.83–46.62 | "Example. You're stuck in traffic, late for work. The traffic? Not yours. Yelling at it changes nothing. What is yours? A quick text, a good podcast. Same traffic. Totally different day." | Alex in a tiny car in an endless jam, clock 8:52, steam from his ears, honking. Epictetus pops up in the passenger seat. "NOT YOURS" stamp on the jam. Alex yells and the angry scribble cloud fizzles into nothing. Alex calms down, sends a quick text ("Running 10 min late, sorry!") and puts on headphones with a podcast. Same jam, but now the sun comes out and Alex is bobbing his head, happy. |
| 5 `s5_story` | 46.62–59.13 | "Rule two. Events don't hurt you. Your story about them does. Your friend leaves you on read. The event: no reply. The story: they hate me. Drop the story, and most of the pain goes with it." | "RULE 2". Alex on the couch staring at his phone: "Read 9:41 PM". A thought bubble balloons into a dramatic imagined movie (the friend laughing with others, Alex alone in the rain): the "story". Marcus pops the bubble with a pin, and the drama collapses into the plain fact, "no reply" (the friend is actually just asleep). Alex's pain meter drains and he exhales. |
| 6 `s6_obstacle` | 59.13–69.67 | "Rule three. Marcus wrote: what stands in the way becomes the way. Rejected? That's reps for resilience. Failed an exam? Now you know exactly what to study." | "RULE 3". Marcus writes the line in his *Meditations*. Alex walks a path and hits a giant boulder. He pushes, then the boulder tips over and becomes a stair step he climbs. Quick gags: a rejection letter turns into a dumbbell Alex lifts ("reps"); a red "F" exam paper turns into a treasure map pointing at the exact chapters to study. |
| 7 `s7_seneca` | 69.67–81.58 | "And Seneca, one of the richest men in Rome, would practice being poor. Plain food. Rough clothes. Then he'd ask: is this what I was so afraid of? Fear shrinks when you rehearse it." | Seneca in a villa swimming in gold coins. He swaps the feast for plain bread and his rich toga for a rough tunic, and shrugs: "is this what I was so afraid of?" A big shadowy FEAR monster looms over Alex. As they "rehearse it", it literally shrinks to a tiny, harmless creature Alex picks up. |
| 8 `s8_close` | 81.58–93.26 | "So tomorrow, when something goes wrong, ask one question. Is this in my control? If yes, act. If no, let it go. Three rules. Two thousand years. Your move." | Alex wakes up the next morning and something goes wrong (he spills coffee). He freezes, and Marcus, Epictetus and Seneca appear like little shoulder-angels. Question card "Is this in my control?" YES branch: Alex cleans it up (act). NO branch (rain outside): Alex lets a balloon float away (let it go). Final: the three Stoics line up behind Alex, "3 RULES · 2,000 YEARS · YOUR MOVE." Alex turns to camera and smiles, and the end frame holds with gentle breathing. |

## Facts (must stay accurate)

- Marcus Aurelius: Roman emperor 161–180 AD. His private journal is known as *Meditations*. Book 2.1 begins with the morning warning about meeting meddling, ungrateful, arrogant people. "What stands in the way becomes the way" paraphrases *Meditations* 5.20.
- Epictetus: born a slave (in Hierapolis), later freed. Lame in one leg. Taught the "dichotomy of control" (*Enchiridion* 1).
- Seneca: one of the wealthiest men in Rome, advisor to Nero. In *Letter 18* he recommends spending days with scanty food and coarse dress, asking "Is this the condition that I feared?"

## Deliverables

- `stoicism-video-codex/renders/stoicism-in-90-seconds.mp4`
- Full source project (compositions, characters, rig, audio, cue sheet), `production/BIBLE.md`, `RIG_API.md`, `STORYBOARD.md`, `REVIEW.md`
- A short `README.md`: how to re-render, tools used, and a list of known limitations.
- Commit and push branch `codex/stoicism-video`. Report the ffprobe summary (resolution, duration, fps, audio stream) and the final check/lint counts.
