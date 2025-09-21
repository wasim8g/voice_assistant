from speech_module import listen_command
from command_module import process_command
from tts_module import speak

def main():
    speak("Assistant is online. Say 'assistant' to wake me up.")
    
    running = True  # flag to control the loop
    while running:
        command = listen_command()  # listens to user
        if command:
            if "stop" in command or "exit" in command or "quit" in command:
                speak("Shutting down. Goodbye!")
                running = False
            else:
                process_command(command)

if __name__ == "__main__":
    main()
