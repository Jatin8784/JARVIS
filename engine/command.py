import pyttsx3
import speech_recognition as sr

# Initialize TTS engine ONCE
engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 174)

def speak(text):
    if text.strip() == "":
        return
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source, timeout=10, phrase_time_limit=6)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-IN")
        print("You said:", query)
        return query.lower()
    except Exception as e:
        print("Could not recognize speech")
        return ""

text = takeCommand()
speak(text)
