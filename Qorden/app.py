import gradio as gr
import requests
import Translator
from helpers import language_headers
from helpers import make_header, upload_file, request_transcript, make_polling_endpoint, wait_for_completion, \
    make_paras_string
def change_audio_source(radio, file_data, mic_data):

    if radio == "Audio File":
        sample_rate, audio_data = file_data
        return [gr.Audio.update(visible=True),
                gr.Audio.update(visible=False)]

    elif radio == "Record Audio":
        sample_rate, audio_data = mic_data
        return [gr.Audio.update(visible=False),
                gr.Audio.update(visible=True)]
def submit_to_AAI(radio,
                  audio_file,
                  mic_recording):
    api_key="cf171c0d3d8348cc9844c2c7edc13b55"
    header = make_header(api_key)
    if radio == "Audio File":
        audio_data = audio_file
    elif radio == "Record Audio":
        audio_data = mic_recording

    upload_url = upload_file(audio_data, header, is_file=False)
    transcript_response = request_transcript(upload_url, header)
    polling_endpoint = make_polling_endpoint(transcript_response)
    wait_for_completion(polling_endpoint, header)
    r = requests.get(polling_endpoint, headers=header).json()
    transc_id = r['id']
    paras = make_paras_string(transc_id, header)
    paras=Translator.translation_class(paras,'ar')
    return paras

with open('styles.css', 'r') as f:
    css = f.read()

with gr.Blocks(css=css) as demo:
    gr.HTML('<img src="logo.jpg" class="logo"></a>')
    gr.HTML("<h1 class='title'>Transliteration Software</h1>"
            "<br>"
            "<p>Check out the <a href="">Real-time call translation</a> Making life easier.</p>")


    radio = gr.Radio(["Audio File", "Record Audio"], label="Audio Source", value="Audio File")

    audio_file = gr.Audio()
    mic_recording = gr.Audio(source="microphone", visible=False)
    file_data = gr.State([1, [0]])  # [sample rate, [data]]
    mic_data = gr.State([1, [0]])  # [Sample rate, [data]]


    language = gr.Dropdown(
        choices=list(language_headers.keys()),
        value="US English",
        label="Language Specification",
        visible=True,
    )

    submit = gr.Button('Submit')

    with gr.Tab('Transcript'):
        trans_tab = gr.Textbox(placeholder="Your formatted transcript will appear here ...",
                               show_label=False)

    radio.change(fn=change_audio_source,
                 inputs=[radio,file_data,
                     mic_data],
                 outputs=[
                     audio_file,
                     mic_recording])

    submit.click(fn=submit_to_AAI,
                 inputs=[radio,
                         audio_file,
                         mic_recording],
                 outputs=trans_tab
                          )

demo.launch(share=True)
