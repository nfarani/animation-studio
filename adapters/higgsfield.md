# ADAPTER — Higgsfield (via CLI: higgsfield / higgs / hf)

Tool-specific notes only. The master shot spec (11_shot_list.md) stays authoritative.
Mark every entry VERIFIED (date, how) or UNVERIFIED. Do not rely on UNVERIFIED capabilities for HIGH-RISK shots.
Update this file whenever `higgsfield --help`, a generation result or creator feedback confirms something.

## Access
- Install: npm install -g @higgsfield/cli · Login: higgsfield auth login
- CLI installed and logged in — VERIFIED 2026-10-06 (`higgsfield version` → 1.1.26; binaries `higgsfield` and `higgs` on PATH; `hf` is listed as an alias in help but is **not** on PATH on this machine)
- Balance check: `higgsfield account status` — VERIFIED 2026-10-06 (returns account, plan and credit balance; read 576.22 credits on the plus plan)
- Same credit pool as the Higgsfield web app — UNVERIFIED (reported by third-party guides)

## CLI commands confirmed to exist — VERIFIED 2026-10-06 (`higgsfield --help`, `higgsfield generate --help`)
- `higgsfield model list --video | --image` — list models
- `higgsfield model get <job_type>` — inspect a model's accepted params (not yet run)
- `higgsfield generate cost <job_type> [--param value]...` — **estimate credits without creating a job** (not yet run)
- `higgsfield generate create <job_type> --prompt ... --image <upload_id>` — create a job (PAID; approval gate applies)
- `higgsfield generate wait | get | list` — job status
- `higgsfield generate workflow <name>` · `higgsfield workflow list` — workflows (e.g. reframe)
- `higgsfield upload` — upload media inputs
- `higgsfield voices` — list voices for text-to-speech and voice-change
- `higgsfield soul-id` — train and manage Soul refs (character identity; not yet explored)
- `higgsfield preset` — browse generation presets

## Supported generation types
- text-to-image — VERIFIED 2026-10-06 that image models are listed; per-model params UNVERIFIED
- reference-image generation — UNVERIFIED (which models, how many references)
- image editing (needed for THEN → NOW plates) — UNVERIFIED (candidates by name in the model list: flux_kontext, nano_banana family, gpt_image family)
- image-to-video — VERIFIED 2026-10-06 only in that `generate create <video_model> --image` appears in CLI help; per-model support UNVERIFIED
- start frame + end frame video — UNVERIFIED
- text-to-video — UNVERIFIED
- lip-sync / speech — UNVERIFIED (a `voices` command exists; no lip-sync model identified yet)
- upscale / background removal / reframe — VERIFIED 2026-10-06 that such job types are listed (video_upscale, topaz_video, sam_3_video, reframe workflow); behaviour UNVERIFIED

## Models listed — VERIFIED 2026-10-06 (`higgsfield model list`); capabilities and cost of each UNVERIFIED
- **Video (generation):** flux_3_video, gemini_omni, gemini_omni_flash_1_1, veo3, veo3_1, veo3_1_lite, grok_video, grok_video_v15, grok_video_v15_lite, happy_horse_video, kling2_6, kling3_0, kling3_0_turbo, minimax_hailuo, minimax_h3, minimax_h3_max, seedance1_5, seedance_2_0, seedance_2_0_mini, seedance_2_5, wan2_6, wan2_7, wan3_0, wan3_0_prime
- **Video (edit / utility):** flux_3_video_edit, kling_video_edit, hf_mult_motion_control, hf_mult_replace_object, video_upscale, bytedance_video_upscale, topaz_video, topaz_hyperion_2_5, fps_boost, video_deflicker, sam_3_video, video_background_remover, depth_anything_video, clipify, ad_multiplier
- **Image (generation / edit):** flux_3_image, flux_2, flux_kontext, gpt_image_2, gpt_image_2_5, grok_image, grok_image_2_0, text2image_soul_v2, soul_cast, soul_cinematic, soul_location, ideogram_4_5, image_auto, kling_omni_image, nano_banana, nano_banana_flash, nano_banana_2_lite, nano_banana_pro (+ relight / shots variants), openai_hazel, recraft_v4_1, seedream_v4_5, seedream_5_0_flash, seedream_v5_lite, seedream_v5_pro, z_image, 3d_jutsu_angles
- **Image (utility):** outpaint, flux_2_pro_outpaint, bytedance_image_upscale, topaz_image, topaz_image_generative, image_background_remover

