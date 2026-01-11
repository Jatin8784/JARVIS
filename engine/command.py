import pyttsx3
import speech_recognition as sr
import eel

engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 174)

def speak(text):
    if text.strip() == "":
        return
    engine.say(text)
    engine.runAndWait()
    engine.stop()

@eel.expose
def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        eel.DisplayMessage("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source, timeout=10, phrase_time_limit=6)

    try:
        print("Recognizing...")
        eel.DisplayMessage("Recognizing...")
        query = r.recognize_google(audio, language="en-IN")
        print("You said:", query)
        eel.DisplayMessage(query)
        speak(query)
        eel.ShowHood()
        return query.lower()
    except Exception as e:
        print("Could not recognize speech")
        return ""

# text = takeCommand()
# speak(text)
