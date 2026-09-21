# Interview Protocol

Shared by `fb-ad-copy`, `email-newsletter` and `landing-page`. The goal is to collect just enough to write copy that fits the request, then write it. Never write first and ask later.

## 1. Use what you already know

Before asking anything, scan the user's request, the conversation, attached files and the project instructions for answers (offer, audience, brand voice, proof, banned words, tone). Treat anything you find as answered and never re-ask it.

If the project instructions tell you to read a brand or guidelines folder first, do that and apply it. This plugin does not load brand context itself, and it must not ask the user to repeat what that context already says.

## 2. Ask in rounds

- **Round 1:** 3 to 5 questions, always the ones listed in the skill's `references/interview.md`.
- **Round 2:** only the follow-ups that the Round 1 answers trigger. Ask 3 to 5 at most.
- **Two rounds maximum.** If a required field is still missing after Round 2, write a clearly labelled assumption instead of opening a third round.
- Number the questions. Give lettered options where the skill provides them.
- Tell the user they can reply in shorthand, for example: `1b, 2a, 3: free audit call, 4 skip`.
- Always allow `skip` and `you decide`. "You decide" means pick the recommended default and tell the user what you picked.
- Skip any question the user has already answered.
- Ask in plain chat text. Do not start writing until the summary in step 4 is confirmed.

## 3. Readiness gate

Each skill lists its required fields. You are ready when every required field has an answer or a labelled assumption. Nice-to-have fields never block writing.

## 4. Confirmation summary

Before generating, post a short summary of 4 to 8 lines covering: the deliverable, the goal, the audience and temperature, the offer and the action, the angle or tone you will use, and any assumptions. End with:

> Reply **yes** to write it, or tell me what to change.

Wait for the answer. If the user changes something material (goal, audience, offer, format), update the summary and confirm once more. Small tweaks do not need a second confirmation.

## 5. Generate, gate, deliver

1. Generate the copy using the skill's references and the answers.
2. Run the quality gate in `copy-foundations/SKILL.md` (human-voice lint plus the skill's own checklist).
3. Deliver the copy first. After it, add a short **Assumptions** list (only if you made any) and **QA notes** (only if there is something the user must act on, such as a Special Ad Category flag).
4. Offer two or three next steps, such as more variations, a shorter cut, or a different angle.

**Saving:** if the project instructions say where deliverables go, follow them. Otherwise deliver in chat and offer to save as `YYYY-MM-DD_<type>_<descriptor>.md`. The linter needs a file, so write the draft to that file (or a temp file) before running it.

## 6. Interview style

Short, plain and friendly. No lectures on copywriting theory. Explain a question in one line only if the user is likely to be unsure. Recommend a default when it helps ("Most cold ads do best with a 6-beat text, want me to pick?").
