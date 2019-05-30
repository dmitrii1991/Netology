from pprint import pprint
import requests

TOKEN = "08a1586aa9e1103673bf886dd93958bbeb8b543f494874c1d21629ccf51af742d9802822f71df6e1488f6"

class Our_friends:


    def __init__(self, user_id):
        self.user_id = user_id

    def __str__(self):
        return 'https://vk.com/id' + self.user_id


    def friends(self):  #список друзей
        params = {
            'user_id': self.user_id,
            'access_token': TOKEN,
            'v': '5.92',
            'fields': 'domain'
        }
        response = requests.get('https://api.vk.com/method/friends.get', params) # код состояния
        data_users = response.json()  # Получение всех друзей
        users_set = set()
        for user in data_users['response']['items']:  # Записываем всех друзей в список
            users_set.add(user['id'])
        return users_set


    def __and__(self, other):
        user_friends = list(self.friends() & other.friends())
        user_list = [Our_friends(i) for i in user_friends]
        print(user_list, "323")


if __name__ == "__main__":
    user_1 = Our_friends('703347')
    user_2 = Our_friends('17041800')
    # pprint(user_1.friends())
    user_1 & user_2
    print(user_1)
    print(user_2)
