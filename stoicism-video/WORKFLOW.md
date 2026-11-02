# WORKFLOW: parallel cartoon production, no collisions

Read order for every agent: `production/BIBLE.md` → `production/STORYBOARD.md` → `production/RIG_API.md` (once it exists) → `SPEC.md` (format, safe zones, HyperFrames contract, caption band).

## Pipeline
| Phase | Who | Runs |
| --- | --- | --- |
| 1 | Character Designer, Animators 1–4 (Step A), Captions, Sound | all in parallel |
| 2 | Designer reports "RIG READY" → CEO reviews the expression sheet → CEO tells animators "RIG READY" → Animators Step B (drop in the real rigs) | parallel |
| 3 | CEO integration: review each scene, send fixes back to the owner, audio cues, `check`, `snapshot --review` | serial |
| 4 | CEO renders `renders/stoicism-in-90-seconds.mp4` | serial |
| 5 | Final Reviewer audits everything (launched by the orchestrator) | serial |

Animator Step A (start immediately): environment/background layers, props, camera moves, hand-lettered words, timing table, and **placeholder characters** that follow the RIG_API anchors (simple ink silhouettes of the right size). If RIG_API.md doesn't exist yet, use a feet-baseline anchor and a 520 px tall adult, and leave the character markup in clearly marked `<!-- CHAR:name -->` blocks. Step B: replace the placeholders with `characters/*.svg` markup and animate with `assets/rig.js`.

## Lanes (write ONLY your lane)
| Agent | Owns | Snapshot dir |
| --- | --- | --- |
| Character Designer | `characters/*`, `assets/rig.js`, `production/RIG_API.md`, `production/expression-sheet.png`, `.hyperframes/rig-lab/` | `.hyperframes/snap-rig/` |
| Animator 1 | `compositions/s1_hook.html`, `compositions/s2_what.html`, `assets/scenes/s1_hook/*`, `assets/scenes/s2_what/*` | `.hyperframes/snap-an1/` |
| Animator 2 | `compositions/s3_control.html`, `compositions/s4_traffic.html`, `assets/scenes/s3_control/*`, `assets/scenes/s4_traffic/*` | `.hyperframes/snap-an2/` |
| Animator 3 | `compositions/s5_story.html`, `compositions/s6_obstacle.html`, `assets/scenes/s5_story/*`, `assets/scenes/s6_obstacle/*` | `.hyperframes/snap-an3/` |
| Animator 4 | `compositions/s7_seneca.html`, `compositions/s8_close.html`, `assets/scenes/s7_seneca/*`, `assets/scenes/s8_close/*` | `.hyperframes/snap-an4/` |
| Captions | `compositions/captions.html`, `.hyperframes/snap-E/*` | `.hyperframes/snap-E/` |
| Sound | `assets/music/*`, `script/audio_cues.json`, `.hyperframes/audio-F/*` | `.hyperframes/audio-F/` |
| CEO | `index.html`, `production/BIBLE.md`, `production/STORYBOARD.md`, `production/STATUS.md`, `compositions/bg.html`, `renders/*`, fixes after a lane is closed | `.hyperframes/snap-ceo/` |

Read-only for everyone else: `SPEC.md`, `WORKFLOW.md`, `production/*` (except your own file), `script/*`, `assets/voice/*`, `assets/sfx/*`, `characters/*` and `assets/rig.js` (except the designer).
No git, no `npm install` in the project, no preview server. Never delete files outside your lane. If you need something outside your lane, message its owner (or the CEO).

## Self-check loop (every visual worker)
1. `cd /home/user/prospect-finder/stoicism-video && npx hyperframes lint`: zero errors in your files.
2. `npx hyperframes snapshot --composition <scene-id> --frames 10 -o .hyperframes/<your snap dir>/<scene-id>`. On a port/browser conflict with a parallel worker, retry with a bounded loop (`for i in 1 2 3; do … && break; sleep 15; done`).
3. Open every PNG with the Read tool and judge it against BIBLE + STORYBOARD: on-model characters, acting reads, nothing clipped, safe zones respected, beats on time. Fix, then re-snapshot. At least 2 rounds per step.
4. Report to the CEO by SendMessage (≤ 200 words), then end your final message with the same report.

HyperFrames docs: `$HF=/tmp/claude-0/-home-user-prospect-finder/b673fc1b-a9a8-5b77-ab8d-5e5873bf956c/scratchpad/hyperframes/skills/hyperframes` (`SKILL.md`, `references/types/character.md`, `format.md`, `motion.md`, `runtimes.md`, `captions.md`, `sound.md`, `review.md`). Python venv: `/tmp/claude-0/-home-user-prospect-finder/b673fc1b-a9a8-5b77-ab8d-5e5873bf956c/scratchpad/venv/bin/python`.
