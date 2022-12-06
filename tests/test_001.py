from selenium.webdriver.common.by import By
from Estructura.funciones.functions import Functions as Selenium
from Estructura.pages.variables_Siged import Variables as var
import unittest
import time

class test_001(Selenium, var, unittest.TestCase):
    
    def setUp(self):
        Selenium.abrir_navegador(self)
        self.driver.find_element(By.XPATH, var.txt_cuil).send_keys(var.usuario)
        self.driver.find_element(By.XPATH, var.txt_contra).send_keys(var.contra)
        self.driver.find_element(By.XPATH, var.boton_ingresar).click()
        time.sleep(5)
         
    def test_001(self):
        pass
    
    def tearDown(self):
        Selenium.tearDown(self)
    

if __name__ == "__main__":
    unittest.main()


    