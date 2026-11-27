# My brain

A folder an LLM reads before it answers you. You own every file in it, and you can read every file in it.

It is the same shape as the [100x brain](https://github.com/Siddhant-Goswami/100x-brain), which holds what Cohort 8 has been taught. Yours holds what the course will never know: you.

## Start here (20 minutes)

1. **Copy it.** Click "Use this template" on GitHub, or download the zip. Open the folder in the tool you already use: Antigravity, Claude Code, Codex or Cursor.
2. **Write `me.md`.** By hand, in your own words. Your North Star goes in it.
3. **Give it one source.** Put one document you own into `raw/` (your notes, an article, a transcript, as a text or markdown file). Then say: `Take in the new file in raw/.` Read what it wrote in `wiki/`, and click one of its source links.
4. **Tell it one fact.** Say: `Save this in wiki/told.md: ...` Open the file and check the line is there. Close the chat, open a new one, and ask for the fact.
5. **Write three questions** in `eval/questions.md`: three questions whose answers you know. One of them is something it should say "not known" to. Score them.

No tool that opens a folder? Do steps 2, 4 and 5 with one file: paste `me.md` at the top of a new chat. That is `memory.txt` from Lecture 6, and it still counts.

## What is in the folder

| Path | What it is | Who writes it |
| --- | --- | --- |
| `AGENTS.md` | The rules. Your tool reads them first | You |
| `me.md` | Who you are and where you are going | You, never the LLM |
| `now.md` | What you are working on this week | You |
| `index.md` | One line per page. Read first, every time | The LLM |
| `log.md` | One dated line per change | Whoever made the change |
| `raw/` | Your sources, kept as they came. Never edited | You put them in |
| `wiki/` | Pages the LLM writes from your sources. Every line names its source | The LLM, and you read them |
| `notes/` | Your own notes | You, never the LLM |
| `eval/questions.md` | Three questions with known answers, and the marks | You |

## The week

- Use it for **one job only**. `now.md` starts with one: keep me up to date for my North Star.
- **Each day:** put one thing you saved into `raw/`, say `Take in the new file in raw/.`, then ask `Is this worth my time?` Add one line to `log.md`: what it said, and whether you agree.
- Once in the week, **find one line that is wrong** or out of date. Replace it and keep the old line, marked.
- A week after you start, open a new chat and **ask for the fact** from step 4.

`python3 tools/check.py` tells you which of these are done.

## Questions about the course

Your brain does not copy the course notes. It asks the 100x brain, at this address:

```
https://100x-curriculum.vercel.app/api/brain
```

Claude Code and Cursor pick the address up from this folder. In any other app, add it the way you added the sheet's server in Lecture 11.
