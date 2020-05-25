import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import sys
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 200)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    time = datetime.datetime.now().hour
    if time>=0 and time<=12:
        speak("Good Morning Sir")
    elif time>12 and time<=15:
        speak("Good Afternoon Sir")
    elif time>15 and time<=24:
        speak("Good Evening Sir")
    speak("Jarvis here...")
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("User: "+ r.recognize_google(audio, language='en-in'))
    except LookupError:
        print("Could not understand audio")
        return "None"
    return query
if __name__ == "__main__":
    wishMe()
    while True:
        query = take_command().lower()
        if 'wikipedia' in query:
            speak("Searching Wikipedia")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("www.youtube.com")
        elif 'open google' in query:
            webbrowser.open("www.google.com")
        elif 'the time' in query:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            speak("Sir, the time is")
            speak(time)
        elif 'open calculator' in query:
            speak("Ok sir, Opening")
            calPath = "C:\\Users\\HP\\Desktop\\Calci.exe"
            os.startfile(calPath)
        elif 'how are you' in query:
            speak("I am Fine Sir. How are you Sir?")
        elif 'i am fine' in query:
            speak("So, Tell Me How Can I help you?")
        elif 'ok quit' in query:
            speak("Bye Sir. See you soon")
            sys.exit("BYE SIR")
