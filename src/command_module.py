 
import webbrowser
from tts_module import speak

def process_command(command):
    if "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    elif "open whatsapp" in command:
        speak("Opening WhatsApp Web")
        webbrowser.open("https://web.whatsapp.com")
    elif "open calculator" in command:
        speak("Opening Calculator")
        import os
        os.system("calc")  # Windows
    elif "search" in command:
        search_query = command.replace("search", "").strip()
        speak(f"Searching for {search_query}")
        webbrowser.open(f"https://www.google.com/search?q={search_query}")
    else:
        speak("Sorry, I did not understand that command")
def process_command(command):
    # Existing commands...
    
    if "stop" in command or "exit" in command or "quit" in command:
        speak("Shutting down. Goodbye!")
        exit()  # stops the assistant

    # Other commands like open YouTube, AI response, etc.
