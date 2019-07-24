from User import user
from db import db
import json

ACCESS_TOKEN = ""

def find_love(token, id):
    user1 = user.Id_user(token, id)
    try:
        user1.search()
        result = user1.find_foto()
        return result
    except KeyError:
        return None

users = find_love(ACCESS_TOKEN, "304436454")
if users:
    # create_db("vkinder_db", "postgres", "1234")
    # add_users(users, "vkinder_db", "postgres", "1234")
    data_json = []
    for user in users:
        data_json.append({'points': user[0], 'id': user[1], 'foto': user[2]})
    with open('data.json', 'w') as f:
        json.dump(data_json, f)
else:
    print('Ошибка')
