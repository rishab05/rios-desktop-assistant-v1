import pyttsx3
import datetime
import speech_recognition as sr
import os
import webbrowser
import wikipedia
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour>=0  and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    
    speak("Hi Sir, I am Rios, How may I help you?")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)    
        print("Say that again please...")  
        return "None"
    return query   

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your email', 'your password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

def audioToText(audio):
    fh = open("./notes/recognized.txt", "a")
    fh.write(audio)
    fh.write("\n")
    fh.close() 

def doTask():

    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   


        elif 'play music' in query:
            music_dir = 'E:\\Music'
            songs = os.listdir(music_dir)
            #print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Rishabh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "reciever's email"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry. I am not able to send this email")
        elif 'type' in query:
            try:
                speak("What should I type")
                content = takeCommand()
                audioToText(content)
                speak("file is saved")
            except Exception as e:
                print(e)
                speak("Sorry, I can't saved the file")
        
        elif 'exit' in query or 'quit' in query:
            speak("Bye sir")
            exit()
        
        else:
            speak("Sorry I can't understand, please say again")
                


def main():
    wishMe() #greet according to current time
    doTask()
    

if __name__=="__main__":
    main()

