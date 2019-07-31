from User import user
from db import db
import json

ACCESS_TOKEN = ""

def find_love(token, id):

    user1 = user.Id_user(token, id)
    try:
        user1.search()
        users = user1.find_foto()
        if users:
            db.create_db("vkinder_db", "postgres", "1234")
            db.add_users(users, "vkinder_db", "postgres", "1234")
            data_json = []
            for u in users:
                data_json.append({'points': u[0], 'id': u[1], 'foto': u[2]})
            with open('data.json', 'w') as f:
                json.dump(data_json, f)
        else:
            print('Ошибка')
        return users
    except KeyError:
        return None

if __name__ == '__main__':
    find_love(ACCESS_TOKEN, "304436454")
