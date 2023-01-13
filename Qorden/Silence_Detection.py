from pydub import AudioSegment, silence
import warnings

warnings.filterwarnings('ignore')
myaudio = AudioSegment.from_wav("voice.wav")
silence = silence.detect_silence(myaudio, min_silence_len=1000, silence_thresh=-16)
silence = [((start/1000),(stop/1000)) for start,stop in silence] #convert to sec
print(silence)