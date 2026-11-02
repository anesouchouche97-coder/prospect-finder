# STATUS board (owned by the CEO)

| Agent | Id | Task | Status | Notes |
| --- | --- | --- | --- | --- |
| CEO | (this) | index.html parchment bg (`compositions/bg.html`), rig stub, integration, render | bg + stub DONE; waiting on lanes | lint 0/0 |
| Character Designer | a6e48a541dc3495a1 | `characters/*.svg`, `defs.svg`, `assets/rig.js`, `RIG_API.md`, expression sheet | running | told: `assets/rig.js` is a CEO no-op stub, overwrite it |
| Animator 1 | acb889a79b40b7bd8 | s1_hook, s2_what | Step A | |
| Animator 2 | ae71b17c5665cd186 | s3_control, s4_traffic | Step A | |
| Animator 3 | a19e1e2c00f11dad9 | s5_story, s6_obstacle | Step A | |
| Animator 4 | a1c4d210f89a13d22 | s7_seneca, s8_close | Step A | |
| Captions | a65c3bdbc75c2570b | `compositions/captions.html` | running | early frame: missing space between "MOST" and "POWERFUL" |
| Sound | a9767ac2ceadf8586 | `assets/music/*`, `script/audio_cues.json` | running | |

## Milestones
- [x] Parchment background + rig stub (CEO)
- [ ] RIG_API ready → heads-up to animators
- [ ] RIG READY → CEO review of expression sheet → "RIG READY" to animators
- [ ] All scenes Step B reviewed and accepted
- [ ] Captions accepted
- [ ] Sound cues accepted + inserted into AUDIO-CUES
- [ ] `check --json` clean, `snapshot --review` pass
- [ ] Render `renders/stoicism-in-90-seconds.mp4` verified

## Review log
- (empty)
