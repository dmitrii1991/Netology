import unittest
from secretary_program_ import *

class Secretary_program(unittest.TestCase):

    def setUp(self):  # запускается перед выполнением каждого теста в классе

        pass

    def test_check_document_existance(self):
        self.assertEqual(check_document_existance("2207 876234"), True)  # Проверка на равенство
        self.assertNotEqual(check_document_existance("2207"), True)

    def test_get_all_doc_owners_names(self):
        self.assertIn("Аристарх Павлов", get_doc_owner_name('10006'))

    def tearDown(self):  # запускается после каждого теста в классе
        pass

if __name__ == '__main__':
    unittest.main()  # Запуск теста
