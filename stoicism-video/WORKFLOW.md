# WORKFLOW — parallel production, no collisions

Phase 1 (parallel): Workers A–F build at the same time, each inside its own lane.
Phase 2 (serial): Task Manager integrates, runs `check` + review, and renders.
Phase 3 (serial): Final Reviewer audits the rendered MP4 against everything and reports or fixes.

## Lanes (file ownership — write ONLY your lane)
| Worker | Owns (may create/overwrite) | Snapshot dir |
| --- | --- | --- |
| A | `compositions/s1_hook.html`, `compositions/s2_what.html` | `.hyperframes/snap-A/` |
| B | `compositions/s3_control.html`, `compositions/s4_traffic.html` | `.hyperframes/snap-B/` |
| C | `compositions/s5_story.html`, `compositions/s6_obstacle.html` | `.hyperframes/snap-C/` |
| D | `compositions/s7_seneca.html`, `compositions/s8_close.html` | `.hyperframes/snap-D/` |
| E | `compositions/captions.html` | `.hyperframes/snap-E/` |
| F | `assets/music/*`, `script/audio_cues.json`, `.hyperframes/audio-F/*` | `.hyperframes/audio-F/` |
| Task Manager | `index.html`, `compositions/bg.html`, `renders/*`, any fix after Phase 1 | `.hyperframes/snap-TM/` |

Read-only for everyone: `SPEC.md`, `WORKFLOW.md`, `script/scenes.json`, `script/words_global.json`, `script/*.txt`, `assets/voice/*`, `assets/sfx/*`.
No git commands. No `npm install` in the project. No preview server. Never delete files outside your lane. If you need something outside your lane, write it in your report instead of doing it.

## Worker procedure (A–E)
1. Read `SPEC.md` fully, then the HyperFrames docs: `$HF/skills/hyperframes/SKILL.md`, `$HF/skills/hyperframes/references/format.md`, `motion.md`, `look.md`, `types/explainer.md`, `types/vertical.md` (E also: `captions.md`). `$HF=/tmp/claude-0/-home-user-prospect-finder/b673fc1b-a9a8-5b77-ab8d-5e5873bf956c/scratchpad/hyperframes` (reference docs only).
2. Read your scenes' `words[]` in `script/scenes.json` (scene-local seconds). Write a short beat table (word → visual → time) before coding.
3. Write the composition(s) following the SPEC contract.
4. `cd /home/user/prospect-finder/stoicism-video && npx hyperframes lint` → zero errors attributed to your files (ignore other lanes' findings).
5. `npx hyperframes snapshot --composition <scene-id> --frames 8 -o .hyperframes/snap-<letter>/<scene-id>` (E: `--range` windows, e.g. `--at` a few word times). If a run fails because of a port or browser conflict with a parallel worker, wait about 20 s (use a short `timeout`-bounded retry loop, not a bare sleep) and retry.
6. **Open every PNG with the Read tool and judge it**: hierarchy, spacing, nothing clipped or overlapping, safe zones respected (nothing readable above y=200; scenes leave y 1120–1340 empty for captions), motion state sensible at that time, premium look. Fix, then re-snapshot. Do at least 2 rounds.
7. Final report (≤ 250 words): files, beat table with times, lint result, known issues.

## Worker F procedure
1. Read `SPEC.md` (Sound), `$HF/skills/hyperframes/references/sound.md`, `$HF/skills/media-use/references/mixing.md`, `$HF/skills/media-use/audio/references/sfx.md`.
2. Use the venv Python `/tmp/claude-0/-home-user-prospect-finder/b673fc1b-a9a8-5b77-ab8d-5e5873bf956c/scratchpad/venv/bin/python` (pip install numpy/scipy into it if missing); scripts live in `.hyperframes/audio-F/`.
3. Make the original music bed, the cue sheet, and a verification mix, as described in your prompt.
4. Final report: files, cue list summary, loudness numbers, known issues.
