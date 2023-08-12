import speech_recognition as sr
#from google_trans_new import google_translator
from deep_translator import GoogleTranslator
from gtts import gTTS
#import pyaudio
from playsound import playsound

r = sr.Recognizer()
translator = GoogleTranslator()

with sr.Microphone() as source:
    print("SPEAK NOW. . . .")
    audio = r.listen(source)
    try:
        speech_text = r.recognize_google(audio)
        print(speech_text)
    except sr.UnknownValueError:
        print("Could not understand")
    except sr.RequestError:
        print("Could not request result from google")

    #translated_text = translator.translate(speech_text, lang_tgt="fr")

    translated_text = GoogleTranslator(source='auto', target='de').translate(speech_text)

    #translated_text = translator.translate(speech_text, lang_src='en', lang_tgt='pt')
    print(translated_text)

    voice = gTTS(translated_text, lang="es")
    voice.save("voice.mp3")
    #pyaudio("voice.mp3")
    playsound("voice.mp3")
