from denoise import AudioDeNoise
import Translator
import TTS
import assemblyai
import os
from gtts import gTTS
import Real_stream

recording = Real_stream.recording()
audio = assemblyai.read_file('output.wav')
text=assemblyai.assembly(audio)
trans_text = Translator.translation_class(text,'arabic')
print(trans_text)
tts = gTTS(trans_text, lang='ar', slow=False)
tts.save('hello.mp3')
os.remove('output.wav')
