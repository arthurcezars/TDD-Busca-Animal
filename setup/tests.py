from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By

class AnimaisTestCase(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome('D:\Repositorio Local\Alura\Programacao\Formação Django\TDD no Django\chromedriver.exe')

    def tearDown(self):
        self.browser.quit()

    def test_buscando_um_novo_animal(self):
        """
        Teste se um usuário encontra um animal pesquisando
        """

        home_page = self.browser.get(self.live_server_url + '/')
        brand_element = self.browser.find_element(By.CSS_SELECTOR, '.navbar')
        self.assertEqual('Busca Animal', brand_element.text)
