# Banja Voice Module (BVM)
- BVM is a soon to be part of [Banja](https://github.com/stevemats/BanjaTranscriber) module that will be responsible for live and audio transcription. 

- BVM currently gives you two options:
1. Transcribe recorded audio to text e.g from a meeting &c.
2. Transcribe a live audio e.g a speech in a meeting or court room, and transcribe it to readable text.

## Installation

``` $ git clone https://github.com/stevemats/BVM ```

## How to run BVM
- Change directory to BVM, then run below commands:

``` $ pip3 install -r requirements.txt```

- To recognize the text of an audio file named 
`16-122828-0002.wav`:
    ```
    python recognizer.py 16-122828-0002.wav
    ```
    **Output**:
    ```
    I believe you're just talking nonsense
    ```
- To recognize the text from your microphone after talking 5 seconds:
    ```
    python live_recognizer.py 5
    ```
    This will record your talking in 5 seconds and then uploads the audio data to Google to get the desired output.
    
<center><br> Coming Soon !</br></center>