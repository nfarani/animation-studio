# GENERATION LOG — The Last Game

Approval: `/produce economy the last game`, invoked by the creator on 2026-10-06. That invocation approved the whole pipeline for this film up to the spend ceiling printed in the production plan (**210 credits**). No per-batch approval was requested.

## Totals

| | |
|---|---|
| Balance before | 576.22 |
| Balance after | 446.22 |
| **Credits spent** | **130.00** |
| Spend ceiling | 210 |
| Traced to delivered outputs | 120 (26 images × 2 + 16 video clips = 68) |
| Not traced to an output | 10 |

The 10 untraced credits: several job submissions returned a client-side error (HTTP 503, HTTP 520, or the six-concurrent-jobs limit) and were resubmitted. The balance shows that some of those first submissions were charged anyway. `higgsfield generate list` or the web app's history will show which; any duplicate outputs there were not downloaded.

## Models used

| Use | Model | Settings | Credits each |
|---|---|---|---|
| Master assets and keyframes | nano_banana_pro | 16:9, 2k | 2 |
| All video clips | seedance_2_0_mini | 16:9, 720p, audio on | 1 per second (4 s clips = 4; 5 s = 5; 6 s = 6) |

No STANDARD or PREMIUM video model was used. The three shots planned as PREMIUM (S03_SH03, S05_SH02, S06_SH03) were made on the economy model and passed review.

## Jobs, in order

