# Learn AI the Right Way

Source for the YouTube channel **Learn AI the Right Way** ([@LearnAItheRightway](https://www.youtube.com/@LearnAItheRightway)): a beginner-first AI course presented by Ria, with Arjun, an FAQ mentor bot.

Launched 21 November 2026 with a Start Here video and Lessons 1–3. Course 0 (Linux basics, Lessons 1–5) is scripted and waiting for voice recording.

## What's here

| Folder | Contents |
|---|---|
| `pipeline/` | Video build tools: `deckkit.py` (slides with Ria), `align.py` (caption alignment), `render_lesson.py` (captions, chapters, transitions), screenshot helper |
| `ria/` | Ria presenter artwork (SVG) |
| `catalogue/` | Course catalogue page and curriculum data |
| `start-here/` | Start Here orientation video: deck, narration, chapters |
| `lessons/lesson-0N/` | Lessons 1–3: deck builders, narration, chapters, thumbnails source |
| `course-0/` | Course 0 Lessons 1–5 (Linux basics): slides, narration, labs, quizzes, FAQs, generated lesson pages and YouTube details |
| `arjun/` | Ask Arjun mentor page: template, FAQ bank (`faq.json`), voice lines and clips |
| `pages/` | Entrance quiz and lesson quiz pages |
| `launch/` | Launch go/no-go checklist and YouTube descriptions |
| `tracker/` | Google Apps Script for the learner and revenue tracker (`Tracker.gs`) |

## Not in this repo (on purpose)

- Rendered videos, lesson voice audio and slide PNGs: too large, rebuilt from source. Masters live in Google Drive.
- Learner data, form responses and payment records.
- Any API keys. Razorpay keys live only in the Apps Script project's Script Properties.

## Rebuilding a lesson video

1. `python build_deck.py` in the lesson folder renders the slides (Playwright).
2. Record narration in ElevenLabs (voice Bella) as `part1/2/3.mp3` from `voice_paste.txt` / `narr.json`.
3. `python pipeline/align.py` then `python pipeline/render_lesson.py` produces the MP4 with captions and chapters.
