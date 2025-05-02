
---

# **System Audio Recorder & Transcriber**

This Flask application allows you to **record system audio**, transcribe the recorded audio, and display the transcribed text on the webpage. It uses the **Groq Whisper API** to transcribe the audio in real-time. The audio is captured from your system's audio output using `ffmpeg` and **PulseAudio**.

---

## **Features**

* **Record System Audio**: Captures the audio playing on your system using `ffmpeg` and **PulseAudio**.
* **Stop Recording**: Allows you to stop the recording at any time.
* **Transcribe Audio**: Uses the **Groq Whisper API** to convert the recorded audio into text.
* **Real-time Transcription**: After stopping the recording, the transcription is displayed directly on the webpage.

---

## **How It Works**

1. **Recording**:

   * The app uses `ffmpeg` to capture audio from your system's **PulseAudio output**.
   * The audio is saved as a `.wav` file (`system_audio.wav`).
2. **Transcription**:

   * Once the recording is stopped, the recorded `.wav` file is sent to the **Groq Whisper API** for transcription.
   * The transcribed text is returned and displayed on the webpage.

---

## **Requirements**

* **Python 3.6+**
* **ffmpeg**: A command-line tool to capture and record audio.
* **PulseAudio**: A sound system used for recording system audio.
* **Groq API Key**: You need a Groq API key to use the Whisper transcription service.
* **pavucontrol** (Optional): A GUI tool to monitor and control PulseAudio streams.

---

## **Installation & Setup**

### 1. **Clone the repository**

```bash
git clone https://github.com/your-repository/system-audio-recorder.git
cd system-audio-recorder
```

### 2. **Install Dependencies**

Make sure you have **Python 3.6+** installed. You will also need **ffmpeg** and **PulseAudio**.

Install the necessary Python packages:

```bash
pip install -r requirements.txt
```

### 3. **Install `ffmpeg` and `PulseAudio`**

On **Arch Linux** (or any distribution using `pacman`):

```bash
sudo pacman -S ffmpeg pulseaudio
```

For other Linux distributions, use the appropriate package manager to install `ffmpeg` and `pulseaudio`.

---

### 4. **Set Up the `.env` File**

Create a `.env` file in the root directory and add your **Groq API key**. The `.env` file should look like this:

```plaintext
GROQ_API_KEY=your-actual-groq-api-key
```

If you don't have a Groq API key, sign up at [Groq](https://groq.com/) to get access to their Whisper transcription service.

---

### 5. **Install `pavucontrol` (Optional)**

If you want to visually monitor and control the PulseAudio streams, you can install `pavucontrol`:

```bash
sudo pacman -S pavucontrol  # On Arch Linux
```

For Ubuntu/Debian:

```bash
sudo apt install pavucontrol
```

Once installed, you can open `pavucontrol` to visually see and manage PulseAudio input/output streams. You can also use it to check if the PulseAudio input for **system sound** is active while recording.

---

### 6. **Run the Flask Application**

Now you're ready to run the Flask app:

```bash
python app.py
```

The app will start running on `http://localhost:5000`.

---

## **How to Use the Application**

1. **Open the app**: Visit [http://localhost:5000](http://localhost:5000) in your web browser.
2. **Start Recording**: Click the **Start Recording** button. The app will begin recording your system audio.
3. **Stop Recording**: Click the **Stop Recording** button when you’re done recording.
4. **Transcribe**: After stopping the recording, click the **Transcribe** button to send the recorded audio to Groq’s Whisper API for transcription. The transcribed text will be displayed on the page.

---

## **Monitoring Audio Streams (Optional)**

To monitor and control the audio being captured on your system:

1. **Open `pavucontrol`**:

   * Launch `pavucontrol` by typing `pavucontrol` in the terminal.
   * Navigate to the **Recording** tab.
   * You should see an active stream for the `ffmpeg` capture device (which the app is using to capture the system's audio).

2. **Ensure PulseAudio is Correctly Capturing System Audio**:

   * In the **Playback** tab, you can see which applications are outputting audio to your speakers or headphones.
   * In the **Recording** tab, ensure that the app (via `ffmpeg`) is listed as an active source for capturing audio.

3. **Monitor Audio Levels**:

   * You can visually monitor the audio levels for the capture stream and adjust the volume accordingly.

---

## **Project Structure**

```plaintext
your_project/
│
├── app.py            # Flask Application
├── .env              # Environment variables (Groq API key)
├── templates/
│   └── index.html    # HTML Template
├── static/
│   └── style.css     # CSS Styles
└── requirements.txt  # Python dependencies
```

### **Important Files**

* **app.py**: The main Python file that runs the Flask application, handles routes, and integrates with the Groq Whisper API.
* **.env**: A hidden file that stores your Groq API key.
* **templates/index.html**: The main HTML page with buttons to start recording, stop recording, and transcribe audio.
* **static/style.css**: Custom styles to make the webpage look clean and simple.

---

## **Troubleshooting**

* **No Audio Captured**: Make sure **PulseAudio** is running, and you're using the correct source for the system audio (`alsa_output.pci-0000_00_1f.3.analog-stereo.monitor` is common for many Linux systems, but you may need to adjust this for your setup).

  * Check available PulseAudio sources:

    ```bash
    pactl list sources short
    ```
  * Use `pavucontrol` to verify that the system audio is being captured.

* **Missing Transcription**: Double-check that the Groq API key is correctly set in the `.env` file.

* **ffmpeg Errors**: Ensure that `ffmpeg` is installed and accessible from the terminal.

---

## **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## **Contributions**

Feel free to fork this repository and open pull requests for improvements. If you find any bugs or issues, please open an issue on GitHub!

---

## **Acknowledgements**

* **Groq**: For providing the Whisper API for audio transcription.
* **ffmpeg**: For recording system audio.
* **Flask**: For building this simple web application.
* **PulseAudio**: For managing and capturing system audio.
* **pavucontrol**: For monitoring PulseAudio streams and managing the system's audio input.

---


