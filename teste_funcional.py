from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.nav = webdriver.Chrome()

    def tearDown(self):
        self.nav.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith ouviu falar de uma nova aplicação interessante
        # Lista de tarefas. Verificar a homepage
        self.nav.get('http://localhost:8000')

        # Ela percebe que o titulo da pagina e o cabecalho mencionam lista de tarefas (to-do)
        self.assertIn('To-do', self.nav.title)
        self.fail('Finish the test!')


if __name__ == '__main__':
    unittest.main(warnings='ignore')

