from pprint import pprint
import requests
import time
import json

TOKEN = "d3c0f1924c15827420b1c5b32104a799a66da408fbe5abb363e2ffb89faa80f31301879e685cbeb00a239"
ID = "171691064"
NAME = "eshmargunov"

def benchmark(func):
    def times(*args, **kw):
        start = time.time()
        rezult = func(*args, **kw)
        end = time.time()
        print(' It takes {} sec.'.format(end - start))
        return rezult
    return times

class Groups:

    def __init__(self, user_id):
        self.user_id = user_id
        self.params = {
            'user_id': self.user_id,
            'access_token': TOKEN,
            'v': '5.92',
            'fields': 'domain'
        }

    def __str__(self):
        return 'https://vk.com/id' + self.user_id

    def mygroup(self): # output all groups
        response = requests.get('https://api.vk.com/method/groups.get', self.params)  # status code
        data_mygroup = response.json()  # get dict id groups
        mygroup_set = set()
        mygroup_set = data_mygroup['response']['items']
        print(len(mygroup_set), " groups in the studied profile")
        return mygroup_set # get list id groups

    @benchmark
    def myfriends_groups(self): # all groups of friends
        response = requests.get('https://api.vk.com/method/friends.get', self.params)  # status code
        myfriends = response.json()  # get dict friends
        myfriends_list = []
        for myfriend in myfriends['response']['items']:# cycle without closed  and delened profiles
            if myfriend.get('is_closed') != "false" and myfriend.get('deactivated') != 'deleted':
                myfriends_list.append(myfriend['id'])
        print(len(myfriends_list), "/", len(myfriends['response']['items'])," friends without closed and deleted profiles")

        myfriends_and_groups = {}
        i = 0

        for id_friends in myfriends_list:
            time.sleep(0.4)
            self.params = {
                'user_id': id_friends,
                'access_token': TOKEN,
                'v': '5.92',
                'fields': 'domain'
            }
            response = requests.get('https://api.vk.com/method/groups.get', self.params) # status code
            data_friendsgroup = response.json()  # get dict id groups
            if 'response' in data_friendsgroup.keys():
                myfriends_and_groups[id_friends] = data_friendsgroup['response']['items']
                i += 1

                print(i, "/", len(myfriends_list), 'find: ', len(data_friendsgroup['response']['items']), 'group(s)')
        return myfriends_and_groups# get list id groups


@benchmark
def spy_game(my_list_group, dict_friends_group):
    rezult = my_list_group #
    outdata = {} # dict characteristic_group
    outdata_all = [] # list outdata
    i = 0

    for group in my_list_group: # "spy list of groups"
        for group_friend in dict_friends_group:
            for i in dict_friends_group[group_friend]:
                if group == i and i in rezult:
                    rezult.remove(group)
    print('user is spy in these groups(id): ', rezult)

    for id in rezult:
        params = {
            'group_id': id,
            'access_token': TOKEN,
            'v': '5.92',
            'fields': 'domain'
        }
        response = requests.get('https://api.vk.com/method/groups.getById', params)  # status code
        data_group = response.json()  # get name and id groups
        outdata['name'] = data_group['response'][0]['name']
        outdata['gid'] = data_group['response'][0]['id']
        response = requests.get('https://api.vk.com/method/groups.getMembers', params) # status code
        data_group = response.json() # get count groups
        outdata['members_count'] = data_group['response']['count']
        outdata_all.append(str(outdata))
    print('geting info about groups')
    pprint(outdata_all)
    print('start data output in json')
    with open('diplom.json', 'w', encoding='utf-8') as f:
        json.dump(outdata_all, f)
    print('done!')
    return outdata_all

if __name__ == "__main__":
    spy_game(Groups(ID).mygroup(), Groups(ID).myfriends_groups())
