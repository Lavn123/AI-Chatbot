import os
import speech_recognition as sr


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.79
        r.energy_threshold = 600
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') 
        print(f"User said: {query}\n") 

    except:
        print("Say that again please...")    
        return "None" 
    return query   

while True:

    wake_up = takeCommand()

    if 'wake up' in wake_up:
        os.startfile('"C:\\Users\\Lavanya\\OneDrive\\Desktop\\MAYA\\maya.py"')

    else:
        print("Nothing........")

        
            