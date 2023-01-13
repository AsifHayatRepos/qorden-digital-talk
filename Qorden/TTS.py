import pyttsx3
engine = pyttsx3.init()
def rate():
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 125)
    return rate

def volume():
    volume = engine.getProperty('volume')
    engine.setProperty('volume',1.0)
    return volume

def voices():
    voices = engine.getProperty('voices')
    #engine.setProperty('voice', voices[0].id)
    engine.setProperty('voice', voices[0].id)
    return voices

def change_voice(engine, language, gender='VoiceGenderFemale'):
    for voice in engine.getProperty('voices'):
        if language in voice.languages and gender == voice.gender:
            engine.setProperty('voice', voice.id)
            return True
    raise RuntimeError("Language '{}' for gender '{}' not found".format(language, gender))

def STT(text):
    engine.say(text)
    engine.runAndWait()
    engine.stop()
    engine.runAndWait()