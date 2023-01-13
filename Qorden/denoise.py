import numpy as np
import pywt
import soundfile
from tqdm import tqdm
import warnings
warnings.filterwarnings("ignore")
from lib.noiseProfiler import NoiseProfiler


def mad(arr):
    arr = np.ma.array(arr).compressed()
    med = np.median(arr)
    return np.median(np.abs(arr - med))


class AudioDeNoise:


    def __init__(self, inputFile):
        self.__inputFile = inputFile
        self.__noiseProfile = None

    def deNoise(self):

        info = soundfile.info(self.__inputFile)  # getting info of the audio
        rate = info.samplerate
        for block in tqdm(soundfile.blocks(self.__inputFile, int(rate * info.duration * 0.10))):
            coefficients = pywt.wavedec(block, 'db4', mode='per', level=2)
            sigma = mad(coefficients[- 1])
            thresh = sigma * np.sqrt(2 * np.log(len(block)))
            coefficients[1:] = (pywt.threshold(i, value=thresh, mode='soft') for i in coefficients[1:])
            clean = pywt.waverec(coefficients, 'db4', mode='per')
            return clean

    def generateNoiseProfile(self, noiseFile):

        data, rate = soundfile.read(noiseFile)
        self.__noiseProfile = NoiseProfiler(data)
        noiseSignal = self.__noiseProfile.getNoiseDataPredicted()

        soundfile.write(noiseFile, noiseSignal, rate)

    def __del__(self):

        del self.__noiseProfile
