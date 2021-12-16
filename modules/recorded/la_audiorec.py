# importing libraries
import speech_recognition as sr
import os
from pydub import AudioSegment
from datetime import datetime as dt
from pydub.silence import split_on_silence

# create a speech recognition object
r = sr.Recognizer()

# a function that splits the audio file into chunks
# and applies speech recognition
def get_large_audio_transcription():

    # audio path
    path = input('Enter path to audio:')

    """
    Splitting the large audio file into chunks
    and apply speech recognition on each of these chunks
    """
    # open the audio file using pydub
    sound = AudioSegment.from_wav(path)
    # split audio sound where silence is 700 miliseconds or more and get chunks
    chunks = split_on_silence(sound,
                              # experiment with this value for your target audio file
                              min_silence_len=500,
                              # adjust this per requirement
                              silence_thresh=sound.dBFS-14,
                              # keep the silence for 1 second, adjustable as well
                              keep_silence=500,
                              )
    folder_name = "audio-chunks"
    # create a directory to store the audio chunks
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)
    whole_text = ""
    # process each chunk
    for i, audio_chunk in enumerate(chunks, start=1):
        # export audio chunk and save it in
        # the `folder_name` directory.
        chunk_filename = os.path.join(folder_name, f"chunk{i}.wav")
        audio_chunk.export(chunk_filename, format="wav")
        # recognize the chunk
        with sr.AudioFile(chunk_filename) as source:
            audio_listened = r.record(source)
            # try converting it to text
            try:
                text = r.recognize_google(audio_listened)
            except sr.UnknownValueError as e:
                print("Error:", str(e))
            else:
                text = f"{text.capitalize()}. "
                print(chunk_filename, ":", text)
                whole_text += text
    # return the text for all chunks detected
    print("\nFull text:", whole_text)
    time_now = dt.now()  # get current time of PS change
    new_time = time_now.strftime("%m-%d-%Y_%H-%M-%S")
    with open('speechtext_' + new_time + '.txt', 'w') as f:
        f.write(whole_text)
    
# testing
# if __name__ == '__main__':
#     # import sys
#     # path = "30-4447-0004.wav"
#     # path = "7601-291468-0006.wav"
#     # path = input('Enter path to audio:')
#     print("\nFull text:", get_large_audio_transcription())
