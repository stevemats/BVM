import speech_recognition as sr
from datetime import datetime as dt
import sys

def live_recognizer():

    #read duration from the arguments
    duration = int(input('Enter duration to record in secs(>1):'))

    # initializer
    r = sr.Recognizer()
    print("Please talk")
    with sr.Microphone() as source:
        # read the audio data from the default microphone
        audio_data = r.record(source, duration=duration)
        print("Recognizing...")
        # convert voice to txt
        text = r.recognize_google(audio_data)
        print('Audio Recognized:',text)
        print('\n',
            'Your voice succeffuly converted to text(recognized_audio_(date)_(time).txt to current banja folder)')

        # //To DO: Output voice to user path of choice
        time_now = dt.now() 
        new_time = time_now.strftime("%m-%d-%Y_%H-%M-%S")
        with open('recognized_audio_' + new_time + '.txt', 'w') as f:
            f.write(text)
