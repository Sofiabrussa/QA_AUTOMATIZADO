import unittest
from Estructura.funciones.functions import Functions as Selenium

class test_002(Selenium, unittest.TestCase):


    def setUp(self):
        Selenium.abrir_navegador(self, URL="https://www.mercadolibre.com.ar/")
        #Selenium.new_window(self, "https://www.mercadolibre.com.ar/gz/home/navigation#nav-header")
        Selenium.scroll_to(self, "//*[@id='root-app']/div/div/section[4]/div/div[1]/a")
        Selenium.esperar(self, 4)
        Selenium.js_clic(self, "//*[@id='root-app']/div/div/section[4]/div/div[1]/a")
        Selenium.esperar(self, 4)
        Selenium.send_keys(self, "//*[@id='user_id']", "sofiabrussa@gmail.com")
        Selenium.esperar(self, 2)
        Selenium.send_specific_keys(self, "//*[@id='user_id']", "Enter")
        



    def tearDown(self):
        pass


    def testName(self):
        pass


if __name__ == "__main__":
    unittest.main()