import os
import subprocess
import signal
from flask import Flask, render_template, jsonify
import groq
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

app = Flask(__name__)

OUTPUT_FILE = "Audio/system_audio.wav"
MONITOR_SOURCE = "alsa_output.pci-0000_00_1f.3.analog-stereo.monitor"  # Replace with your monitor source
ffmpeg_process = None

# Get API key from environment
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise RuntimeError("Missing GROQ_API_KEY in environment or .env file")

client = groq.Client(api_key=GROQ_API_KEY)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start')
def start_recording():
    global ffmpeg_process

    if ffmpeg_process:
        return "Already recording."

    if os.path.exists(OUTPUT_FILE):
        os.remove(OUTPUT_FILE)

    cmd = [
        "ffmpeg",
        "-f", "pulse",
        "-i", MONITOR_SOURCE,
        "-acodec", "pcm_s16le",
        "-ar", "44100",
        "-ac", "2",
        OUTPUT_FILE
    ]

    ffmpeg_process = subprocess.Popen(cmd)
    return "Recording started."

@app.route('/stop')
def stop_recording():
    global ffmpeg_process

    if not ffmpeg_process:
        return "No recording in progress."

    ffmpeg_process.send_signal(signal.SIGINT)
    ffmpeg_process.wait()
    ffmpeg_process = None
    return "Recording stopped."

@app.route('/transcribe')
def transcribe_audio():
    if not os.path.exists(OUTPUT_FILE):
        return jsonify({"error": "No audio file to transcribe."}), 404

    with open(OUTPUT_FILE, "rb") as audio_file:
        result = client.audio.transcriptions.create(
            model="whisper-large-v3",
            file=audio_file
        )

    return jsonify({"transcription": result.text})

if __name__ == '__main__':
    app.run(debug=False,port=5000)