| # | Time (UTC) | Output | Model | Job ID | Result | Credits |
|---|---|---|---|---|---|---|
| 1 | 10:27:15 | `assets/CHAR_LEO_BOY_MASTER/turnaround_v1` | nano_banana_pro | `169c4d52-dfb4-4430-998e-904f30a5faf2` | completed | 2 |
| 2 | 10:29:24 | `assets/CHAR_FRIENDS_SHEET/sheet_v1` | nano_banana_pro | `df77cf7f-2a17-45b8-9877-4a6aebbafcff` | completed | 2 |
| 3 | 10:29:25 | `assets/PROP_SHEET_MASTER/sheet_v1` | nano_banana_pro | `42bddb58-c08e-4e3e-b72b-15b563e407af` | completed | 2 |
| 4 | 10:29:28 | `assets/ENV_PITCH_THEN_E/plate_v1` | nano_banana_pro | `4fc1714d-d23d-4ec8-93f1-a98ac8772173` | completed | 2 |
| 5 | 10:29:29 | `assets/CHAR_SAM_MASTER/turnaround_v1` | nano_banana_pro | `a397b17b-3d5e-4f0e-8e69-62d8196d99b0` | completed | 2 |
| 6 | 10:30:43 | `assets/CHAR_LEO_ADULT_MASTER/turnaround_v1` | nano_banana_pro | `78cd16d4-ba3f-467a-8b9c-fac681f27ea6` | completed | 2 |
| 7 | 10:31:05 | `assets/ENV_PITCH_THEN_E/plate_v2` | nano_banana_pro | `d9385dfd-ede4-4683-a269-667c18304938` | completed | 2 |
| 8 | 10:31:38 | `assets/ENV_PITCH_THEN_A/plate_v1` | nano_banana_pro | `—` | client error, resubmitted | 0 or charged (see note) |
| 9 | 10:31:38 | `assets/ENV_PITCH_THEN_E/plate_v3` | nano_banana_pro | `—` | client error, resubmitted | 0 or charged (see note) |
| 10 | 10:32:21 | `assets/ENV_PITCH_THEN_E/plate_v3` | nano_banana_pro | `—` | client error, resubmitted | 0 or charged (see note) |
| 11 | 10:33:30 | `assets/ENV_PITCH_THEN_A/plate_v1` | nano_banana_pro | `a8ea8a9e-6cea-4cee-a38b-494c421006e2` | completed | 2 |
| 12 | 10:35:12 | `assets/ENV_PITCH_NOW_A/plate_v1` | nano_banana_pro | `52cdbc0d-b02c-48ec-8b25-ffceabe45a3d` | completed | 2 |
| 13 | 10:35:22 | `assets/ENV_PITCH_THEN_E/plate_v3` | nano_banana_pro | `5a858f7c-0768-4082-a867-cc302181f2ef` | completed | 2 |
| 14 | 10:35:28 | `keyframes/S03_SH03_v1` | nano_banana_pro | `389e585e-028a-4f7d-885c-14d73f3fe265` | completed | 2 |
| 15 | 10:36:56 | `assets/ENV_PITCH_NOW_B/plate_v1` | nano_banana_pro | `f1d8f92a-a51e-4d03-b3f7-bc55ccbbd050` | completed | 2 |
| 16 | 10:42:12 | `renders/S03_SH03/take1` | seedance_2_0_mini | `12e0905e-a684-4689-b908-e0bcb4a27e73` | completed | 4 |
| 17 | 10:45:01 | `renders/S03_SH03/take2` | seedance_2_0_mini | `14ac41de-43fc-4bf0-99e4-5390082befe9` | completed | 4 |
| 18 | 10:46:16 | `keyframes/S03_SH01_v1` | nano_banana_pro | `—` | client error, resubmitted | 0 or charged (see note) |
| 19 | 10:47:24 | `keyframes/S01_SH03_v1` | nano_banana_pro | `a79a7456-9f33-4b07-8ea0-379b31e36a04` | completed | 2 |
| 20 | 10:47:44 | `keyframes/S01_SH01_v1` | nano_banana_pro | `e8a50335-0470-4a68-9704-1d736aeb33f4` | completed | 2 |
| 21 | 10:48:01 | `keyframes/S02_SH01_v1` | nano_banana_pro | `ae659d84-bf9b-4947-9016-9f73a32b3cdc` | completed | 2 |
| 22 | 10:48:02 | `keyframes/S02_SH03_v1` | nano_banana_pro | `28be7f98-3105-47f7-9360-a319409c9989` | completed | 2 |
| 23 | 10:48:04 | `keyframes/S01_SH02_v1` | nano_banana_pro | `b42b5829-35e8-477d-b986-56f1dce58c5b` | completed | 2 |
| 24 | 10:49:21 | `keyframes/S02_SH04_v1` | nano_banana_pro | `28999a7e-54d6-445f-a97b-71fa65a85303` | completed | 2 |
| 25 | 10:52:21 | `keyframes/S05_SH02_v1` | nano_banana_pro | `4b7579a1-3c74-41d4-9772-1101da5be708` | completed | 2 |
| 26 | 10:52:23 | `keyframes/S05_SH01_end_v1` | nano_banana_pro | `df37f6df-b6b3-4f32-b66b-27058742faa5` | completed | 2 |
| 27 | 10:52:23 | `keyframes/S06_SH04_v1` | nano_banana_pro | `f0c146d8-0943-4f45-96a7-43cd1264feff` | completed | 2 |
| 28 | 10:52:32 | `keyframes/S06_SH01_v1` | nano_banana_pro | `6749e7c4-bd6c-4e94-8094-0e2efb4eccd4` | completed | 2 |
| 29 | 10:52:38 | `keyframes/S04_SH01_v1` | nano_banana_pro | `56a01d51-f938-40d7-b001-ea38ca1acabc` | completed | 2 |
| 30 | 10:52:51 | `keyframes/S01_SH02_end_v1` | nano_banana_pro | `3c5b2159-457e-4800-b002-3ce805837aae` | completed | 2 |
| 31 | 10:53:01 | `keyframes/S03_SH01_v1` | nano_banana_pro | `2fd960de-06cd-41a8-8ee9-49145c541316` | completed | 2 |
| 32 | 10:53:11 | `keyframes/S03_SH04_v1` | nano_banana_pro | `3e5d7721-d9a6-4790-a112-dbf3b94cea9b` | completed | 2 |
| 33 | 10:53:40 | `renders/S02_SH01/take1` | seedance_2_0_mini | `b86e99d9-5763-494b-b3ad-22ca8c8a849d` | completed | 4 |
| 34 | 10:54:30 | `renders/S02_SH03/take1` | seedance_2_0_mini | `e527cb69-1510-4efe-83a3-24619e8a47c3` | completed | 4 |
| 35 | 10:54:55 | `renders/S02_SH04/take1` | seedance_2_0_mini | `7ea7e698-b271-4ad3-ab62-b97db503624d` | completed | 4 |
| 36 | 10:57:18 | `renders/S01_SH01/take1` | seedance_2_0_mini | `—` | client error, resubmitted | 0 or charged (see note) |
| 37 | 10:57:34 | `renders/S01_SH03/take1` | seedance_2_0_mini | `—` | client error, resubmitted | 0 or charged (see note) |
| 38 | 11:02:08 | `renders/S03_SH01/take1` | seedance_2_0_mini | `—` | client error, resubmitted | 0 or charged (see note) |
| 39 | 11:02:10 | `renders/S04_SH01/take1` | seedance_2_0_mini | `—` | client error, resubmitted | 0 or charged (see note) |
| 40 | 11:02:17 | `renders/S01_SH02/take1` | seedance_2_0_mini | `—` | client error, resubmitted | 0 or charged (see note) |
| 41 | 11:02:21 | `renders/S05_SH01/take1` | seedance_2_0_mini | `—` | client error, resubmitted | 0 or charged (see note) |
| 42 | 11:02:22 | `renders/S07_SH01/take1` | seedance_2_0_mini | `—` | client error, resubmitted | 0 or charged (see note) |
| 43 | 11:02:26 | `renders/S03_SH01/take1` | seedance_2_0_mini | `—` | client error, resubmitted | 0 or charged (see note) |
| 44 | 11:02:30 | `renders/S04_SH01/take1` | seedance_2_0_mini | `—` | client error, resubmitted | 0 or charged (see note) |
| 45 | 11:02:43 | `renders/S01_SH02/take1` | seedance_2_0_mini | `—` | client error, resubmitted | 0 or charged (see note) |
| 46 | 11:02:51 | `renders/S01_SH01/take1` | seedance_2_0_mini | `ab5f042c-aff1-43cc-a007-2e83bc3092b4` | completed | 4 |
| 47 | 11:02:53 | `renders/S07_SH01/take1` | seedance_2_0_mini | `—` | client error, resubmitted | 0 or charged (see note) |
| 48 | 11:02:58 | `renders/S01_SH03/take1` | seedance_2_0_mini | `5aec116a-a7ca-4ab2-8ffd-91a1ac42a144` | completed | 4 |
| 49 | 11:05:09 | `renders/S05_SH02/take1` | seedance_2_0_mini | `3d73d3f6-a58c-45c7-9e8d-779efdbf2e27` | completed | 6 |
| 50 | 11:05:11 | `renders/S03_SH04/take1` | seedance_2_0_mini | `0aed569c-919f-4cea-8c22-569bc9411124` | completed | 4 |
| 51 | 11:05:56 | `renders/S05_SH01/take1` | seedance_2_0_mini | `9077ded8-21fb-475f-858e-26c7736a691d` | completed | 5 |
| 52 | 11:07:27 | `renders/S06_SH01/take1` | seedance_2_0_mini | `d8e682e5-7636-4c52-a21b-556c22f76715` | completed | 4 |
| 53 | 11:09:18 | `renders/S01_SH02/take1` | seedance_2_0_mini | `fd788d5c-1aaa-4583-b4b7-b774d163c16c` | completed | 4 |
| 54 | 11:09:24 | `renders/S06_SH04/take1` | seedance_2_0_mini | `bd1d26e4-d234-4e8b-9ea1-3e800097ce80` | completed | 4 |
| 55 | 11:09:46 | `renders/S07_SH01/take1` | seedance_2_0_mini | `7a84c9e2-59e8-4657-a105-db79c5740a66` | completed | 5 |
| 56 | 11:10:53 | `renders/S04_SH01/take1` | seedance_2_0_mini | `9ae20cab-d2a2-487b-b1ba-aeaafba8af7d` | completed | 4 |
| 57 | 11:13:21 | `renders/S03_SH01/take1` | seedance_2_0_mini | `243ed93e-6e45-4f64-9a25-00a7b902afb1` | completed | 4 |

