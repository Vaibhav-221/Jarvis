import speech_recognition as sr
import webbrowser
import pyttsx3
import time
import musicLabrary

recognizer = sr.Recognizer()
engine = pyttsx3.init('sapi5') 
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[0].id)
# engine.setProperty('rate', 170)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLabrary.music[song]
        webbrowser.open(link)

    

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
                speak("i am starting")



                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)

        except Exception as e:
            print("Error; {0}".format(e))