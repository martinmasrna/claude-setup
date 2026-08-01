#!/usr/bin/env python3
"""Pull a YouTube caption track and turn it into readable markdown.

Mechanical work only: fetch, strip VTT scaffolding, undo the roll-up
duplication YouTube's auto-captions are full of. Repunctuating the result is
a judgement call and stays with the agent.
"""

import argparse
import html
import json
import re
import subprocess
import sys
import tempfile
from collections import deque
from pathlib import Path

CUE_TIME = re.compile(
    r"^(\d{2}:\d{2}:\d{2}\.\d{3})\s+-->\s+(\d{2}:\d{2}:\d{2}\.\d{3})"
)
INLINE_TAG = re.compile(r"<[^>]+>")


def run_ytdlp(args):
    proc = subprocess.run(
        ["yt-dlp", *args], capture_output=True, text=True, check=False
    )
    if proc.returncode != 0:
        sys.exit(f"yt-dlp failed:\n{proc.stderr.strip()}")
    return proc.stdout


def download(url, lang, outdir, auto, extra):
    """Fetch one caption track. Returns the .vtt path, or None if absent."""
    flag = "--write-auto-subs" if auto else "--write-subs"
    run_ytdlp(
        [
            "--skip-download",
            "--no-playlist",
            "--no-write-subs" if auto else "--no-write-auto-subs",
            flag,
            "--sub-langs",
            lang,
            "--sub-format",
            "vtt",
            "--write-info-json",
            "-o",
            str(outdir / "video.%(ext)s"),
            *extra,
            url,
        ]
    )
    found = sorted(outdir.glob("*.vtt"))
    return found[0] if found else None


def parse_vtt(path):
    """VTT cues -> [(start_seconds, line)], roll-up repeats removed."""
    lines_out = []
    recent = deque(maxlen=4)
    start = None

    for raw in path.read_text(encoding="utf-8").splitlines():
        stripped = raw.strip()
        match = CUE_TIME.match(stripped)
        if match:
            start = to_seconds(match.group(1))
            continue
        if not stripped or stripped.startswith(("WEBVTT", "Kind:", "Language:", "NOTE")):
            continue
        if start is None:
            continue

        text = html.unescape(INLINE_TAG.sub("", stripped)).strip()
        if not text or text in recent:
            continue
        recent.append(text)
        lines_out.append((start, text))

    return lines_out


def to_seconds(stamp):
    hours, minutes, seconds = stamp.split(":")
    return int(hours) * 3600 + int(minutes) * 60 + float(seconds)


def to_stamp(seconds):
    seconds = int(seconds)
    hours, remainder = divmod(seconds, 3600)
    minutes, secs = divmod(remainder, 60)
    return f"{hours}:{minutes:02d}:{secs:02d}" if hours else f"{minutes}:{secs:02d}"


def chunk(lines, every):
    """Group lines into blocks, each tagged with the time it starts."""
    blocks = []
    current, anchor = [], None
    for start, text in lines:
        if anchor is None:
            anchor = start
        current.append(text)
        if every and start - anchor >= every:
            blocks.append((anchor, " ".join(current)))
            current, anchor = [], None
    if current:
        blocks.append((anchor or 0, " ".join(current)))
    return blocks


def render(info, blocks, auto, lang, show_stamps):
    duration = info.get("duration")
    header = [
        f"# {info.get('title', 'Untitled')}",
        "",
        f"- **Channel:** {info.get('uploader', 'unknown')}",
        f"- **URL:** {info.get('webpage_url', '')}",
        f"- **Uploaded:** {format_date(info.get('upload_date'))}",
        f"- **Duration:** {to_stamp(duration) if duration else 'unknown'}",
        f"- **Captions:** {'auto-generated' if auto else 'human-written'} ({lang})",
        "",
    ]
    if auto:
        header += [
            "> Auto-generated captions. Proper nouns, product names and",
            "> homophones come back confidently wrong; punctuation quality",
            "> varies by video. Verify any name or figure against the video",
            "> before quoting it.",
            "",
        ]
    header.append("---")
    header.append("")

    body = []
    for start, text in blocks:
        if show_stamps:
            body.append(f"**[{to_stamp(start)}]** {text}")
        else:
            body.append(text)
        body.append("")
    return "\n".join(header + body)


def format_date(raw):
    if not raw or len(raw) != 8:
        return "unknown"
    return f"{raw[:4]}-{raw[4:6]}-{raw[6:]}"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("url")
    parser.add_argument("--lang", default="en", help="caption language (default: en)")
    parser.add_argument("-o", "--output", help="write here instead of stdout")
    parser.add_argument(
        "--every",
        type=int,
        default=60,
        help="seconds per timestamped block, 0 for one blob (default: 60)",
    )
    parser.add_argument(
        "--no-timestamps", action="store_true", help="omit the [m:ss] markers"
    )
    parser.add_argument(
        "--list-langs", action="store_true", help="show available tracks and exit"
    )
    parser.add_argument(
        "--cookies-from-browser",
        metavar="BROWSER",
        help="use browser cookies (chrome, safari, firefox) for age-gated "
        "videos or bot checks",
    )
    args = parser.parse_args()

    extra = []
    if args.cookies_from_browser:
        extra += ["--cookies-from-browser", args.cookies_from_browser]

    if args.list_langs:
        print(run_ytdlp(["--list-subs", "--skip-download", "--no-playlist",
                         *extra, args.url]))
        return

    with tempfile.TemporaryDirectory() as tmp:
        outdir = Path(tmp)
        auto = False
        vtt = download(args.url, args.lang, outdir, auto=False, extra=extra)
        if not vtt:
            for stale in outdir.glob("*.info.json"):
                stale.unlink()
            vtt = download(args.url, args.lang, outdir, auto=True, extra=extra)
            auto = True
        if not vtt:
            sys.exit(
                f"No '{args.lang}' captions on this video, human or automatic.\n"
                f"Run with --list-langs to see what tracks exist, or fall back "
                f"to local speech-to-text (see SKILL.md)."
            )

        info_files = sorted(outdir.glob("*.info.json"))
        info = json.loads(info_files[0].read_text(encoding="utf-8")) if info_files else {}
        lines = parse_vtt(vtt)

    if not lines:
        sys.exit("Caption file downloaded but parsed empty — inspect it by hand.")

    blocks = chunk(lines, args.every)
    text = render(info, blocks, auto, args.lang, not args.no_timestamps)
    words = sum(len(b.split()) for _, b in blocks)

    if args.output:
        Path(args.output).write_text(text, encoding="utf-8")
        print(
            f"Wrote {args.output} — {words:,} words, "
            f"{'auto-generated' if auto else 'human-written'} captions.",
            file=sys.stderr,
        )
    else:
        print(text)
        print(f"\n[{words:,} words]", file=sys.stderr)


if __name__ == "__main__":
    main()
