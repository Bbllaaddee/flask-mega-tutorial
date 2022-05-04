import json
import requests
from flask import current_app
from flask_babel import _

def translate(text, source_language, dest_language):
    headers = {'Content-Type': 'application/json'}

    r = requests.post('https://libretranslate.de/translate', headers=headers,
            json={'q': text, 'source': source_language, 'target': dest_language, 'format': "text"})


    if r.status_code != 200:
        print(r.json())
        return _('Error: translation service failed')

    return r.json()['translatedText']
