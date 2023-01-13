from denoise import AudioDeNoise
import Translator
import TTS
import assemblyai

audio=assemblyai.read_file('voice.wav')
text=assemblyai.assembly(audio)
trans_text = Translator.translation_class(text,'arabic')
print(trans_text)
TTS.STT(trans_text)