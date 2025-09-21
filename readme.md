
# Voice-Controlled AI Desktop Assistant

A **smart AI-powered desktop assistant** built with Python that can recognize real-time speech, execute system commands, and generate AI-based responses using **Google Gemini**.

This project demonstrates practical applications of **speech recognition**, **text-to-speech**, **AI integration**, and system automation.

---

## Features

* **Voice commands**: Wake up the assistant with a wake word (default: "assistant")
* **Application control**: Launch apps like YouTube, WhatsApp, and Calculator
* **Web search**: Search the web directly via voice commands
* **AI responses**: Uses Google Gemini API to answer general queries
* **Text-to-speech**: Reads responses aloud
* **Modular structure**: Easy to extend for additional commands or offline speech recognition

---

## Technologies & Tools

* **Python 3.10+**
* **SpeechRecognition** (for speech-to-text)
* **pyttsx3** (for text-to-speech)
* **Google Gemini API** (AI-based responses)
* **Webbrowser & OS modules** (to launch apps)
* **Pyaudio** (microphone input)
* **python-dotenv** (for environment variables)

---

## Installation

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/voice_assistant.git
cd voice_assistant
```

2. **Create a virtual environment**

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Set up your Gemini API key**
   Create a `.env` file in the project root:

```
GEMINI_API_KEY=your_api_key_here
LANG=en-US
```

---

## Usage

Activate your virtual environment, then run:

```bash
python src/assistant/main.py
```

1. Say the wake word: `"assistant"`
2. Give commands like:

   * `"Open YouTube"`
   * `"Search Python decorators"`
   * `"Open Calculator"`
   * Or ask a question to get AI-powered responses

---

## Folder Structure

```
voice_assistant/
├─ src/
│  └─ assistant/
│     ├─ main.py
│     ├─ config.py
│     ├─ stt.py
│     ├─ tts.py
│     ├─ commands.py
│     └─ gemini_client.py
├─ requirements.txt
├─ README.md
├─ .env.example
├─ .gitignore
└─ venv/
```

---

## Notes

* **Microphone** and **speaker** permissions are required.
* **Gemini API key**: Ensure your key is valid and environment variable `.env` is set.
* Offline speech recognition can be added using VOSK or Whisper.
* For hotword detection, consider integrating Picovoice/Porcupine.

---

## Future Improvements

* Add **hotword detection** for faster wake-up
* Integrate **offline STT** for no internet use
* GUI overlay with **Tkinter or Electron**
* AI function calling for structured commands

---

## Author

**Your Name** – Portfolio-ready project
