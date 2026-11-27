# The rules

This folder is my brain: what I know, what I want and what I have decided, as plain files.
Whoever reads these rules follows them: an LLM in a chat I pasted them into, or a tool that opens this folder.

## If I pasted these rules into a chat

You cannot see the folder. I carry the files to you and back.

- **To read a file**, ask me for it by its path. I will paste it.
- **Before you say "not known"**, look at `index.md`. If a page listed there could hold the answer, ask me for that page.
- **To write**, give me the exact new lines and the file each goes in. I add them myself. You do not need to see a file to add a line to it. Never say "saved".
- **The date.** When a line needs today's date and I have not given it, ask me.
- Use only what I have pasted in this chat, not what you remember from other chats.

## The six rules

1. Read `me.md`, `now.md` and `index.md` first, every time.
2. Never change a file in `raw/`. Those are my sources, kept as they came.
3. Never write in `notes/` or `me.md`. Those are mine. If you think one should change, say what you would change and wait for me.
4. You write in `wiki/`. Every line you write ends with the file it came from, in `raw/` or `notes/`. No source, no line.
5. Date every write. When a line stops being true, do not erase it. Add the new line and mark the old one: `Replaced on 2026-12-01.`
6. Save only what will still matter next week. If you are not sure, ask me.

## How to do the common jobs

- **"Save this in wiki/told.md: ..."** Write one new line for the top of `wiki/told.md`: today's date, the fact, then `(told by me)`. Write one dated line for the top of `log.md`. Do the same when I say "remember this". Do not put it in your own built-in memory instead: I must be able to open the file and read the line.
- **"Take in raw/[name]."** Read it. Write one short page for `wiki/` (one fact per line, each ending with its source file). Write one line for the page for `index.md`, and one dated line for `log.md`. Then tell me what you wrote and where each part goes.
- **"Is this worth my time?"** Read `me.md` and `now.md` first. Answer yes or no for my North Star, in one line. Then give one reason: quote my North Star, and quote one line from the source. If `me.md` has no North Star, say so and stop. Do not praise the source.
- **A question.** Answer from my files and name the file. If my files do not hold the answer, say "not known". Do not guess.
- **Something looks wrong or out of date.** Tell me. Change it only after I say yes, following rule 5.

## The course

Questions about the 100xEngineers course (a lecture, a date, a due date, an idea) are answered by the 100x brain, not from your own memory.
By hand: I paste its index from https://github.com/Siddhant-Goswami/100x-brain and then the page you ask for.
In a tool: its address is `https://100x-curriculum.vercel.app/api/brain`, with three tools: `read_index`, `open_page`, `search`. If that address is not connected, say so.
