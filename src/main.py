 
from speech_module import listen_command
from command_module import process_command
from tts_module import speak

def main():
    speak("Assistant is online. Say 'assistant' to wake me up.")
    
    while True:
        command = listen_command()  # listens to user
        if command:
            process_command(command)

if __name__ == "__main__":
    main()
