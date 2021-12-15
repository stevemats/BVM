import speech_recognition as sr
from datetime import datetime as dt
import sys

def live_recognizer():

    #read duration from the arguments
    duration = int(input('Enter duration to record(>1):'))

    # initialize the recognizer
    r = sr.Recognizer()
    print("Please talk")
    with sr.Microphone() as source:
        # read the audio data from the default microphone
        audio_data = r.record(source, duration=duration)
        print("Recognizing...")
        # convert speech to text
        text = r.recognize_google(audio_data)
        print('Audio Recognized:',text)

        time_now = dt.now()  # get current time of PS change
        new_time = time_now.strftime("%m-%d-%Y_%H-%M-%S")
        with open('recognized_audio_' + new_time + '.txt', 'w') as f:
            f.write(text)
