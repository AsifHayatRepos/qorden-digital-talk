import requests
import time
from denoise import AudioDeNoise


UPLOAD_ENDPOINT = "https://api.assemblyai.com/v2/upload"
TRANSCRIPTION_ENDPOINT = "https://api.assemblyai.com/v2/transcript"
api_key = "<YOUR-API-KEY-HERE>"
headers = {"authorization": api_key, "content-type": "application/json"}

def read_file(filename):
   with open(filename, 'rb') as _file:
       while True:
           data = _file.read(5242880)
           if not data:
               break
           yield data

def Noise_Removal(audiofile):
    audioDenoiser = AudioDeNoise(audiofile)
    audio_filtered = audioDenoiser.deNoise()
    return audio_filtered

audio=Noise_Removal('voice.wav')
upload_response = requests.post(UPLOAD_ENDPOINT, headers=headers, data=audio)
audio_url = upload_response.json()["upload_url"]

transcript_request = {'audio_url': audio_url}
transcript_response = requests.post(TRANSCRIPTION_ENDPOINT, json=transcript_request, headers=headers)
_id = transcript_response.json()["id"]

while True:
    polling_response = requests.get(TRANSCRIPTION_ENDPOINT + "/" + _id, headers=headers)
    if polling_response.json()['status'] == 'completed':
        with open(f'{_id}.txt', 'w') as f:
            f.write(polling_response.json()['text'])
        print('Transcript saved to', _id, '.txt')
        break
    # If the transcription has failed, raise an Exception
    elif polling_response.json()['status'] == 'error':
        raise Exception("Transcription failed. Make sure a valid API key has been used.")
    # Otherwise, print that the transcription is in progress
    else:
        print("Transcription queued or processing ...")
        time.sleep(5)