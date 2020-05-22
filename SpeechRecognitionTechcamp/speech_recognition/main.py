# Import the speech recognition Library
import speech_recognition as sr 
from time import ctime
import webbrowser

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
            print('Sorry, I did not Understand what you said')
        except sr.RequestError:
            print('Sorry, My speech service is currently down')
        return voice

def respond(voice):
    if 'what is your name' in voice:
        print('My Name is John Doe')
    if 'what time is it' in voice:
        print(ctime())
    if 'search' in voice:
        search = record_audio('What do you want to search for?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        print('Here is what I found for ' + search)
    if 'find location' in voice:
        location = record_audio('where to')
        url = 'https://google.nl/maps/place' + location + '/&amp'
        webbrowser.get().open(url)
        print('Here is the location for ' + location)


print('How can I help you?')
voice = record_audio()
respond(voice)


