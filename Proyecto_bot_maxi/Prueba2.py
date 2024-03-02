import pyaudio

def print_device_info():
    p = pyaudio.PyAudio()
    print("Dispositivos de entrada:")
    for i in range(p.get_device_count()):
        dev_info = p.get_device_info_by_index(i)
        if dev_info['maxInputChannels'] > 0:
            print("ID:", i, "- Nombre:", dev_info['name'], "- Canales:", dev_info['maxInputChannels'])
    
    print("\nDispositivos de salida:")
    for i in range(p.get_device_count()):
        dev_info = p.get_device_info_by_index(i)
        if dev_info['maxOutputChannels'] > 0:
            print("ID:", i, "- Nombre:", dev_info['name'], "- Canales:", dev_info['maxOutputChannels'])

print_device_info()