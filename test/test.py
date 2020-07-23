import os
from time import sleep
import speech_recognition as sr

# obtain audio from the microphone
r = sr.Recognizer()


def play(text_str):
    # os.system(f"gtts-cli -l 'bn' '{text_str}' | mpg321 -")
    print(text_str)
    # sleep(5)


def recog():
    with sr.Microphone() as source:
        print('*' * 80)
        print('ready')
        print('say... ')
        r.adjust_for_ambient_noise(source)
        rec = r.listen(source, timeout=7)
    try:
        text = r.recognize_google(rec, language='bn-BD')
        if text is None:
            play('বুঝতে পারি নি, আবার বলুন।')
        return text
    except sr.UnknownValueError:
        print("could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Cloud Speech service; {0}".format(e))


if __name__ == '__main__':
    text = recog()
    print(text)
