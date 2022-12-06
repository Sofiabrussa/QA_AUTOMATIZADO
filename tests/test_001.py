from Estructura.funciones.functions import Functions as Selenium
from Estructura.pages.variables_Siged import Variables as var
import unittest
import time


class test_001(Selenium, unittest.TestCase):
    
    def setUp(self):
        Selenium.abrir_navegador(self)
    
         
    def test_001(self):
        #INICIO DE SESION 
        Selenium.xpath_elemento(self, var.txt_cuil).send_keys(var.usuario)
        Selenium.xpath_elemento(self, var.txt_contra).send_keys(var.contra)
        Selenium.xpath_elemento(self, var.boton_ingresar).click()
        time.sleep(5)
        
        #Controlar ingreso al sistema correcto
        assert Selenium.xpath_elemento(self, var.titulo).text == "SAS"
        print(Selenium.xpath_elemento(self, var.titulo).text)
    
    def tearDown(self):
        Selenium.tearDown(self)
    

if __name__ == "__main__":
    unittest.main()


    