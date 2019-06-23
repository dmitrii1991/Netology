import unittest
from API_tran import *

class Secretary_program(unittest.TestCase):

    def setUp(self):
        pass

    def test_translate_it(self):
        self.assertEqual(translate_it('car', 'ru')['text'][0], 'автомобиль')

    def test_code(self):
        self.assertEqual(translate_it('car', 'ru')['code'], 200)

    def test_wrong_arg(self):
        self.assertRaises(ValueError, translate_it, '', needlang='ru')

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()  # Запуск теста
