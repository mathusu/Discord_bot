import speech_recognition as sr
import time

r = sr.Recognizer()

with sr.AudioFile('C:\\Users\\Usuario\\Desktop\\Repositorio_GitHub\\Clases_python\\Proyecto_bot_maxi\\maxi1-40segs.wav') as source:
    audio = r.listen(source)

    try:
        print("leyendo archivo")
        text = r.recognize_google(audio, language='es-ES')
        time.sleep(2)
        print(text)
        print("Audio finalizado")
    except:
        print("No entendi una kajeta ura")

# PARA AUDIO ahlol.wav Entendimiento mediocre debido a la cantidad de personas hablando