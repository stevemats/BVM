#!/usr/bin/env/python

#----------------------------------------------------------------
# A journey of a thousand miles starts with one step!
# https://github.com/stevemats/BVM
#----------------------------------------------------------------

from modules.recorded.la_audiorec import *
from modules.recorded.sm_audiorec import short_recognizer
from modules.live.live_recognizer import live_recognizer 



def banner():
    print("""


        ____              _        __      __   _            __  __           _       _      
        |  _ \            (_)       \ \    / /  (_)          |  \/  |         | |     | |     
        | |_) | __ _ _ __  _  __ _   \ \  / /__  _  ___ ___  | \  / | ___   __| |_   _| | ___ 
        |  _ < / _` | '_ \| |/ _` |   \ \/ / _ \| |/ __/ _ \ | |\/| |/ _ \ / _` | | | | |/ _ /
        | |_) | (_| | | | | | (_| |    \  / (_) | | (_|  __/ | |  | | (_) | (_| | |_| | |  __/
        |____/ \__,_|_| |_| |\__,_|     \/ \___/|_|\___\___| |_|  |_|\___/ \__,_|\__,_|_|\___|
                         _/ |                                                                 
                        |___|

        [x] Modeler: Steve Matindi
        [x] About: Transcription module for transcribing audio     
        [x] Usage Demo  : $ python bvm.py 

    """)

def main():
    print('\n1. Convert Small Recorded Audio to Text (fast)')
    print('2. Convert Large Recorded Audio to Text')
    print('3. Convert Live audio/Speech to Text')
    print('4. Exit')

    while True:
        try:
            choice = int(input('Enter choice: '))
            if choice == 1:
                short_recognizer()
                break
            elif choice == 2:
                get_large_audio_transcription()
                break
            elif choice == 3:
                live_recognizer()
                break
            elif choice == 4:
                print("\n", "GoodBye!")
                break
            else:
                print("Invalid choice. Enter a choice in menu. 1 or 2")
                main()
        except ValueError:
            print("Invalid choice. Enter 1 or 2")
    exit()


if __name__ == '__main__':
    banner()
    main()
