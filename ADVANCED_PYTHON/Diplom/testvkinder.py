import unittest
from User import user
from db import db
import json
import time

ACCESS_TOKEN = ''

class TestVkinder(unittest.TestCase):


    def test(self):  # проверка истинность
        name = user.Id_user(ACCESS_TOKEN, "2324405")
        self.assertTrue(name)  # проверка на истинность

    def test_code(self):  # Проверка на равенство
        time.sleep(0.3)
        name = user.Id_user(ACCESS_TOKEN, "2324405")
        self.assertEqual(str(name), 'https://vk.com/id2324405')


if __name__ == '__main__':
    unittest.main()  # Запуск теста