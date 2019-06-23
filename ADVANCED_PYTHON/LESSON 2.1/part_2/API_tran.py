import requests

URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'


def translate_it(origlan, needlang='ru'):
    API_KEY = 'trnsl.1.1.20190515T233613Z.f09f527824630250.6b980ff5cda887b12f51b95d9c5d50bd765ab3ac'  # мой ключ
    params = {
        'key': API_KEY,
        'text': origlan,
        'lang': '{}'.format(needlang.lower())
        }

    if origlan == '':
        raise ValueError

    response = requests.get(URL, params=params)
    text = response.json()
    return text

if __name__ == '__main__':
    print(translate_it('car', "ru")['text'][0])

