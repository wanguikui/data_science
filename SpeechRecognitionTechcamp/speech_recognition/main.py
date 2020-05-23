# Import the speech recognition Library
import speech_recognition as sr 
from time import ctime
import webbrowser
from gtts import gTTS
import random
import playsound
import os
import time

# create an instance of the recognizer class
r = sr.Recognizer()

# convert speech to text

def record_audio(ask = False):
    with sr.Microphone() as source:
       # print('say something')

        if ask:
            print(ask)
           
        audio = r.listen(source)
        voice = ''
        try:

            voice = r.recognize_google(audio)
           # print(voice)

        except sr.UnknownValueError:
            john_doe('Sorry, I did not Understand what you said')
        except sr.RequestError:
            john_doe('Sorry, My speech service is currently down')
        return voice

def respond(voice):
    if 'what is your name' in voice:
        john_doe('My Name is John Doe')
    if 'what time is it' in voice:
        john_doe(ctime())
    if 'search' in voice:
        search = record_audio('What do you want to search for?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        john_doe('Here is what I found for ' + search)
    if 'find location' in voice:
        location = record_audio('where to')
        url = 'https://google.nl/maps/place/ ' + location + '/&amp'
        webbrowser.get().open(url)
        john_doe('Here is the location for ' + location)
    if 'exit' in voice:
        john_doe('Goodbye')
        exit()

# function for speech
def john_doe(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

# use time property to continously listen/interact with john_doe
time.sleep(1)
john_doe('How can I help you?')
while(1):
    voice = record_audio()
    respond(voice)



