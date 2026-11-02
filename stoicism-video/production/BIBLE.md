# BIBLE: cartoon style for the Stoicism short

Authoritative for every agent (supersedes SPEC.md's "Look" and "Scenes" sections; SPEC.md format, safe zones, HyperFrames contract and caption band stay valid).

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

## Boiling ink (one method for everyone)
Defined by the Character Designer in `production/RIG_API.md` and `characters/defs.svg`; call `Rig.boil(tl, ...)` once per scene for the whole scene duration. Backgrounds and props use the same `.ink` class/filter, so the whole frame boils together at 12 fps.

## Composition rules
- Characters' faces sit in y 250–1100; caption band y 1120–1340 stays clear of faces/key action (ground lines and feet may pass behind it); nothing readable above y 200; x within 90–990.
- Each scene = parchment environment (2–3 parallax layers drawn in the same ink style) + characters + few props. Hand-lettered words only for "RULE 1/2/3", name banners, stamps and short labels (Playfair Display 900 or italic, ink color, slight rotation).
- Camera: wrap the scene's world in a `.cam` group; push-ins (scale 1→1.12), pans, small shake on impacts. Transition out: the last 0.3 s of each scene does an ink-wipe or whip-pan out; the next scene's first 0.3 s whips in.
- Acting per HyperFrames `references/types/character.md`: anticipation, squash/stretch, offset parts, blink every 2–4 s, hold reactions ≥0.6 s, eyes look at what matters.
