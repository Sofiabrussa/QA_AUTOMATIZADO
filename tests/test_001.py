from Estructura.funciones.functions import Functions as Selenium
from Estructura.pages.variables_Siged import Variables as var
import unittest
import time


class test_001(Selenium, unittest.TestCase):
    
    def setUp(self):
        Selenium.abrir_navegador(self)
    
         
    def test_001(self):
        #INICIO DE SESION 
        #Selenium.xpath_elemento(self, var.txt_cuil).send_keys(var.usuario)
        Selenium.send_keys(self, var.txt_cuil, var.usuario)
        Selenium.send_keys(self, var.txt_contra, var.contra)
        Selenium.xpath_elemento(self, var.boton_ingresar).click()
        time.sleep(3)
        
        #BANDEJA DE CONSULTA 
        time.sleep(3)
        Selenium.xpath_elemento(self, var.tramites).click()
        Selenium.xpath_elemento(self, var.consulta).click()
        Selenium.xpath_elemento(self, var.filtro_tramite).send_keys("3379")
        
        Selenium.action_chains(self, var.boton_consultar)
        time.sleep(5)
        
    
        #INICIAR UN TRAMITE PERSONA DOCUMENTADA
        Selenium.esperar_elemento(self, var.nuevo_tramite, )
        time.sleep(3)
       
        
        
    
    def tearDown(self):
        Selenium.tearDown(self)
    

if __name__ == "__main__":
    unittest.main()


    