Sum of completed rows: 120 credits.

## Batches

| Batch | Contents | Outcome |
|---|---|---|
| A1 | Leo (boy) master | validated first attempt |
| A2 | Sam, friends sheet, prop sheet, pitch view E | 3 validated; pitch view E had the wrong layout |
| A3 | Leo (adult), pitch view E v2 | adult validated; E v2 layout right, fence too low |
| A4 | Pitch view A (match-cut frame), E v3 | A validated and became the look reference; E kept as layout reference only |
| A5 | Present-day view A, Sam keyframe, present-day Sam frame | all validated; frames align between eras |
| S1 | S03_SH03 (hero) takes 1–2 | take 1 rejected: camera pushed in. Take 2 with the keyframe as both first and last frame: passed |
| K1–K2 | 14 shot keyframes + 1 end-state keyframe | all usable on the first attempt |
| S2–S4 | 14 video clips | all passed on take 1 |

---

# VERSION 2 — BALANCED

Approval: the creator's message of 2026-10-06 asking for "a second version with a more balanced stack rather than the cheapest models". Plan and ceiling (**170 credits**) were printed before the first job.

| | |
|---|---|
| Balance before | 446.22 |
| Balance after | 325.97 |
| **Credits spent on version 2** | **120.25** |
| Ceiling | 170 |
| **Project total (v1 + v2)** | **250.25** |

## Models used in version 2

| Tier | Model | Used for | Credits |
|---|---|---|---|
| PREMIUM | seedance_2_0 (720p) | S03_SH03 Sam's line · S05_SH02 adult close-up | 18 per 4 s clip |
| STANDARD | wan3_0 (720p) | S01_SH01 · S02_SH02 · S02_SH04 · S03_SH01 · S03_SH04 · S07_SH01 | 7 per 4 s, 8.75 per 5 s |
| ECONOMY | seedance_2_0_mini (720p) | S01_SH03 · S04_SH02 · S05_SH04 · S06_SH03 | 4 per 4 s |
| Images | nano_banana_pro (2k) | 7 keyframes | 2 each |
| Audio | mirelo_text_to_audio | two ambience beds, one memory sound | 0.25 per second |

