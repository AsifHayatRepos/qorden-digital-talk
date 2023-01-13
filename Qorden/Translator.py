from deep_translator import GoogleTranslator
def translation_class(text,language):
    trans = GoogleTranslator(source='auto', target=language).translate(text)
    return trans