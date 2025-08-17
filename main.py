import datetime
from pyexpat import model
import sys
import time
import webbrowser
import keyboard
import pyttsx3
from sklearn.calibration import LabelEncoder
import speech_recognition as sr
import os
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"
import json
import pickle
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import random
import numpy as np
import psutil
# from elevenlabs import generate, play
# from elevenlabs import set_api_key
# from api_key import api_key_data
# set_api_key(api_key_data)

# def engine_talk(query):




with open("intents.json") as file:
    data = json.load(file)

model = load_model("chat_model.h5")

with open("tokenizer.pkl", "rb") as f:
    tokenizer=pickle.load(f)

with open("label_encoder.pkl", "rb") as encoder_file:
    label_encoder=pickle.load(encoder_file)


def initilize_engine():
    engine=pyttsx3.init("sapi5")
    voices=engine.getProperty("voices")
    engine.setProperty("voice",voices[1].id)
    rate=engine.getProperty("rate")
    engine.setProperty('rate',rate-50)
    volume=engine.getProperty("volume")
    engine.setProperty("volume",volume+0.25)
    return engine
def speak(text):  
    engine=initilize_engine()
    engine.say(text)
    engine.runAndWait()
    # speak("hello , iam Bharath ,  assistnace  how can i help to you")

def command():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        print("Hearing.......",end="", flush=True)
        r.pause_threshold=1.0
        r.phrase_threshold=0.3
        r.sample_rate=48000
        r.dynamic_energy_threshold=True
        r.opration_timeout_limit=5
        r.non_speaking_duration=0.5
        r.dynamic_energy_adjustment=2
        r.energy_threshold=4000
        r.phrase_timeout_limit=10
        # print(sr.Microphone.list_microphone_names())
        audio=r.listen(source)
    try:
        print("\r", end="", flush=True)
        print("recogniting.......",end="", flush=True)
        query=r.recognize_google(audio, language="en-in")
        print("\r", end="", flush=True)
        print(f"user said: {query}\n")
    except Exception as e:
        print("it's not clear, please repeat again")
        return "None"
    return query
def cal_day():
    day=datetime.datetime.today().weekday() + 1
    day_dict = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }
    if day in day_dict.keys():
        day_of_week= day_dict[day]
        print(day_of_week)
        return day_of_week


def Wishme():
    hour=int(datetime.datetime.now().hour)
    t=time.strftime("%I:%M:%p")
    day=cal_day()
    if hour>=0 and hour<=12 and ('AM' in t):
        speak(f"Good Morning Boss, it's {day} and the time is {t}")
    elif hour>=12 and hour<=17 and ('PM' in t):
        speak(f"Good Afternoon Boss, it's {day} and the time is {t}")
    else:
        speak(f"Good Evening Boss, it's {day} and the time is {t}")
def social_media(command):
    if "youtube" in command:
        speak("Opening Youtube")
        webbrowser.open("https://www.youtube.com")
    elif "facebook" in command:
        speak("Opening facebook")
        webbrowser.open("https://www.facebook.com")
    elif "instagram" in command:
        speak("opening instagram")
        webbrowser.open("https://www.instagram.com")
    elif "whatsapp" in command:
        speak("opening whatsapp")
        webbrowser.open("https://www.whatsapp.com")
    else:
        speak("sorry, I cant help you with that command")
def schedule():
    day= cal_day().lower()
    if day == "monday":
        speak("Boss today schedule is ")
    week={
            "monday": "9:30 AM to 10:10 AM you have Deep learning class, from 10:20 am to 11:00 am you have Optimization Techniques class, from 11:40 am to 01:00 pm you have a Natural language processing lab, from 01:00 pm to 05:00 pm relax and enjoy your day",
            "tuesday": "9:30 AM to 10:10 AM you have Digital image processing class, from 10:20 am to 11:00 am you have NLP lab class, from 11:40 am to 01:00 pm you have a Text processing using AI, from 01:00 pm to 05:00 pm relax and enjoy your day",
            "wednesday": "9:30 AM to 10:10 AM you have Deep learning class, from 10:20 am to 11:00 am you have Optimization Techniques class, from 11:40 am to 01:00 pm you have a Natural language processing lab, from 01:00 pm to 05:00 pm relax and enjoy your day",
            "thursday": "9:30 AM to 10:10 AM you have natural language processing class, from 10:20 am to 11:00 am you have Leadership class, from 11:40 am to 01:00 pm you have a Machine learning Lab, from 01:00 pm to 05:00 pm relax and enjoy your day",
            "friday": "9:30 AM to 10:10 AM you have Deep learning class, from 10:20 am to 11:00 am you have Optimization Techniques class, from 11:40 am to 01:00 pm you have a Natural language processing lab, from 01:00 pm to 05:00 pm relax and enjoy your day",
            "saturday": "you have no schedule for today, relax and enjoy your day",
            "sunday": "it's a holiday, let's enjoy the day"
        }
    if day in week.keys():
            speak(week[day])
