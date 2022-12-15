from Estructura.funciones.functions import Functions as Selenium
import unittest


class Test(Selenium, unittest.TestCase):


    def setUp(self):
        Selenium.abrir_navegador(self, URL="https://www.youtube.com/")
        Selenium.esperar(self, 4)
        Selenium.get_text(self, "//*[@id='text']")
        Selenium.get_text(self, "//*[@id='endpoint']/tp-yt-paper-item/yt-formatted-string")
        Selenium.esperar(self, 3)
        Selenium.save_variable_scenary(self, "//*[@id='text']", "categoria")
        
        Selenium.new_window(self, "https://www.google.com/")
        Selenium.switch_to_ventana(self, "https://www.google.com/")
        Selenium.esperar(self, 3)
        variable = Selenium.get_variable_scenary(self, "categoria")
        Selenium.send_keys(self, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input", variable)
        
        
    def tearDown(self):
        pass


    def testName(self):
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()