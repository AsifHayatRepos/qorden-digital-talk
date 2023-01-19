import sounddevice as sd
from scipy.io.wavfile import write

def recording():
    print('Recording')
    fs = 44100  # Sample rate
    seconds = 4  # Duration of recording
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()  # Wait until recording is finished
    print('Done')
    write('output.wav', fs, myrecording)