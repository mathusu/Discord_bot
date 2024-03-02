import pyaudio
import speech_recognition as sr
import time

audio = pyaudio.PyAudio()

chunk = 1024
formato = pyaudio.paInt16
canales = 1
tasa_muestreo = 44100
duración_grabación = 5


recognizer = sr.Recognizer()

def reconocer_audio(audio_data):
    try:
        audio_data = sr.AudioData(audio_data, tasa_muestreo, 2)
        text = recognizer.recognize_google(audio_data, language='es-ES')  
        time.sleep(1)
        print("Texto reconocido:", text)

    except sr.UnknownValueError:
        time.sleep(1)
        print("No se pudo entender el audio")

    except sr.RequestError as e:
        print("Error al conectarse al servicio de reconocimiento de voz de Google; {0}".format(e))


stream = audio.open(format=formato, channels=canales, rate=tasa_muestreo, input=True, frames_per_buffer=chunk, device_index=3)

print("Escuchando...")

for i in range(0, int(tasa_muestreo / chunk * duración_grabación)):
    audio_data = stream.read(chunk)
    reconocer_audio(audio_data)

stream.stop_stream()
stream.close()
audio.terminate()