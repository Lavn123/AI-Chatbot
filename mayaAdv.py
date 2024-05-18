import pyttsx3
import datetime
import speech_recognition as sr
import whatsapp

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio) 
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)    
    if hour>=0 and hour<=12:
        speak("Good Morning!!")
        print("Good Morning!!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!!")
        print("Good Afternoon!!")

    else:
        speak("Good Evening!!")
        print("Good Evening!!")

    speak("I am Maya, Please tell me how can i help you.")
    print("I am Maya, Please tell me how can i help you.")    
                 
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


if __name__=="__main__" :
    wishme()
    while True:
        query = takeCommand().lower() 

        if 'whatsapp message' in query:
            query = query.replace("maya", " ")
            query = query.replace("send", " ")
            query = query.replace("whatsapp message", " ")
            query = query.replace("to", " ")
            name = query

            if 'amma' in name:
                numb = "9916548600"
                speak(f"What's  the message for {name}")
                mess = takeCommand()
                whatsapp.whatsapp(numb,mess)

            elif 'disha akka' in name: 
                numb = "7349509443"
                speak(f"What's  the message for {name}")
                mess = takeCommand()
                whatsapp.whatsapp(numb,mess)

            elif 'HLS' in name:
                gro = ""
                speak(f"What's the message for {name}")
                mess = takeCommand()
                whatsapp.Whats_Grp(gro,mess)

                



            