import requests
import time
import datetime
import sys
import os
import re
import heapq
from pprint import pprint
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from ErrorsVK import ErrorsVK

ACCESS_TOKEN = ""
ERRORSVK = ErrorsVK.errors_from_vk

class Id_user:
    def __init__(self, token: str, name: str):
        self.user_info = {}
        self.token = token
        self.name = str(name)
        self.fields = 'domain'  # запрашиваемые поля в методах/required fields
        self.params = {
            'access_token': self.token,
            'v': '5.92',
            'fields': self.fields
        }
        # проверка на данные ID/ check for ID data
        try:
            if self.name.isdigit():
                self.params['user_id'] = self.name
            elif self.name[0:1] == 'id' and self.name[2:].isdigit():
                self.params['user_id'] = self.name[2:]
            else:
                self.params['user_ids'] = self.name
                response = requests.get('https://api.vk.com/method/users.get', self.params)
                data_user = response.json()
                self.params['user_id'] = data_user['response'][0]['id']
                del self.params['user_ids']
        except KeyError:
            error = data_user['error']['error_code']
            print('Код ошибки: ', error, '\n Описание ошибки: ', ERRORSVK.setdefault(error, 'неизвестная ошибка'))
            return None

    def get_info(self):
        try:
            # получение информации возраста, пола, интересов
            self.params['fields'] = 'bdate, city, sex, interests, books, music, games, relation, movies'
            response = requests.get('https://api.vk.com/method/users.get', self.params)
            data_user = response.json()
            if not data_user.get('error'):
                if not data_user['response'][0].get('deactivated') == 'deleted' and not data_user['response'][0].get('is_closed') == True:
                    self.user_info['Имя'] = data_user['response'][0].setdefault('first_name', 'скрыто')
                    self.user_info['Фамилия'] = data_user['response'][0].setdefault('last_name', 'скрыто')
                    self.birth = data_user['response'][0].setdefault('bdate', 'скрыто')
                    if self.birth == 'скрыто' or len(self.birth.split('.')) != 3:
                        while True:
                            self.age = input('введите Ваш возраст (от 16 лет)\n')
                            if int(self.age) >= 16:
                                break
                    else:
                        birth = [int(x) for x in self.birth.split('.')]
                        birth.reverse()
                        d = datetime.date(*birth)
                        self.age = (datetime.date.today() - d).days // 365
                    self.user_info['День рождения'] = self.birth
                    self.user_info['Возраст'] = int(self.age)
                    self.city = data_user['response'][0].setdefault('city', '')
                    if self.city:
                        self.user_info['Контактная информация'] = self.city['title']
                    else:
                        self.user_info['Контактная информация'] = input(
                            'Контактная информация (Наименование населенного пункта\n')
                    self.games = data_user['response'][0].setdefault('games', '')
                    self.user_info['Любимые игры'] = self.games
                    self.movies = data_user['response'][0].setdefault('movies', '')
                    self.user_info['Любимые фильмы'] = self.movies
                    self.music = data_user['response'][0].setdefault('music', '')
                    self.user_info['Любимая музыка'] = self.music
                    self.sex = data_user['response'][0].setdefault('sex', 'скрыто')
                    if self.sex == 1:
                        self.user_info['Пол'] = 'Женский'
                    elif self.sex == 2:
                        self.user_info['Пол'] = 'Мужской'
                    else:
                        self.user_info['Пол'] = input('Выберите пол (Мужской\Женский): \n')
                    self.interests = data_user['response'][0].setdefault('interests', '')
                    self.user_info['Интересы'] = self.interests
                    self.books = data_user['response'][0].setdefault('books', '')
                    self.user_info['Любымие книги'] = self.books
                    # pprint(self.user_info)
                else:
                    print('''
Невозможно собрать информацию пользователя
пользователь удален/ или у пользователя закрытый профиль
                    ''')
                    return None
            else:
                error = data_user['error']['error_code']
                print('Код ошибки: ', error, '\n Описание ошибки: ', ERRORSVK.setdefault(error, 'неизвестная ошибка'))
                return None
        except KeyError:
            error = data_user['error']['error_code']
            print('Код ошибки: ', error, '\n Описание ошибки: ', ERRORSVK.setdefault(error, 'неизвестная ошибка'))
            return None

    def search(self):
        self.get_info()
        del self.params['user_id']
        if int(self.age) <= 21:
            self.params['age_from'] = 16
        else:
            self.params['age_from'] = int(self.age) - 5
        self.params['age_to'] = int(self.age) + 5
        self.params['has_photo'] = 1
        self.params['count'] = 1000
        if self.user_info['Пол'] == 'Женский':
            self.params['sex'] = 2
        else:
            self.params['sex'] = 1
        self.params['status'] = 6

        self.params_city = {
            'access_token': self.token,
            'v': '5.92',
            'country_id': 1,
            'need_all': 0,
        }
        city_from_user = input(f'Ваш город: {self.user_info["Контактная информация"]} введите 1 для поиска в этом '
                               f'городе, или название другого города (не более 15 симв) \n')
        if city_from_user == '1':
            self.params_city['q'] = self.user_info['Контактная информация'][0:14]
        else:
            self.params_city['q'] = city_from_user
        response_city = requests.get('https://api.vk.com/method/database.getCities', self.params_city)
        data_city = response_city.json()
        self.params['city'] = data_city['response']['items'][0]['id']
        response = requests.get('https://api.vk.com/method/users.search', self.params)
        data_people = response.json()
        weight = {
            'interests': 5,
            'book': 3,
            'music': 2,
            'games': 1,
            'movies': 2,
        }
        self.candidates = []
        for love in data_people['response']['items']:
            point = 0
            music_weight = re.split(", ", love.setdefault('music', ''))
            if music_weight != '' and self.music != '':
                general_music = set(music_weight).intersection(set(re.split(", ", self.music)))
                if general_music is not None:
                    point += weight['music'] * len(general_music)
            book_weight = re.split(", ", love.setdefault('books', ''))
            if book_weight != '' and self.books != '':
                general_book = set(book_weight).intersection(set(re.split(", ", self.books)))
                if general_book != None:
                    point += weight['music'] * len(general_book)
            games_weight = re.split(", ", love.setdefault('games', ''))
            if games_weight != '' and self.games != '':
                general_game = set(games_weight).intersection(set(re.split(", ", self.games)))
                if general_game != None:
                    point += weight['games'] * len(general_game)
            movies_weight = re.split(", ", love.setdefault('movies', ''))
            if movies_weight != '' and self.movies != '':
                general_movie = set(movies_weight).intersection(set(re.split(", ", self.movies)))
                if general_movie != None:
                    point += weight['movies'] * len(general_movie)
            interests_weight = re.split(", ", love.setdefault('interests', ''))
            if interests_weight != '' and self.interests != '':
                general_interests = set(interests_weight).intersection(set(re.split(", ", self.interests)))
                if general_interests != None:
                    point += weight['interests'] * len(general_interests)
            if len(self.candidates) < 30:
                self.candidates.append([point, love['id']])
            else:
                self.candidates.append([point, love['id']])
                heapq.heappop(self.candidates)

    def find_foto(self):
        result = []
        for candidate in self.candidates:
            self.params_photo = {
                'access_token': self.token,
                'v': '5.95',
                'owner_id': candidate[1],
                'count ': 1000,
                "album_id": 'profile',
                'extended': 1
            }
            response = requests.get('https://api.vk.com/method/photos.get', self.params_photo)
            time.sleep(0.4)
            data_foto_user = response.json()
            dict_photos = []
            if not data_foto_user.get('error'):
                for photo in data_foto_user['response']['items']:
                    finded_photos = dict()
                    likes = photo['likes']['count']
                    finded_photos = {
                        'likes': likes,
                        'url': ''
                    }
                    for size in photo['sizes']:
                        if size['type'] == 's' and not finded_photos['url']:
                            finded_photos['url'] = size['url']
                        elif size['type'] == 'r':
                            finded_photos['url'] = size['url']
                    dict_photos.append(finded_photos)
                sorted_dict_photos = sorted(dict_photos, key=lambda k: k['likes'])
                urls = []
                for link in sorted_dict_photos[-3:]:
                    urls.append(link['url'])
                result.append([candidate[0], candidate[1], urls])
            result.sort(reverse=True)
        print(result)
        return result

    def __str__(self):
        return 'https://vk.com/id' + str(self.params['user_id'])

if __name__ == "__main__":
    try:
        polina = Id_user(ACCESS_TOKEN, "2324405")
        print(polina)
        polina.search()
        polina.find_foto()
        # polina.search()
        # polina.find_foto()

    except NameError as name:
        print(f"{name}| enter string!")

