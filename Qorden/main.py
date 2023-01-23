from gtts import gTTS

import Translator
import assemblyai

global api_key

api_key = "cf171c0d3d8348cc9844c2c7edc13b55"

def main(audio):
    #recording = Real_stream.recording()
    #audio = assemblyai.read_file('output.wav')
    text = assemblyai.assembly(audio)
    trans_text = Translator.translation_class(text,'arabic')
    print(trans_text)
    tts = gTTS(trans_text, lang='ar', slow=False)
    #tts.save('hello.mp3')
    #os.remove('output.wav')
    return tts

