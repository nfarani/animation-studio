# tools/

Helpers used by the production agent. Kept in the repo so they survive between sessions.

- `ffmpeg` — symlink to a bundled ffmpeg inside `.venv` (no system install needed). Rebuild: `python3 -m venv tools/.venv && tools/.venv/bin/pip install imageio-ffmpeg pillow numpy faster-whisper`, then re-link.
- `gen.sh <project dir> <out path> <model> [params]` — one Higgsfield job: submit, wait, download, log. Recovers jobs that were created despite a submission error.
- `montage.py <out.jpg> <columns> <images...>` — contact sheet for review.
- `speech.py <ffmpeg> <media...>` — word-level transcript with timings (checks that no line is cut).
- `jumps.py <ffmpeg> <clips...>` — finds frames where the background changes abruptly.
- Each episode's own `edit/build_cut.py` builds the cut from its edit list.
