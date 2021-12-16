import speech_recognition as sr
from datetime import datetime as dt

# To Do: output transcription, path for file to trascribe

def short_recognizer():

    # filename = sys.argv[1]

    # initialize the recognizer
    path = input('Enter path to audio:')

    r = sr.Recognizer()
    # open the file
    with sr.AudioFile(path) as source:
        # listen for the data (load audio to memory)
        audio_data = r.record(source)
        # recognize (convert from speech to text)
        text = r.recognize_google(audio_data)
        print(text)

        time_now = dt.now()  # get current time of PS change
        new_time = time_now.strftime("%m-%d-%Y_%H-%M-%S")
        with open('speechtext_' + new_time + '.txt', 'w') as f:
            f.write(text)
