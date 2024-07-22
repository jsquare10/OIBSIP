import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def say(audio):
    engine.say(audio)
    engine.runAndWait()

def wishUser():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        say("Good Morning!")
    elif hour >=12 and hour<18:
        say("Good Afternoon!")
    else:
        say("Good Evening")

def inputCommand():

    r=sr.Recognizer()
    with sr.Microphone() as  source:
        print("Listening..........")
        r.pause_threshold =1
        audio = r.listen(source)
    
    try:
        print("Recognizing.........")
        query = r.recognize_google(audio,language='en-in') # type: ignore
        print(f"User said: {query}\n")

    except Exception as e:
        print("say that again please")
        return "None"
    return query
if __name__=="__main__":
    wishUser()
    while True:
        query = inputCommand().lower()

        if 'wikipedia' in query:
            say('Searching wikipedia.....')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            say("According to wikipedia")
            print(results)
            say(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'the time' in query:
            Time = datetime.datetime.now().strftime("%H:%M:S")
            say(f"Mam, the time is {Time}")
        elif 'play music' in query:
            music = r"E:\oiasis infobyte project"
            songs = os.listdir(music)
            print(songs)
            print("playing song............")
            os.startfile(os.path.join(music,songs[0]))

