import gradio as gr
import plotly.express as px
import requests

from helpers import language_headers
from helpers import make_header, upload_file, request_transcript, make_polling_endpoint, wait_for_completion, \
    make_paras_string


def change_audio_source(radio, file_data, mic_data):

    if radio == "Audio File":
        sample_rate, audio_data = file_data
        return [gr.Audio.update(visible=True),
                gr.Audio.update(visible=False),
             ]
    elif radio == "Record Audio":
        sample_rate, audio_data = mic_data
        return [gr.Audio.update(visible=False),
                gr.Audio.update(visible=True)]

def create_output(paras, language, transc_opts=None):
    if transc_opts is None:
        transc_opts = ['Automatic Language Detection', 'Speaker Labels', 'Filter Profanity']


    return [language, paras]


def submit_to_AAI(api_key,
                  radio,
                  audio_file,
                  mic_recording):
    # Make request header
    header = make_header(api_key)

    # Select which audio to use
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
    return create_output(r, paras, language)



with open('styles.css', 'r') as f:
    css = f.read()

with gr.Blocks(css=css) as demo:
    gr.HTML('<img src="logo.jpg" class="logo"></a>')
    gr.HTML("<h1 class='title'>Transliteration Software</h1>"
            "<br>"
            "<p>Check out the <a href="">Real-time call translation</a> Making life easier.</p>")

    with gr.Box():
        gr.HTML("<p class=\"apikey\">API Key:</p>")
        api_key = gr.Textbox(label="", elem_id="pw")


    radio = gr.Radio(["Audio File", "Record Audio"], label="Audio Source", value="Audio File")

    audio_file = gr.Audio()
    mic_recording = gr.Audio(source="microphone", visible=False)
    plot = gr.State(px.line(labels={'x': 'Time (s)', 'y': ''}))
    file_data = gr.State([1, [0]])  # [sample rate, [data]]
    mic_data = gr.State([1, [0]])  # [Sample rate, [data]]


    language = gr.Dropdown(
        choices=list(language_headers.keys()),
        value="US English",
        label="Language Specification",
        visible=False,
    )

    submit = gr.Button('Submit')

    with gr.Tab('Transcript'):
        trans_tab = gr.Textbox(placeholder="Your formatted transcript will appear here ...",
                               show_label=False)

    radio.change(fn=change_audio_source,
                 inputs=[
                     radio,file_data,
                     mic_data],
                 outputs=[
                     audio_file,
                     mic_recording])

    submit.click(fn=submit_to_AAI,
                 inputs=[api_key,
                         radio,
                         audio_file,
                         mic_recording],
                 outputs=trans_tab
                          )

demo.launch()
