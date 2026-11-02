# STATUS board (owned by the CEO)

| Agent | Id | Task | Status | Notes |
| --- | --- | --- | --- | --- |
| CEO | (this) | index.html parchment bg (`compositions/bg.html`), rig stub, integration, render | bg + stub DONE; waiting on lanes | lint 0/0 |
| Character Designer | a6e48a541dc3495a1 | `characters/*.svg`, `defs.svg`, `assets/rig.js`, `RIG_API.md`, expression sheet | RIG_API delivered; real rig.js + sheet in progress | told: `assets/rig.js` is a CEO no-op stub, overwrite it |
| Animator 1 | acb889a79b40b7bd8 | s1_hook, s2_what | Step A | |
| Animator 2 | ae71b17c5665cd186 | s3_control, s4_traffic | Step A | |
| Animator 3 | a19e1e2c00f11dad9 | s5_story, s6_obstacle | Step A | |
| Animator 4 | a1c4d210f89a13d22 | s7_seneca, s8_close | Step A | |
| Captions | a65c3bdbc75c2570b | `compositions/captions.html` | v2 ACCEPTED | v1: 108 groups, spacing fixed. Fixes: bridge gaps <0.4 s (blank at 30.2), always one gold word (52.0) |
| Sound | a9767ac2ceadf8586 | `assets/music/*`, `script/audio_cues.json` | running | |

## Milestones
- [x] Parchment background + rig stub (CEO)
- [x] RIG_API ready → heads-up to animators (CEO asked designer for Rig.sit/stand, "scared" mood, optional lift gesture + balloon/dumbbell/headphones props)
- [ ] RIG READY → CEO review of expression sheet → "RIG READY" to animators
- [ ] All scenes Step B reviewed and accepted
- [x] Captions accepted (v2; re-check over scene art at integration)
- [ ] Sound cues accepted + inserted into AUDIO-CUES
- [ ] `check --json` clean, `snapshot --review` pass
- [ ] Render `renders/stoicism-in-90-seconds.mp4` verified

## Review log
- Captions v1 (CEO): good look on parchment; 2 timing fixes sent.
- Captions v2 (CEO): gaps bridged, one gold word always; accepted.
