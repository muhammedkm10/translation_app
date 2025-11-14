import os
from googletrans import Translator

def translate_text_sync(text, source_lang, target_lang):
    try:
        print(text,source_lang,target_lang)
        translator = Translator()
        result = translator.translate(text, src=source_lang, dest=target_lang)
        print('my result',result.text)
        return {"status":True ,"result":result.text}
    except Exception as e:
        return {"status":False ,"result":str(e)}