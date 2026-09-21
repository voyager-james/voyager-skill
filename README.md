# Voyager Copy (Codex plugin)

Interview-first copywriting for Facebook ads, emails and newsletters, and landing pages. Ask for a deliverable and the agent asks the questions that fit your goal, confirms a summary, then writes the copy.

## Skills

| Skill | Use it for | Call it |
|---|---|---|
| `fb-ad-copy` | Facebook and Instagram ad packages (1 primary text, 5 headlines, 1 description, CTA, plus a 30-hook batch for video) | `$fb-ad-copy` |
| `email-newsletter` | Newsletters, promo emails, welcome, nurture, launch and re-engagement sequences | `$email-newsletter` |
| `landing-page` | Opt-in, webinar registration, book-a-call, sales and thank-you pages, with form spec and build notes | `$landing-page` |
| `copy-foundations` | Shared interview rules, copy principles and the human-voice linter. Also usable alone to lint any copy | `$copy-foundations` |

You can also just ask in plain language ("write a Facebook ad for my coaching offer") and Codex picks the skill.

## How it works

1. **Use what is already known.** The agent reads your request, the conversation and your project instructions first. It does not ask for anything that is already there. If your project tells Codex to read a brand folder first, keep doing that. The plugin does not manage brand context.
2. **Round 1.** 3 to 5 questions with lettered options. Reply in shorthand, for example `1b, 2a, 3: free audit call, 4 skip`.
3. **Round 2.** Only the follow-ups your answers trigger (for example: lead magnet details for a leads campaign, price and guarantee for a sales campaign).
4. **Confirmation summary.** The agent shows what it will write and waits for a yes.
5. **Write, check, deliver.** Copy is checked against the skill's checklist, Meta ad policy (ads) and the human-voice linter (no em-dashes, en-dashes or AI-tell phrases).

Maximum two question rounds. You can always answer `skip` or `you decide`.

## What each interview asks

**Facebook ads:** goal (leads, sales, webinar registrations, book a call, awareness, traffic), audience temperature, offer and next step, format. Then goal-specific follow-ups, tone framework, proof and compliance.

**Email and newsletter:** type, goal, recipients and warmth, topic and the one action. Then sequence timing, newsletter format, promo details, sender voice and length.

**Landing page:** page type, traffic source, offer and conversion action, platform. Then proof, objections, structure, form length and legal extras.

## Install from GitHub (private repo)

Prerequisite: your machine can clone the repo (GitHub CLI logged in with `gh auth login`, or git credentials saved).

```bash
codex plugin marketplace add <owner>/<repo>
```

Then open Codex, go to Plugins, and install **Voyager Copy** from the **Voyager Agency Plugins** marketplace.

If the direct add fails on a private repo, clone it first and add the local folder:

```bash
git clone https://github.com/<owner>/<repo>.git
codex plugin marketplace add ./<repo>
```

To update later: `git pull`, then reinstall or refresh the plugin in Codex and start a new thread.

## Requirements

- Codex with plugin support.
- Python 3 for the human-voice linter. Without Python the agent falls back to a manual dash and phrase check.

## Repository layout

```
.agents/plugins/marketplace.json     marketplace entry (what `codex plugin marketplace add` reads)
plugins/voyager-copy/
  .codex-plugin/plugin.json          plugin manifest
  skills/
    fb-ad-copy/                      SKILL.md + references/ (interview, ad rules, Meta compliance, hooks)
    email-newsletter/                SKILL.md + references/ (interview, email rules)
    landing-page/                    SKILL.md + references/ (interview, page blueprints)
    copy-foundations/                SKILL.md + references/ (interview protocol, principles, ai_tells.txt) + scripts/lint_copy.py
```

## Adding a new deliverable skill

1. Copy an existing skill folder and rename it.
2. Write `references/interview.md` first: Round 1 questions, Round 2 triggers, required fields, summary template.
3. Add the rules in `references/`, and a routing table in `SKILL.md` that maps answers to copy decisions.
4. Point the skill at `../copy-foundations/` for the protocol, principles and quality gate.

## Brand-specific banned words

Keep client-specific phrase lists out of this repo. Pass them at lint time:

```bash
python plugins/voyager-copy/skills/copy-foundations/scripts/lint_copy.py draft.md --tells-file my_client_tells.txt
```
