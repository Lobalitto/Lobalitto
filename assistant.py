#!/usr/bin/env python3
"""Portable AI assistant: translate English to Russian and speak the result."""

from __future__ import annotations

import argparse
import sys
from typing import Optional

from googletrans import Translator
import pyttsx3


def translate_text(text: str) -> str:
    translator = Translator()
    translation = translator.translate(text, src="en", dest="ru")
    return translation.text


def pick_russian_voice(engine: pyttsx3.Engine) -> Optional[str]:
    for voice in engine.getProperty("voices"):
        langs = []
        if hasattr(voice, "languages"):
            langs = [lang.decode("utf-8", errors="ignore") if isinstance(lang, bytes) else str(lang) for lang in voice.languages]
        if any("ru" in lang.lower() or "russian" in lang.lower() for lang in langs) or "russian" in voice.name.lower():
            return voice.id
    return None


def speak_text(text: str) -> None:
    engine = pyttsx3.init()
    russian_voice_id = pick_russian_voice(engine)
    if russian_voice_id:
        engine.setProperty("voice", russian_voice_id)
    engine.say(text)
    engine.runAndWait()


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Translate English text to Russian and speak it out loud.",
    )
    parser.add_argument(
        "text",
        nargs="*",
        help="English text to translate. If omitted, reads from stdin.",
    )
    parser.add_argument(
        "--no-speech",
        action="store_true",
        help="Only print the translation without speaking.",
    )
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    if args.text:
        input_text = " ".join(args.text).strip()
    else:
        input_text = sys.stdin.read().strip()

    if not input_text:
        print("No input text provided.", file=sys.stderr)
        return 1

    translated = translate_text(input_text)
    print(translated)

    if not args.no_speech:
        speak_text(translated)

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
