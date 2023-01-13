from denoise import AudioDeNoise

def Noise_Removal(audiofile):
    audioDenoiser = AudioDeNoise(audiofile)
    audio_filtered = audioDenoiser.deNoise()
    return audio_filtered

audio=Noise_Removal('voice.wav')
print(audio)