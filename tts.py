from gtts import gTTS
from playsound import playsound
import os

ls = os.path.dirname(os.path.abspath(__file__))

def tts(text, lang='en'):
    tts = gTTS(text = text, lang = lang, slow = True)

    new_file = "speech.mp3"
    path = os.path.join(ls, new_file)
    tts.save(new_file)

    playsound(new_file)
    # os.remove(new_file)

if __name__ == "__main__":
    input_text = input("Enter text: \n")
    tts(input_text)