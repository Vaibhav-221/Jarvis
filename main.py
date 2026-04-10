import speech_recognition as sr
import webbrowser
import pyttsx3
import time
from openai import OpenAI
import requests

# Initialize speech engine once
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
if voices:
    engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 170)
import musicLabrary

recognizer = sr.Recognizer()
newsapi = "5eee06fab56e42d9bd278df618ddcf6b"
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[0].id)
# engine.setProperty('rate', 170)

def speak(text):
    """Speak the given text using a fresh pyttsx3 engine.
    Using the default driver (sapi5 on Windows) avoids driver‑specific
    conflicts and works even when the microphone is active.
    """
    try:
        _engine = pyttsx3.init()  # let pyttsx3 pick the appropriate driver
        _engine.setProperty('rate', 170)
        voices = _engine.getProperty('voices')
        if voices:
            _engine.setProperty('voice', voices[0].id)
        _engine.say(text)
        _engine.runAndWait()
    except Exception as e:
        print(f"SPEAK ERROR: {e}")
    # Small pause to ensure audio finishes before we start listening again
    time.sleep(0.8)

def aiProcess(command):
    client = OpenAI(api_key="<Your Key Here>",
    )

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud. Give short responses please"},
        {"role": "user", "content": command}
    ]
    )
    return completion.choices[0].message.content


def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://www.linkedin.com/")
    
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLabrary.music[song]
        webbrowser.open(link)
        

    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/everything?q=tesla&from=2026-03-09&sortBy=publishedAt&apiKey=5eee06fab56e42d9bd278df618ddcf6b")
        if r.status_code == 200:
            # Parse the JSON response
            data = r.json()
            
            # Extract the articles
            articles = data.get('articles', [])
            
            # Print the headlines
            for article in articles:
                speak(article['title'])

    else:
        output = aiProcess(c)
        speak(output)


    

if __name__ == "__main__":
   speak("Initializing jarvis")
   r = sr.Recognizer()
   while True:
        # Listen for the wake word "Jarvis"
        # obtain audio from the microphone
        r = recognizer
        
        print("recognizing...")
        try:

            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=5, phrase_time_limit=3)
            word = r.recognize_google(audio)


            if "jarvis" in word.lower():
                speak("ya go ahead")
                # pause to let TTS finish before listening for command
                # time.sleep(0.5)

                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)

        except Exception as e:
            print("Error; {0}".format(e))
            