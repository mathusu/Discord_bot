import pyaudio

# Crear un objeto PyAudio
audio = pyaudio.PyAudio()

# Obtener el número de dispositivos de entrada disponibles
num_dispositivos = audio.get_device_count()

print("Dispositivos de entrada disponibles:")
for i in range(num_dispositivos):
    dispositivo_info = audio.get_device_info_by_index(i)
    print(f"Dispositivo {i}: {dispositivo_info['name']}")