---
name: youtube-transcript
description: Turn a YouTube video into a clean, readable transcript with provenance. Use whenever the user gives a YouTube URL and wants the transcript, the text, a summary, quotes, notes, or wants the video mined for research — and whenever a task needs the contents of a video rather than its metadata. Handles caption download, roll-up de-duplication, and the readability pass.
---

# YouTube transcript

`scripts/fetch_transcript.py` does the mechanical half: downloads the caption
track, strips VTT scaffolding, removes the roll-up duplication in
auto-captions, and writes markdown with a provenance header. You do the half
that needs judgement.

## Run it

```bash
python3 ~/.claude/skills/youtube-transcript/scripts/fetch_transcript.py "<url>" -o transcript.md
```

Useful flags:

- `--lang de` — a different caption language (default `en`)
- `--every 120` / `--every 0` — seconds per timestamped block; `0` gives one blob
- `--no-timestamps` — drop the `[m:ss]` markers
- `--list-langs` — show which tracks the video actually has
- `--cookies-from-browser chrome` — for age-gated videos, or when YouTube
  throws a bot check at an unauthenticated request

Write to a file rather than stdout for anything over ~10 minutes. An hour of
speech is roughly 9,000 words, and you rarely want all of it in context at
once — the script prints the word count to stderr so you can decide before
reading.

## Then do the readability pass

The script deliberately does not rewrite anything. Read the file first and
see what you actually got — auto-caption quality varies, so decide from the
text in front of you rather than from an assumption about it.

1. **Check the header.** If it says auto-generated, treat every proper noun,
   number, and technical term as suspect. This is the reliable failure mode:
   names, products, and homophones come back confidently wrong, and they come
   back wrong the same way every time.
2. **Check whether it needs repunctuating at all.** Some auto-captions arrive
   as lowercase unpunctuated streams; others arrive with sentence breaks,
   speaker-change markers (`>>`) and sound events (`[applause]`, `[Music]`)
   already in place. If punctuation is missing, add it — sentence boundaries,
   capitalisation, paragraph breaks at topic shifts. If it is already there,
   leave it alone and spend the effort on artefacts instead.
3. **Fix artefacts, and list what you fixed.** Wrong proper nouns,
   homophone substitutions, mis-classified sound tags. Append a short cleanup
   note to the file recording each class of change, so a reader can tell your
   edits from the source. Keep the timestamp markers throughout; they are how
   anyone gets back to the moment in the video.
4. **Do not smooth the speech.** Fix transcription artefacts, not the
   speaker. Filler words, false starts, and broken grammar are data — if the
   user is mining the video for voice, register, or phrasing, sanding it into
   clean prose destroys the thing they came for. Say so if asked to.
5. **Flag what you could not resolve.** An obviously-garbled name is worth a
   `[?]` rather than a confident guess, and anything picked up off-mic
   (audience questions especially) deserves saying so explicitly.

## When there are no captions

Some small channels disable them. The script exits saying so. Options, in
order of effort:

- `--list-langs` first — there may be a track in another language, and a
  translated transcript beats none.
- Local speech-to-text: `brew install openai-whisper` (or `uv tool install`),
  then pull audio with
  `yt-dlp -x --audio-format mp3 -o audio.mp3 "<url>"` and run
  `whisper audio.mp3 --model small --output_format srt`. Slow, runs fine on
  Apple silicon, and produces punctuated output — but it is a real install and
  a real wait, so confirm with the user before starting.

## Quoting

The header carries channel, URL, upload date, and caption type. Keep it
attached to any excerpt that leaves this machine. Quote sparingly and
attribute — a transcript is a research input, not redistributable content,
and auto-captions are not accurate enough to put in quotation marks against
someone's name without checking the audio.

## How much to trust the above

The guidance here comes from four videos (2026-08-01): two human-captioned,
two auto-captioned. Both auto-captioned ones arrived already punctuated with
sound events, and both mangled proper nouns — but two samples is not enough
to know how caption quality varies with video age, language, channel size, or
whether YouTube has reprocessed an old upload. Treat "check what you actually
got" as the rule and everything else as a prior. If you hit a video that
contradicts this, correct the file.

## Maintenance

YouTube breaks extractors regularly. If downloads start failing with
extraction errors, update first: `yt-dlp -U`. The binary lives at
`~/.local/bin/yt-dlp` (standalone build — Homebrew was not used, its
directory permissions are broken on this machine).
