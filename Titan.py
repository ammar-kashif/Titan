# IMPORTING LIBRARIES
import speech_recognition as sr
from pyowm import OWM
import subprocess
import pyttsx3
import pyaudio
import datetime
import webbrowser
import wikipedia
import time
from random import choice, choices

# INSTANCES, PATHS AND VARIABLES
r = sr.Recognizer()
mic = sr.Microphone()
chrome = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
responses = ['What else can I do for you?', '', 'How else may I offer assistance to you?', 'Anything else...']
response = choice(responses)


# TITAN.EXE
def Titan(say):
    titan = pyttsx3.init()
    titan.setProperty('rate', 180)
    titan.say(say)
    titan.runAndWait()


# LISTENING
def Listen():
    with mic as source:
        print('Listening...')
        audio = r.listen(source)
    try:
        print('Recognizing...')
        text = r.recognize_google(audio)
    except Exception as e:
        print('Recognizing...')
        return 'None'
    return text


# WISHME
def wish():
    hour = int(datetime.datetime.now().hour)
    if 4 <= hour < 12:
        Titan('Good Morning, Titan here to assist you')
    elif 12 <= hour < 17:
        Titan('Good Afternoon, Titan here to assist you')
    elif 17 <= hour < 23:
        Titan('Good Evening, Titan here to assist you')
    elif 00 <= hour < 4:
        Titan("O Lord! It's late! What is it that you want?")


# TAKING NOTE
def note():
    Titan('Taking note...')
    noted = Listen().lower()
    Titan('Do you want to save the note?')
    text = Listen().lower()
    if 'yes' in text:
        Titan('Filename...')
        text = Listen().lower()
        filename = f'{text}.txt'
        with open(filename, 'w') as f:
            f.write(noted)
        Titan('Do you want to read the note?')
        text = Listen().lower()
        if 'yes' in text:
            Titan('Opening Note...')
            subprocess.Popen(['notepad.exe', filename])
        elif 'no' in text:
            Titan('No problem, you can read it later')
    elif 'no' in text:
        Titan('Dumped it!')


# WIKIPEDIA SEARCH
def wiki():
    Titan('What should I search?')
    text = Listen().lower()
    try:
        Titan('Searching Wikipedia...')
        text = text.replace('search for', '')
        results = wikipedia.summary(text, sentences=2)
        Titan(f'According to wikipedia, {results}')
    except Exception as e:
        Titan('Sorry, could not find any results')


# GOOGLE SEARCH
def google():
    Titan('What should I search?')
    search = Listen().lower()
    url = "https://www.google.co.in/search?q=" + (str(search)) + "&oq=" + (
        str(search)) + \
          "&gs_l=serp.12..0i71l8.0.0.0.6391.0.0.0.0.0.0.0.0..0.0....0...1c..64.serp..0.0.0.UiQhpfaBsuU"
    webbrowser.get(chrome).open_new(url)


# YOUTUBE SEARCH
def youtube():
    Titan('What should I search?')
    search = Listen().lower()
    url = 'https://www.youtube.com/results?search_query=' + (str(search))
    webbrowser.get(chrome).open_new(url)


# ALIEXPRESS SEARCH
def aliexpress():
    Titan('What should I search?')
    search = Listen().lower()
    url = 'https://www.aliexpress.com/wholesale?catId=0&initiative_id=SB_20191231091831&SearchText=' + (
        str(search))
    webbrowser.get(chrome).open_new(url)


# WEATHER INFO
def weather():
    key = "e2702472a730b34849ba95a819481586"
    owm = OWM(key)

    rwp_id = 1166993
    weather_info = owm.weather_at_id(rwp_id)
    weather_rwp = weather_info.get_weather()
    rwp_temp = weather_rwp.get_temperature(unit='celsius')
    Titan(f"It is {int(rwp_temp['temp'])} degrees celsius today in Rawalpindi")


# TIME INFO
def localTime():
    time_now = time.localtime()
    local_time = time.strftime("%I:%M %p", time_now)
    Titan(f'It is {local_time}.')


# DATE INFO
def localDate():
    time_now = time.localtime()
    local_date = time.strftime("%d %B", time_now)
    Titan(f'Today is {local_date}.')


# DAY INFO
def localDay():
    time_now = time.localtime()
    local_day = time.strftime('%A', time_now)
    Titan(f'Today is {local_day}.')


