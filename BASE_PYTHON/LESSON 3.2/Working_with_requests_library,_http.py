import requests
import os
# API_KEY = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

def translate_it(waytoorigfile, waytonewfiletran, origlan, needlang='ru'):
    API_KEY = 'trnsl.1.1.20190515T233613Z.f09f527824630250.6b980ff5cda887b12f51b95d9c5d50bd765ab3ac'  # мой ключ
    with open(waytoorigfile, "r", encoding="utf-8") as text:
        params = {
            'key': API_KEY,
            'text': text.read(),
            'lang': '{}-{}'.format(origlan.lower(), needlang.lower())
        }
        response = requests.get(URL, params=params)
        json_ = response.json()
        
        with open(waytonewfiletran, 'w') as rezult:
            rezult.write(''.join(json_['text']))


files = ["DE", "ES", "FR"]
translate_it(r"C:\Users\Дмитрий\PycharmProjects\111\venv\2.8 API\3.2.http.requests\DE.txt",r"C:\Users\Дмитрий\PycharmProjects\111\venv\2.8 API\3.2.http.requests\111.txt", "de")
