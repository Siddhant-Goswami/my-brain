# My brain

A folder an LLM reads before it answers you. You own every file in it, and you can read every file in it.

It is the same shape as the [100x brain](https://github.com/Siddhant-Goswami/100x-brain), which holds what Cohort 8 has been taught. Yours holds what the course will never know: you.

## Start here (20 minutes)

You need a text editor and any chat with an LLM. Nothing else. You carry the files to the LLM and back.

1. **Get the folder.** Download the zip and unzip it, or click "Use this template" on GitHub. Open the files in any editor: Notepad, TextEdit, or the one you code in.
2. **Write `me.md`.** By hand, in your own words. Your North Star goes in it.
3. **Start a chat and tell it one fact.** Open a new chat. Paste all of `AGENTS.md` and send. It asks for three files; paste them. Then say: `Today is [date]. Save this in wiki/told.md: ...` It gives you a line and the file it goes in. Paste the line into the file yourself, and save.
4. **Open a new chat and ask twice.** Once with nothing pasted. Once after pasting `AGENTS.md` and the files it asks for. The second answer comes from a file you can open.
5. **Give it one source.** Save one document you own as a text file in `raw/` (an article, a post, your notes). Paste it and ask: `Is this worth my time?` Then say: `Take in raw/[name].` It writes a page, an index line and a log line. Read them, then paste each where it says.
6. **Write three questions** in `eval/questions.md`: three questions whose answers you know. One of them is something it should say "not known" to. Score them: "Before" is a new chat with nothing pasted, "After" is with your files.

Already use a tool that opens folders (Antigravity, Claude Code, Codex or Cursor)? Open this folder in it and say the same sentences. The rules are the same. The tool does the carrying.

## What is in the folder

| Path | What it is | Who writes it |
| --- | --- | --- |
| `AGENTS.md` | The rules. Pasted first into every new chat, or read by your tool | You |
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
- **Each day:** save one thing in `raw/`, paste it into a chat that has your files, and ask `Is this worth my time?` Add one line to `log.md`: what it said, and whether you agree.
- Once in the week, **find one line that is wrong** or out of date. Replace it and keep the old line, marked.
- A week after you start, open a new chat and **ask for the fact** from step 4.

If you have Python, `python3 tools/check.py` ticks off which of these are done.

## Questions about the course

Your brain does not copy the course notes. It asks the [100x brain](https://github.com/Siddhant-Goswami/100x-brain).

- **By hand:** paste the 100x brain's `index.md` into your chat with your question. The LLM names a page. Open that page, paste it, and it answers.
- **In a tool that takes an address:** Claude Code and Cursor pick this one up from the folder. In any other app, add it the way you added the sheet's server in Lecture 11.

```
https://100x-curriculum.vercel.app/api/brain
```