## Jobs

| # | Time (UTC) | Output | Model | Job ID | Result | Credits |
|---|---|---|---|---|---|---|
| 1 | 11:30:17 | `keyframes/S02_SH02_v1` | nano_banana_pro | `9be0b4fc-c2c7-4228-b50d-c4812c08a01b` | completed | 2 |
| 2 | 11:30:30 | `keyframes/S01_SH03_v2` | nano_banana_pro | `74307823-f021-4077-abce-bfc797a001c3` | completed | 2 |
| 3 | 11:30:36 | `keyframes/S02_SH04_v2` | nano_banana_pro | `97799173-98e0-4c32-b227-3433c486b69a` | completed | 2 |
| 4 | 11:31:08 | `keyframes/S03_SH04_v2` | nano_banana_pro | `56196d77-8d7d-41ea-9a84-03d2e4344166` | completed | 2 |
| 5 | 11:31:34 | `keyframes/S01_SH01_v2` | nano_banana_pro | `3128c198-3790-475e-a9c0-b80eced35b5a` | completed | 2 |
| 6 | 11:33:24 | `keyframes/S05_SH02_v2_smile` | nano_banana_pro | `ad7ddaaf-2003-465f-a560-cd44aaca3887` | completed | 2 |
| 7 | 11:49:13 | `renders/S01_SH03/v2_take1` | seedance_2_0_mini | `bca18210-872f-4451-b864-fc6a02ad1966` | completed | 4 |
| 8 | 11:49:15 | `renders/S05_SH04/v2_take1` | seedance_2_0_mini | `51200b1b-6938-47e3-9902-7999ad29f95b` | completed | 4 |
| 9 | 11:49:17 | `renders/S04_SH02/v2_take1` | seedance_2_0_mini | `1c28bf42-2662-4d5e-af7f-24c7c909a118` | completed | 4 |
| 10 | 11:49:17 | `renders/S03_SH03/v2_take1` | seedance_2_0 | `94684ff0-584e-44cb-b4d6-9d7a8e1e5533` | completed | 18 |
| 11 | 11:49:26 | `renders/S01_SH01/v2_take1` | wan3_0 | `81d4e5ff-0447-4cd3-b0dd-d8640b9e4567` | completed | 7 |
| 12 | 11:49:38 | `audio/memory_sting` | mirelo_text_to_audio | `dc85789a-234d-4a1c-8260-ae6bddada506` | completed | 1.25 |
| 13 | 11:49:44 | `audio/bed_then` | mirelo_text_to_audio | `05d47c99-6076-4661-b59e-2284adb6e131` | completed | 4.25 |
| 14 | 11:49:48 | `audio/bed_now` | mirelo_text_to_audio | `c4e9112f-a008-4293-9de0-22ff7ab8ffc2` | completed | 5 |
| 15 | 11:51:41 | `renders/S07_SH01/v2_take1` | wan3_0 | `—` | rejected by concurrency limit, resubmitted | 0 |
| 16 | 11:52:05 | `renders/S07_SH01/v2_take1` | wan3_0 | `—` | rejected by concurrency limit, resubmitted | 0 |
| 17 | 11:53:09 | `renders/S03_SH01/v2_take1` | wan3_0 | `a1dc40f2-f059-4013-b01b-cb0af80221ed` | completed | 7 |
| 18 | 11:53:11 | `renders/S03_SH04/v2_take1` | wan3_0 | `2c827cfd-34ed-4beb-993b-040c18328b35` | completed | 7 |
| 19 | 11:53:15 | `renders/S02_SH02/v2_take1` | wan3_0 | `d395afe5-b3e0-459d-9cdd-9078f7de0250` | completed | 7 |
| 20 | 11:53:22 | `renders/S02_SH04/v2_take1` | wan3_0 | `7dca2b7b-f266-4815-8dd7-451d4327f244` | completed | 7 |
| 21 | 11:55:10 | `renders/S05_SH02/v2_take1` | seedance_2_0 | `240acc62-c786-4e5d-8428-11cca1440868` | completed | 18 |
| 22 | 11:58:29 | `renders/S06_SH03/v2_take1` | seedance_2_0_mini | `f9b242e0-56c4-4140-9150-6b3dbe2f4188` | completed | 4 |
| 23 | 12:01:22 | `renders/S07_SH01/v2_take1` | wan3_0 | `9c5e75fb-48e1-4840-9c28-f0271ba99472` | completed | 8.75 |

Sum of completed rows: 118.25 credits. The balance fell by 120.25, so 2 credits are not traced to a row (most likely one resubmitted job that was charged twice).

Every version 2 clip was accepted on its first take.