wish()
while True:
    text = Listen().lower()
    if 'weather in rawalpindi' in text:
        weather()
        Titan(response)
    elif 'time' in text:
        localTime()
        Titan(response)
    elif 'date' in text:
        localDate()
        Titan(response)
    elif 'day' in text:
        localDay()
        Titan(response)
    elif 'lights on' in text:
        Titan('Lights turned on.')
        Titan(response)
    elif 'lights off' in text:
        Titan('Lights turned off.')
        Titan(response)
    elif 'take a note' in text:
        note()
        Titan(response)
    elif 'search wikipedia' in text:
        wiki()
        Titan(response)
    elif 'search google' in text:
        google()
        Titan(response)
    elif 'search youtube' in text:
        youtube()
        Titan(response)
    elif 'search aliexpress' in text:
        aliexpress()
        Titan(response)
    elif 'open youtube' in text:
        webbrowser.get(chrome).open('youtube.com')
        Titan(response)
    elif 'open reddit' in text:
        webbrowser.get(chrome).open('reddit.com')
        Titan(response)
    elif 'open stack overflow' in text:
        webbrowser.get(chrome).open('stackoverflow.com')
        Titan(response)
    elif 'open spotify' in text:
        Titan('Opening Spotify...')
        location = 'C:/Users/ammar/AppData/Roaming/Spotify/Spotify.exe'
        subprocess.Popen([location])
        Titan(response)
    elif 'open pycharm' in text:
        location = "C:/Program Files/JetBrains/PyCharm Community Edition 2019.2.1/bin/pycharm64.exe"
        subprocess.Popen([location])
        Titan('Opening PyCharm...')
        Titan(response)
    elif 'open visual studio' in text:
        location = "C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/Common7/IDE/devenv.exe"
        subprocess.Popen([location])
        Titan('Opening Visual Studio...')
        Titan(response)
    elif 'open unity' in text:
        location = "C:/Program Files/2019.2.11f1/Editor/Unity.exe"
        subprocess.Popen([location])
        Titan('Opening Unity...')
        Titan(response)
    elif 'open blender' in text:
        location = "C:/Program Files/Blender Foundation/Blender 2.81/blender.exe"
        subprocess.Popen([location])
        Titan('Opening Blender...')
        Titan(response)
    elif 'open substance player' in text:
        location = "C:/Program Files/Allegorithmic/Substance Player/Substance Player.exe"
        subprocess.Popen([location])
        Titan('Opening Substance Player...')
        Titan(response)
    elif 'open visual studio code' in text:
        location = "C:/Users/ammar/AppData/Local/Programs/Microsoft VS Code/Code.exe"
        subprocess.Popen([location])
        Titan('Opening Sublime Text...')
        Titan(response)
    elif 'open arduino' in text:
        location = "C:/Program Files (x86)/Arduino/arduino.exe"
        subprocess.Popen([location])
        Titan('Opening Arduino...')
        Titan(response)
    elif 'open audacity' in text:
        location = "C:/Program Files (x86)/Audacity/audacity.exe"
        subprocess.Popen([location])
        Titan('Opening Audacity...')
        Titan(response)
    elif 'launch steam' in text:
        location = "C:/Program Files (x86)/Steam/Steam.exe"
        subprocess.Popen([location])
        Titan('Launching Steam...')
        Titan(response)
    elif 'launch Origin' in text:
        location = "C:/Program Files (x86)/Origin/Origin.exe"
        subprocess.Popen([location])
        Titan('Launching Origin...')
        Titan(response)
    elif 'launch rocket league' in text:
        location = 'D:/Steam Games/steamapps/common/rocketleague/Binaries/Win32/RocketLeague.exe'
        subprocess.Popen([location])
        Titan('Launching Rocket League...')
        Titan(response)
    elif 'launch apex' in text:
        location = 'D:/Origin Games/Apex/r5apex.exe'
        subprocess.Popen([location])
        Titan('Launching Apex Legends...')
        Titan(response)
    elif 'launch rainbow' in text:
        location = "D:/Steam Games/steamapps/common/Tom Clancy's Rainbow Six Siege/RainbowSix.exe"
        subprocess.Popen([location])
        Titan('Launching Rainbow Six Siege...')
        Titan(response)
    elif 'launch player unknown' in text:
        location = 'D:/PUBG Lite/Launcher.exe'
        subprocess.Popen([location])
        Titan('Launching Player Unknowns Battle Grounds...')
        Titan(response)
    elif 'who are you' in text:
        Titan('I am Titan, a friendly neighbourhood assistant. How can I please you?')
    elif 'how are you' in text:
        Titan('I am doing great. How about you?')
    elif 'i am fine' in text:
        Titan("That's great...so what can I help you with?")
    elif 'titan exit' in text:
        Titan('Initiating exit sequence...')
        break
    else:
        print(text)
        Titan("Sorry, I haven't been programmed to do that yet. Anything else?")