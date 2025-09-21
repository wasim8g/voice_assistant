 
# config.py
from dotenv import load_dotenv
import os

# Load variables from .env file
load_dotenv()  # reads the .env file in project root

# Gemini API key for AI responses
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Language for speech recognition
LANG = os.getenv("LANG", "en-US")

# Wake words to activate assistant
WAKE_WORDS = ("assistant", "hey assistant", "ok assistant")

# Microphone and listening settings
PHRASE_TIME_LIMIT = int(os.getenv("PHRASE_TIME_LIMIT", "7"))
SAMPLE_RATE = int(os.getenv("SAMPLE_RATE", "16000"))
ENERGY_THRESHOLD = int(os.getenv("ENERGY_THRESHOLD", "300"))
