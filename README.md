# Animation Studio

An agent-driven pipeline for Claude Code that turns a script into a finished animated episode, with an approval gate before any paid generation.

**Case study:** [https://niccolas-farani.pages.dev/work/ai-animation-production-agent](https://niccolas-farani.pages.dev/work/ai-animation-production-agent/)

![Animation Studio preview](docs/media/preview.webp)

---

## Install
1. Unzip anywhere, then:  cd animation-studio  &&  claude
2. Claude Code loads CLAUDE.md automatically. Slash commands in .claude/commands/ appear when you type /.
3. Higgsfield (one-time, in your normal terminal):
   npm install -g @higgsfield/cli
   higgsfield auth login
   npx skills add higgsfield-ai/skills    # optional

## Pipeline
   /develop <slug>        story notes only
   /make <slug>           PRE-PRODUCTION blueprint → stops. No prompts, no credits.
   /assets <slug>         master asset specs in approval batches
   /generate <slug> batch 1   shows cost summary → waits for your "approved" → runs that batch only
   /prompts <slug> S01    shot prompts (only once that scene's assets are approved)
   /generate <slug> S01   same approval gate, for shots
   /qa <slug>   /fix <slug> S03_SH07 <what went wrong>   /edit <slug>
   /status <slug>         where am I, what's next, credits spent
   /revise-production <slug> <feedback>

## One-command production
   /make <slug>           review the blueprint if you want
   /produce <slug>        runs everything after /make: assets → prompts → shots → QA → fixes → edit package

   /produce <slug> economy | balanced (default) | quality
   /produce <slug> budget=300        hard cap in credits
   /produce <slug> budget=low|medium|high   size of the retry allowance

/produce shows one production estimate, then proceeds without asking per batch. It stops by itself if the
spend ceiling or your balance would be exceeded. Run it again to resume; it never redoes finished work.

With the staged commands, nothing spends credits without you approving that specific batch.
Running /produce is your approval for that film's whole pipeline, up to the spend ceiling.

## Key files
- STYLE_BIBLE.md — the channel's house style. Grows from what you approve and reject.
- adapters/higgsfield.md — what Higgsfield can actually do and which models map to Economy / Standard / Premium. Starts UNVERIFIED; the agent fills it in as it confirms things.
- projects/<slug>/STATUS.md — current stage of each film.
- projects/<slug>/11_shot_list.md — the master shot spec. Tool prompts are adapters of it, so you can switch models later without replanning.

## Start a film
Copy projects/_example-film to projects/<your-slug>, fill in 00_source/idea_and_script.md, then /make <your-slug>.
