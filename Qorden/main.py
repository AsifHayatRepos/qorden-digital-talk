from gtts import gTTS

import Translator
import assemblyai
import Real_stream
global api_key

api_key = "cf171c0d3d8348cc9844c2c7edc13b55"
def sts(recorded_file, target_language, speech_language, output_path):

    #recording = Real_stream.recording()
    audio = assemblyai.read_file(recorded_file)
    text = assemblyai.assembly(audio)
    trans_text = Translator.translation_class(text, target_language)
    print(trans_text)
    tts = gTTS(trans_text, lang=speech_language, slow=False)
    tts.save(output_path)

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
        description='Speech to Speech translation')
    parser.add_argument('--recorded_file', required=True,
        help='Path to the audio file')
    parser.add_argument('--target_language', default='arabic',
        help='Target translation language')
    parser.add_argument('--speech_language', default='ar',
        help='Write en for english, ar for arabic or follow gTTS language code')
    parser.add_argument('--output_path', required=True,
        help='Pass output Path for converted file')

    args = parser.parse_args()
    sts(args.recorded_file, args.target_language, args.speech_language,args.output_path)
