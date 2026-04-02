# 🎙️ Dora — AI Voice Assistant

Dora is a smart, conversational AI voice assistant built in Python. She listens to your voice, understands what you say, thinks of a response using a powerful AI model, and talks back to you in a natural human-like voice.

Built by **Caleb Kalimina**, Computer Science student at Mulungushi University, Zambia.

---

## ✨ Features

- 🎤 **Voice input** — speaks naturally into your mic, no typing needed
- 🧠 **AI-powered responses** — powered by Llama 3.3 via Groq API
- 🔊 **Natural voice output** — uses Microsoft Edge TTS for smooth, human-like speech
- 💬 **Conversation memory** — remembers everything said during the session
- 🔒 **Secure** — API keys stored safely in a `.env` file, never hardcoded
- 🚫 **Noise filtering** — ignores silence and background noise automatically
- 👋 **Exit with voice** — just say "goodbye" to stop Dora

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| `openai-whisper` | Speech to text (runs locally) |
| `groq` | AI brain — Llama 3.3 70B model |
| `edge-tts` | Text to speech (Microsoft neural voices) |
| `pygame` | Audio playback |
| `pyaudio` | Microphone capture |
| `python-dotenv` | Secure API key management |
| `ffmpeg` | Audio processing for Whisper |

---

## 🚀 Setup

### 1. Clone the repository
```bash
git clone https://github.com/caleb-kalimina/dora_voice_assistant.git
cd dora_voice_assistant
```

### 2. Install system dependencies

**Mac:**
```bash
brew install portaudio ffmpeg
```

**Windows:**
```bash
choco install ffmpeg
```

### 3. Install Python packages
```bash
pip install openai-whisper groq pyaudio python-dotenv edge-tts pygame
```

### 4. Get your Groq API key
- Sign up for free at [console.groq.com](https://console.groq.com)
- Create an API key
- Never share it or commit it to GitHub

### 5. Create your `.env` file
```bash
touch .env
```

Add this inside:
```
GROQ_API_KEY=your_actual_key_here
```

### 6. Run Dora
```bash
python voice_assistant.py
```

---

## 💬 How to Use

1. Run the script
2. Wait for **"Dora is ready!"**
3. Start talking — Dora will listen for 7 seconds
4. She'll respond in her natural voice
5. Keep the conversation going — she remembers everything
6. Say **"goodbye"** to end the session

---

## 📁 Project Structure

```
dora_voice_assistant/
├── voice_assistant.py   # Main application
├── .env                 # Your API key (never committed)
├── .gitignore           # Keeps secrets out of GitHub
└── README.md            # This file
```

---

## ⚠️ Important Notes

- Your `.env` file is in `.gitignore` — it will never be pushed to GitHub
- The Whisper base model (~140MB) downloads automatically on first run
- Dora runs best with a stable internet connection for Groq and Edge TTS
- On older hardware (like Intel Macs) there may be a slight delay — this is normal

---

## 🔮 Roadmap

- [ ] Wake word detection using Porcupine
- [ ] GUI with tkinter
- [ ] Web app version using Flask
- [ ] ElevenLabs integration for even more natural voice
- [ ] Mobile app

---

## 👨🏾‍💻 Author

**Caleb Kalimina**  
Computer Science Student — Mulungushi University, Zambia  
[GitHub](https://github.com/caleb-kalimina)

---

*Built from scratch in one session. April 2026. 🔥*