## Limits
- Video duration: per model. VERIFIED 2026-10-06: `seedance_2_0_mini` minimum 4 s, integer seconds (4, 5, 6, 8, 10 priced); `seedance1_5` only 4/8/12; `veo3_1_lite` only 4/6/8; `minimax_hailuo` only 6/10. Longest clip: UNVERIFIED.
- **Concurrent jobs: 6 per model on the plus plan** — VERIFIED 2026-10-06 (`rate_limit_reached`, `concurrent_jobs_limit: 6`). Submit video jobs in groups of 6 or fewer.
- Output: `seedance_2_0_mini` 720p returns 1280×720, 24 fps, H.264 with stereo AAC audio — VERIFIED 2026-10-06
- Max image resolution: UNVERIFIED (third-party guide says 4K)
- Aspect ratios: `nano_banana_pro` 1:1, 3:2, 2:3, 4:3, 3:4, 4:5, 5:4, 9:16, 16:9, 21:9 · `seedance_2_0_mini` auto, 16:9, 9:16, 4:3, 3:4, 1:1, 21:9 — VERIFIED 2026-10-06 (`model get`)
- Image resolution: `nano_banana_pro` 1k/2k/4k (2k at 16:9 = 2752×1536); `nano_banana_2_lite` 1k only — VERIFIED 2026-10-06

## Controls
- Reference images — VERIFIED 2026-10-06: `nano_banana_pro` and `nano_banana_2_lite` accept up to 14; `seedance_2_0_mini` accepts up to 9 images (counting start and end image), 3 videos, 3 audio files, 12 in total. Each reference needs its own `--image-references <path>` flag; several paths after one flag is an error. Local paths are uploaded automatically.
- Image editing — VERIFIED 2026-10-06: `nano_banana_pro` with one reference and an "edit this image, keep exactly the same camera and framing" prompt keeps fence posts, gateway and horizon aligned well enough for a match cut (the-last-game, THEN_A → NOW_A).
- Start frame / end frame — VERIFIED 2026-10-06: `seedance_2_0_mini` takes `--start-image` and `--end-image`. `kling3_0_turbo` and `grok_video_v15_lite` take a start image only.
- Speech — `seedance_2_0_mini` generates audio by default and animates the mouth when a quoted line is in the prompt (VERIFIED visually 2026-10-06; the audio itself has NOT been listened to).
- Motion controls: UNVERIFIED
- Camera controls: UNVERIFIED

## Model tier map
| Tier | Higgsfield model(s) | Use for | Status |
|---|---|---|---|
| ECONOMY | video: `seedance_2_0_mini` (720p), `grok_video_v15_lite` · image: `nano_banana_2_lite`, `seedream_5_0_flash` | statics, props, inserts, low-motion | cost VERIFIED 2026-10-06; `seedance_2_0_mini` quality VERIFIED on the-last-game (used for every shot, including faces) |
| STANDARD | video: `wan3_0` (used), `kling3_0_turbo`, `wan2_7`, `kling3_0` · image: `nano_banana_pro` (2k) | normal acting, walking, moderate camera | cost VERIFIED 2026-10-06; `wan3_0` quality VERIFIED on the-last-game v2 |
| PREMIUM | video: `seedance_2_0` (used), `wan3_0_prime`, `veo3_1`, `grok_video_v15`, `seedance_2_5` · image: `gpt_image_2` | contact, complex motion, hero close-ups | cost VERIFIED 2026-10-06; `seedance_2_0` quality VERIFIED on the-last-game v2 |

Tiers are assigned from `higgsfield generate cost` results, not from model names.

## Cost profile
VERIFIED 2026-10-06 with `higgsfield generate cost` (free). Re-check before budgeting; prices change.

| Image model | Credits per image |
|---|---|
| z_image | 0.15 |
| seedream_5_0_flash | 0.5 |
| nano_banana_2_lite (1k only), seedream_v5_lite, flux_2 | 1 |
| nano_banana_flash, flux_kontext | 1.5 |
| nano_banana_pro (2k) | 2 |
| gpt_image_2 | 6.5 |

| Video model | Credits for 5 s at default resolution |
|---|---|
| seedance_2_0_mini 480p | 2.5 |
| seedance_2_0_mini 720p, grok_video_v15_lite | 5 (seedance mini is exactly 1 credit per second at 720p) |
| kling3_0_turbo, wan2_7, wan2_6 | 7.5 |
| kling2_6 | 10 |
| happy_horse_video | 12.5 |
| seedance_2_0 | 22.5 |

- Turning `generate_audio` off on seedance_2_0_mini does not lower the price.
- A job that fails before it is created (upload error, rate limit) is not charged.

## To verify next (free, during /assets)
1. `higgsfield model get` on candidate image models: reference-image count, edit support, aspect ratios, resolution
2. `higgsfield model get` on candidate video models: start/end frame inputs, duration options, aspect ratios
3. `higgsfield generate cost` for each candidate, to fill the tier map and cost profile
4. Whether any model or workflow does lip-sync from an audio file
5. `higgsfield soul-id --help`: whether Soul refs suit stylised 3D characters