def openApp(command):
    if "open calculator" in command:
        speak("opening calculator")
        keyboard.send("win+r")
        time.sleep(1)
        keyboard.write("calc")
        time.sleep(1)
        keyboard.send("enter")

    elif "open notepad" in command:
        speak("opening notepad")
        keyboard.send("win+r")
        time.sleep(1)
        keyboard.write("notepad")
        time.sleep(1)
        keyboard.send("enter")

    elif "open paint" in command:
       speak("opening paint")
       keyboard.send("win+r")
       time.sleep(1)
       keyboard.write("mspaint")
       time.sleep(1)
       keyboard.send("enter")

    else:
       speak("sorry, I can't help you with that command")

def closeApp(command):
    if "close calculator" in command:
        speak("closing calculator")
        keyboard.send("alt+f4")

    elif "close notepad" in command:
        speak("closing notepad")
        keyboard.send("alt+f4")

    elif "close paint" in command:
        speak("closing paint")
        keyboard.send("alt+f4")

    else:
        speak("sorry, I can't help you with that command")
def browsing(query):
    if "google" in query:
        speak("Boss, what do you want to search in google")
        s=command().lower()
        webbrowser.open(f"{s}")
    elif "edge" in query:
        speak("opening edge browser")
        keyboard.send("win+r")
        time.sleep(1)
        keyboard.write("microsoft-edge:")
        time.sleep(1)
        keyboard.send("enter")
def condition():
    usage = str(psutil.cpu_percent())
    speak(f"CPU is at {usage} percentage")
    battery = psutil.sensors_battery()
    percentage = battery.percent
    speak(f"Boss our system have {percentage} percentage battery")
    if percentage>=80:
        speak("Boss we could have enough charging to continue our recording")
    elif percentage>=40 and percentage<=75:
        speak("Boss we should connect our system to charging point to charge our battery")
    else:
        speak("Boss we have very low power, please connect to charging otherwise recording should be off...")
import speech_recognition as sr

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300  # Adjust if needed
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=7)
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}")
            return query
        except sr.UnknownValueError:
            print("Could not understand audio.")
            return "none"
        except sr.RequestError:
            print("Could not request results from Google Speech Recognition.")
            return "none"
        except Exception as e:
            print(f"Error: {e}")
            return "none"
if __name__=="__main__":
    while True:
        Wishme()
        # query = command().lower()
        query = takeCommand().lower()
        if query == "none" or query.strip() == "":
            query = input("Enter your Command-> ").lower()

        # query = input("Enter your Command-> ")
        if ('youtube' in query) or ('facebook' in query) or ('instagram' in query) or ('whatsapp' in query):
            social_media(query)
        elif ('schedule' in query) or ('time table' in query):
            schedule()
        elif ('volume up' in query) or ('increase volume' in query):
            keyboard.send("volume up")
            speak("volume increased")
        elif ('volume down' in query) or ('decrease volume' in query):
            keyboard.send("volume down")
            speak("volume decreased")
        elif ('mute' in query) or ('volume mute' in query):
            keyboard.send("volume mute")
            speak("muted")
        elif ('open calculator' in query) or ('open notepad' in query) or ('open paint' in query):
            openApp(query)
        elif ('close calculator' in query) or ('close notepad' in query) or ('close paint' in query):
            closeApp(query)
        elif ('exit' in query) or ('quit' in query) or ('close' in query):
            speak("thank you for using Boomer assistant, have a nice day")
            sys.exit()
        elif ("what" in query) or ("who" in query) or ("how" in query) or ("hi" in query) or ("thanks" in query) or ("hello" in query):
            padded_sequences = pad_sequences(
                tokenizer.texts_to_sequences([query]),
                maxlen=20,
                truncating='post'
                )
            result = model.predict(padded_sequences)
            tag = label_encoder.inverse_transform([np.argmax(result)])[0]
            for intent in data['intents']:
                if intent['tag'] == tag:
                    speak(np.random.choice(intent['responses']))
                    break
        elif ("open google" in query) or ("search" in query) or ("open edge" in query):
            browsing(query)
        elif ("system condition" in query) or ("condition of system" in query):
            speak("checking system condition")
            condition()
        else:
            speak("Sorry, I didn’t understand that. Can you repeat?")

        
        


        # query=command().lower()
        # print(query)



        
