
# 🤖 AI Meeting Action Item Extractor

This Python project uses the **Groq API** (LLaMA 3.3 70B model) with `instructor` and `pydantic` to **automatically extract structured action items** (e.g., emails, todos, notes, calendar events) from a raw transcript of a meeting.

---

## 📌 Features

- 🔍 Extracts actionable items from meeting transcripts
- 🧠 Uses LLaMA-3 via Groq API for intelligent parsing
- 📦 Structured data output in JSON format
- 📝 Supports:
  - `note`
  - `email`
  - `calendar_event`
  - `todo`
  - `web_search` (optional extension)

---

## 🛠 Requirements

Make sure you have Python 3.8+ and install dependencies:

```bash
pip install -r requirements.txt
```

**Example `requirements.txt`:**

```
groq
instructor
pydantic
python-dotenv
```

---

## ⚙️ Environment Setup

Create a `.env` file in the root directory and add your Groq API key:

```env
GROQ_API=your_groq_api_key_here
```

---

## 🚀 Running the Script

Simply run:

```bash
python action_extractor.py
```

If everything works, you'll see:

```
Action items saved to action_items.json
```

---

## 📂 Output Format

**`action_items.json` Example:**

```json
[
  {
    "type": "note",
    "content": "Track Q2 sales weekly and review in meetings"
  },
  {
    "type": "email",
    "content": "Send follow-up email to client@example.com summarizing Q2 meeting",
    "recipient": "client@example.com",
    "subject": "Follow-up on Q2 meeting",
    "body": "Include key points discussed"
  },
  {
    "type": "calendar_event",
    "content": "Schedule review meeting for Friday"
  },
  {
    "type": "todo",
    "content": "Tom to update the project timeline by tomorrow"
  }
]
```

---

## ✍️ Modify the Transcript

You can replace the sample `transcript` variable in `action_extractor.py` with your own text:

```python
transcript = """
Your meeting text here...
"""
```

---

## 🧠 How It Works

- Uses `instructor` to define `pydantic` response models
- Sends a prompt to Groq API with a structured output schema
- Receives and validates structured JSON
- Saves it to `action_items.json`

---

## 🔐 Safety

- API key is loaded from `.env` using `python-dotenv`
- No key is hardcoded in the script

---
