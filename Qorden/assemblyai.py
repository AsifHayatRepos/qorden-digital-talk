import requests
import time

def read_file(filename):
   with open(filename, 'rb') as _file:
       while True:
           data = _file.read(5242880)
           if not data:
               break
           yield data
def assembly(data):
    UPLOAD_ENDPOINT = "https://api.assemblyai.com/v2/upload"
    TRANSCRIPTION_ENDPOINT = "https://api.assemblyai.com/v2/transcript"
    api_key = "cf171c0d3d8348cc9844c2c7edc13b55"
    headers = {"authorization": api_key, "content-type": "application/json"}
    upload_response = requests.post(UPLOAD_ENDPOINT, headers=headers, data=data)
    audio_url = upload_response.json()["upload_url"]
    transcript_request = {'audio_url': audio_url}
    transcript_response = requests.post(TRANSCRIPTION_ENDPOINT, json=transcript_request, headers=headers)
    _id = transcript_response.json()["id"]
    while True:
        polling_response = requests.get(TRANSCRIPTION_ENDPOINT + "/" + _id, headers=headers)

        if polling_response.json()['status'] == 'completed':
            text = polling_response.json()['text']
            return text
            break
        elif polling_response.json()['status'] == 'error':
            raise Exception("Transcription failed. Make sure a valid API key has been used.")
        else:
            print("Processing ...")
            time.sleep(5)