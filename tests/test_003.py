from Estructura.funciones.functions import Functions as Selenium
import unittest


class Test(Selenium, unittest.TestCase):


    def setUp(self):
        Selenium.abrir_navegador(self, URL="https://www.w3schools.com/js/tryit.asp?filename=tryjs_alert")
        Selenium.page_has_loaded(self)
        Selenium.switch_to_iframe(self, "//*[@id='iframeResult']")
        Selenium.esperar_elemento(self, "/html/body/button")
        Selenium.esperar(self, 5)
        Selenium.alert_windows(self, "Accept")
        Selenium.esperar(5)

    def tearDown(self):
        pass


    def testName(self):
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()