## Known strengths
- `nano_banana_pro`: character turnarounds are consistent across four views in one image; a derived older version of a character keeps the likeness when the younger sheet is the reference. (the-last-game, 2026-10-06)
- `nano_banana_pro`: holds a character's identity and a location's look when given the character sheet plus an existing plate as references. (the-last-game, 2026-10-06)
- `seedance_2_0_mini`: simple single-action shots from a good keyframe work on the first take (legs running, ball rolling between objects, a wide with four children). (the-last-game, 2026-10-06)

- `wan3_0` (STANDARD): 7 credits per 4 s, 8.75 per 5 s at 720p; duration 2–30 s; start and end image; generates audio and speaks quoted lines. Six shots accepted on the first take, look consistent with the seedance clips. (the-last-game v2, 2026-10-06)
- `seedance_2_0` (PREMIUM): 18 credits per 4 s at 720p (1080p doubles it). Noticeably more restrained facial acting than the mini model from the same keyframe. (the-last-game v2 S05_SH02, 2026-10-06)
- Dialogue: all three video models place a quoted line in the clip's audio. Line timing inside the clip varies (anywhere from 0.3 s to 2.2 s in), so measure it before cutting.
- Audio models — VERIFIED 2026-10-06: `mirelo_text_to_audio` (ambience and effects, 0.25 credits per second, mono mp3), `sonilo_music` (about 0.06 per second), `seed_audio` text-to-speech (0.2). Also listed: elevenlabs_v4, elevenlabs_v4_turbo, inworld_text_to_speech, qwen_audio_tts, text2speech_v2. Output quality has not been listened to.

- `seedance_2_0_mini` handles long dialogue takes: 10 s and 12 s clips with a locked frame (same start and end image) delivered every scripted word in order; 1 credit per second up to at least 15 s. It also accepts `--audio-references` as a voice reference (whether the voice actually matches has not been listened to). (dan-and-the-dandruffs EP01 Part 1, 2026-10-06)
- Chained `wan3_0` clips sharing keyframes (end frame of one = start frame of the next) make one continuous camera move across three clips. (EP01 Part 1 descent, 2026-10-06)
- Text-to-speech: `text2speech_v2` with `--variant elevenlabs --voice_id <id> --voice_type preset`, 0.15 credits for a short line. 113 preset voices, listed by name only, with no description of gender, age or accent. (2026-10-06)
- `sonilo_music`: 45 s for about 2.8 credits; returns m4a. `mirelo_text_to_audio`: mp3, mono. (2026-10-06)

## Known weaknesses
(record from actual generations: identity drift, hands, camera obedience, etc.)
- `seedance_2_0_mini` ignores "static camera" in the prompt and pushes in on a character. **Fix: pass the same image as both `--start-image` and `--end-image`**; the framing then stays locked. (the-last-game S03_SH03, take 1 vs take 2, 2026-10-06)
- `nano_banana_pro` does not reliably follow a described ground plan (which fence the trees stand along, fence height, camera inside vs outside). Pick the best generated view and derive the others from it, rather than prompting for a layout. (the-last-game ENV_PITCH_THEN_E, 3 attempts, 2026-10-06)
- The six-concurrent-jobs limit sometimes rejects a job even when fewer than six of that model are running; resubmit.
- `wan3_0` with "handheld" in the prompt swings the background a long way within a second. (the-last-game v2 S02_SH02)
- **An HTTP 503 on job creation does not mean the job failed.** The job may have been created and charged. Before resubmitting, run `higgsfield generate list`; if the job is there, `higgsfield generate wait <id>` and download it. Resubmitting blindly pays twice (this explains the untraced credits on the-last-game). VERIFIED 2026-10-06 on dan-and-the-dandruffs.
- `wan3_0` with a start frame only redesigns any part of a character not visible in that frame. Use start + end frames for turns. (dan-and-the-dandruffs TEST_HC_TREMOR, 2026-10-06)
- `seedance_2_0_mini` with a start frame only can change the whole background abruptly mid-clip (a hard jump between two frames). It is invisible in a thumbnail sheet; check every clip by measuring frame-to-frame change in regions the character does not cover. (dan-and-the-dandruffs S3_SH03, found by the creator, 2026-10-07)
- **`bytedance_video_upscale` cost estimate is wrong.** `generate cost` quoted 4 credits for a 70 s video at 4K standard; the job was charged 55.87 credits (about 0.8 per second). Do not trust the estimate for this model; assume roughly 0.8 credits per second at 4K standard. (dan-and-the-dandruffs, 2026-10-20)
- Occasional HTTP 503 / 520 on job creation or upload; retrying works. (2026-10-06)
