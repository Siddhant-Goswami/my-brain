# The rules

This folder is my brain: what I know, what I want and what I have decided, as plain files.
Any tool that opens this folder follows these rules.

1. Read `me.md`, `now.md` and `index.md` first, every time.
2. Never change a file in `raw/`. Those are my sources, kept as they came.
3. Never write in `notes/` or `me.md`. Those are mine. If you think one should change, say what you would change and wait for me.
4. You write in `wiki/`. Every line you write ends with the file it came from, in `raw/` or `notes/`. No source, no line.
5. Date every write. When a line stops being true, do not erase it. Add the new line and mark the old one: `Replaced on 2026-12-01.`
6. Save only what will still matter next week. If you are not sure, ask me.

## How to do the common jobs

- **"Take in the new file in raw/."** Read it. Write one short page in `wiki/` (one fact per line, each ending with its source file). Add one line for the page to `index.md`. Add one dated line to `log.md`. Then tell me what you wrote and where.
- **"Save this in wiki/told.md: ..."** Add it to `wiki/told.md` in this folder, as one line with today's date, ending with `(told by me)`. Add a dated line to `log.md`. Do the same when I say "remember this". Do not put it in your own built-in memory instead: I must be able to open the file here and read it.
- **"Is this worth my time?"** Read `me.md` and `now.md` first. Answer yes or no for my North Star, in one line. Then give one reason: quote my North Star, and quote one line from the source. If `me.md` has no North Star, say so and stop. Do not praise the source.
- **A question.** Answer from the files in this folder and name the file. If my files do not hold the answer, say "not known". Do not guess.
- **Something looks wrong or out of date.** Tell me. Change it only after I say yes, following rule 5.

## The course

Questions about the 100xEngineers course (a lecture, a date, a due date, an idea) are answered by the 100x brain, not from your own memory.
Its address is `https://100x-curriculum.vercel.app/api/brain`, with three tools: `read_index`, `open_page`, `search`.
If that address is not connected in this tool, say so.
