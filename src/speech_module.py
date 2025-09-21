 
import speech_recognition as sr

def listen_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, phrase_time_limit=7)
        try:
            command = r.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            return None
        except sr.RequestError:
            print("Speech Recognition service failed")
            return None
