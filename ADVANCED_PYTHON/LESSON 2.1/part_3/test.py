import unittest
from yand.py import *

class Secretary_program(unittest.TestCase):

    def setUp(self):
        self.dima = Yandex('maksimus.maksi', '19911')

    def test_selenium(self):
        print(self.dima)
        self.assertEqual(self.dima.auto(), 'maksimus.maksi')


if __name__ == '__main__':
    unittest.main()  # Запуск теста
