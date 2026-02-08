# Portable AI Assistant (EN → RU)

A small CLI assistant that translates English text to Russian and speaks the result.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

Translate a sentence and speak it:

```bash
python assistant.py "Hello, how are you?"
```

Translate from stdin:

```bash
echo "Good morning" | python assistant.py
```

Disable speech (print-only):

```bash
python assistant.py "See you later" --no-speech
```

## Notes

- Speech uses `pyttsx3` for offline TTS. Voice availability depends on your OS.
- Translation uses `googletrans`, which requires an internet connection.
