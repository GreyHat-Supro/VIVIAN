import pyttsx3
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib
import pyjokes
from PyDictionary import PyDictionary
import cv2
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am VIVIAN. Please tell me how may I assist you")       

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
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('saha.supratik1234@gmail.com', 'sahabinu1234')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            query = takeCommand().lower()
            results = PyDictionary(query)
            speak('Searching in Wikipedia...')
            speak("According to Wikipedia")
            print(results.meaning(query))
            speak(results.meaning(query))
        elif 'open youtube' in query:
            speak("Opening youtube")
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            speak("Opening google")
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            speak("Opening stackoverflow")
            webbrowser.open("stackoverflow.com")
        elif 'open facebook' in query:
            speak("Opening facebook")
            webbrowser.open("facebook.com")
        elif 'open instagram' in query:
            speak("Opening instagram")
            webbrowser.open("instagram.com")
        elif 'vivian tell me about yourself' in query: 
            speak("I am your personal voice input virtual interface assisting navigator") 
        elif 'play music' in query:
            speak("Whats your mood")
            query = takeCommand().lower()
            if 'sad' in query:
                music_dir = 'E:\\Song\\sad'
                songs = os.listdir(music_dir)
                speak(songs)
                print(songs)    
                os.startfile(os.path.join(music_dir, songs[0]))
            elif 'happy' in query:
                music_dir = 'E:\\Song\\happy'
                songs = os.listdir(music_dir)
                speak(songs)
                print(songs)    
                os.startfile(os.path.join(music_dir, songs[0])) 
        elif "what's the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak("Sir, the time is {strTime}")
        elif 'make me laugh' in query:
            print(pyjokes.get_joke())
            speak(pyjokes.get_joke())
        elif 'vivian take selfie' in query:
            cap = cv2.VideoCapture(1)
            face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
            smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')
            while True:
                _, frame = cap.read()
                original_frame = frame.copy()
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                face = face_cascade.detectMultiScale(gray, 1.3, 5)
                for x, y, w, h in face:
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)
                    face_roi = frame[y:y+h, x:x+w]
                    gray_roi = gray[y:y+h, x:x+w]
                    smile = smile_cascade.detectMultiScale(gray_roi, 1.3, 25)
                    for x1, y1, w1, h1 in smile:
                        cv2.rectangle(face_roi, (x1, y1), (x1+w1, y1+h1), (0, 0, 255), 2)
                        time_stamp = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
                        file_name = f'selfie-{time_stamp}.png'
                        cv2.imwrite(file_name, original_frame)
                cv2.imshow('cam star', frame)
                if cv2.waitKey(10) == ord('q'):
                    break
        elif 'email to ' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = ""    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend . I am not able to send this email") 

