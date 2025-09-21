import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # try voices[1] if 0 doesn’t work
engine.say("Hello, this is a test.")
engine.runAndWait()
