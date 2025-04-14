

### ✅ `README.md`


# 🎧 Whisper Audio Transcription API (FastAPI)

This is a simple web API built using **FastAPI** and **OpenAI Whisper** that transcribes audio files to text. It also serves an HTML frontend from the `/static` folder where you can interact with the transcription endpoint.

---

## 🚀 Features

- Upload and transcribe `.mp3`, `.wav`, or other audio files.
- Get instant transcriptions using Whisper's `"base"` model.
- CORS enabled for frontend integration.
- Simple HTML frontend served from `/static/index.html`.

---

## 🛠 Requirements

- Python 3.8+
- `whisper`
- `fastapi`
- `uvicorn`

### 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

**Example `requirements.txt`:**
```
fastapi
uvicorn
openai-whisper
```

---

## 🔄 Run the API

```bash
uvicorn main:app --reload
```

- The app will run on: `http://localhost:8000`

---

## 🌐 Access Frontend

Put your `index.html` (or any frontend) inside a folder named `static`.

Example access:

```
http://localhost:8000/static/index.html
```

This opens your HTML page, which can make `POST` requests to `/transcribe`.

---

## 🎯 API Endpoint

### `POST /transcribe`

Upload an audio file and get its transcription.

**Request:**
- `multipart/form-data`
- Key: `file`
- Value: (your audio file)

**Response:**
```json
{
  "transcription": "Your audio text here...",
  "error": null
}
```

---

## 📂 Project Structure

```
.
├── main.py
├── static/
│   └── index.html
├── requirements.txt
└── README.md
```

---

## 🧪 Sample Curl Command

```bash
curl -X POST "http://localhost:8000/transcribe" \
  -F "file=@your_audio_file.wav"
```

---

## ✅ Notes

- Make sure the audio file you upload has a valid `content-type`, e.g., `audio/wav`, `audio/mpeg`, etc.
- The temp audio file is deleted after processing.
- You can change the Whisper model (`tiny`, `base`, `small`, `medium`, `large`) by modifying `whisper.load_model("base")`.

---
