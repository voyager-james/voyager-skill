---
name: copy-foundations
description: Shared foundations for the Voyager Copy plugin. Holds the interview protocol, the core conversion-copywriting principles, and the human-voice quality gate (a linter that catches em-dashes, en-dashes and AI-tell phrases). Load it whenever fb-ad-copy, email-newsletter or landing-page runs. Also use it directly to lint, humanize or sanity-check any customer-facing copy such as ads, emails, social posts, headlines and CTAs before delivery.
---

# Copy Foundations

Shared by the three deliverable skills. It has three parts.

| Part | File | Used for |
|---|---|---|
| Interview protocol | `references/interview-protocol.md` | How to ask questions, when to stop, the confirmation summary |
| Core principles | `references/copy-principles.md` | Hooks, pain language, funnel stage, CTA friction, clarity |
| Quality gate | this file + `scripts/lint_copy.py` | Human-voice pass before anything is delivered |

Read the interview protocol first, then the principles, then follow the deliverable skill.

## Quality gate

Run this on every deliverable, after the skill's own checklist and before delivery.

1. **Manual pass.** Replace every em-dash and en-dash with a comma, period, colon or a restructured sentence. Ordinary hyphens in compounds such as `high-converting` stay.
2. **Replace AI-tell phrases** with concrete, context-specific wording. Do not delete a phrase if that leaves a gap in meaning or tone. The phrase list is `references/ai_tells.txt`.
3. **Fix robotic cadence** the linter cannot see: repeated sentence shapes, generic claims, forced enthusiasm, stacked rhetorical questions, copy any brand in the category could have written.
4. **Run the linter** on the saved draft. Resolve the script path relative to this SKILL.md:

   ```powershell
   python scripts/lint_copy.py path/to/draft.md
   ```

   Options: `--json` for structured output, `--tells-file <path>` for a client-specific phrase list, `--no-tells` to check dashes only, `--ext .md,.txt,.html` for folder scans.
5. Fix every finding and rerun until the exit code is 0. Report any deliberate exception to the user.

Keep verbatim customer quotes, code, URLs and file paths as they are. If Python is unavailable, search the copy for the Unicode dashes and compare it against `references/ai_tells.txt` by hand.

## Standalone use

If the user only wants existing copy checked or humanized, skip the interview. Run the quality gate, return the fixed copy, and list what changed.

## Adding brand-specific banned words

Create a copy of `references/ai_tells.txt`, add one phrase per line, and pass it with `--tells-file`. Keep client-specific lists outside this plugin.
