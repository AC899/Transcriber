#https://www.thepythoncode.com/article/using-speech-recognition-to-convert-speech-to-text-python
import speech_recognition as sr

filename = "/Users/anilcarrier/Desktop/DONT_DESPISE_THE_DETOUR_MAY_2022bmck1.wav"
r = sr.Recognizer()

with sr.AudioFile(filename) as file:
    data = r.record(file)
    text = r.recognize_google(data)
    print(text)