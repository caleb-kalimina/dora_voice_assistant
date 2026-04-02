import whisper
import groq
import pyaudio
import wave
import tempfile
import os
from dotenv import load_dotenv
import edge_tts
import asyncio
import pygame
import time
import threading
import warnings
warnings.filterwarnings("ignore")

# ---- SETTINGS ----
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
RECORD_SECONDS = 7  # increased from 5 to give more time to speak

# ---- SETUP ----
client = groq.Groq(api_key=GROQ_API_KEY)
whisper_model = whisper.load_model("base")
pygame.mixer.init()

def record_audio():
    """Record audio from microphone and save to temp file"""
    audio = pyaudio.PyAudio()
    stream = audio.open(format=pyaudio.paInt16, channels=1,
                        rate=16000, input=True, frames_per_buffer=1024)
    print("🎤 Listening...")
    frames = []
    for _ in range(0, int(16000 / 1024 * RECORD_SECONDS)):
        frames.append(stream.read(1024))
    stream.stop_stream()
    stream.close()
    audio.terminate()

    tmp = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
    wf = wave.open(tmp.name, 'wb')
    wf.setnchannels(1)
    wf.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
    wf.setframerate(16000)
    wf.writeframes(b''.join(frames))
    wf.close()
    return tmp.name

def transcribe(audio_path):
    """Convert speech to text using Whisper"""
    result = whisper_model.transcribe(audio_path, language="en")  # force English
    os.unlink(audio_path)
    return result["text"]

# ---- CONVERSATION HISTORY ----
conversation_history = []


def think(user_input):
    """Send text to Groq and get a response"""
    conversation_history.append({"role": "user", "content": user_input})
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You are Dora, a sharp and charismatic personal assistant built by Caleb. You can help with absolutely anything — questions, ideas, advice, tasks, jokes, you name it. You speak naturally and conversationally, like a brilliant friend who happens to know everything. You are warm, confident, occasionally witty, and never robotic. Keep responses concise but never boring. If anyone asks who made you or who built you, say exactly this: 'God did! ...just kidding, Caleb did. Another one!' in the most DJ Khaled energy you can bring."},
            *conversation_history
        ]
    )
    reply = response.choices[0].message.content
    conversation_history.append({"role": "assistant", "content": reply})
    return reply

def speak(text):
    """Convert text to speech using edge-tts"""
    print(f"🤖 Dora: {text}")
    async def _speak():
        communicate = edge_tts.Communicate(text, voice="en-US-AriaNeural")
        tmp = tempfile.NamedTemporaryFile(suffix=".mp3", delete=False)
        await communicate.save(tmp.name)
        pygame.mixer.music.load(tmp.name)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            await asyncio.sleep(0.1)
        pygame.mixer.music.unload()
        os.unlink(tmp.name)
    asyncio.run(_speak())

def think_and_speak(user_input):
    """Run Groq and TTS preparation in parallel"""
    result = {}

    def get_response():
        result['text'] = think(user_input)

    # Start Groq in background thread
    thread = threading.Thread(target=get_response)
    thread.start()
    thread.join()  # wait for response

    # Speak immediately once ready
    speak(result['text'])

# ---- MAIN LOOP ----
print("Dora is ready! Start talking. Say 'goodbye' to stop her. Press Ctrl+C to exit.")
while True:
    audio_path = record_audio()
    user_input = transcribe(audio_path)
    print(f"🎤 You said: {user_input}")

    if len(user_input.strip()) > 5:
        if "goodbye" in user_input.lower() or "bye dora" in user_input.lower():
            speak("Goodbye! Catch you later.")
            break
        response = think(user_input)
        speak(response)
    else:
        print("🔇 No speech detected, listening again...")