from Estructura.funciones.inicializar import Inicializar 
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from Estructura.pages.variables_Siged import Variables as var
from selenium.webdriver.common.by import By
import os 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException, NoSuchElementException




class Functions(Inicializar):    
    def abrir_navegador (self, URL=Inicializar.URL, navegador=Inicializar.nave):
        print(Inicializar.basedir)
        self.ventanas = {}
        print("------------------")
        print(navegador)
        print("------------------")
        
        if navegador == ("Firefox"):
            self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
            self.driver.implicitly_wait(10)
            self.driver.maximize_window()
            self.driver.get(URL)
            self.principal = self.driver.window_handles[0] #Se utiliza para poder desplazarse entre ventanas
            self.ventanas = {"Principal":self.driver.window_handles[0]}
            print(self.ventanas)
            return self.driver

    def tearDown(self):
        print("Se cerrara el DRIVER")
        self.driver.quit()
        

###############################################################################
########################FUNCION BUSCAR ELEMENTO################################

    def xpath_elemento(self, XPATH):
        element = self.driver.find_element(By.XPATH, XPATH)
        return element

###############################################################################
#############################FUNCION WAIT  ####################################

    def esperar_elemento(self, XPATH, MyTextElement=None):  
        try:
            wait = WebDriverWait(self.driver,20)
            if MyTextElement is not None:
                self.XPATH = self.XPATH.format(MyTextElement)
                print(XPATH)
                
            wait.until(EC.element_to_be_clickable((By.XPATH, XPATH))).click()
            print("El elemento a esperar es:", XPATH)
            return True
            
        except TimeoutException:
            print(u"Elemento no presente")
            Functions.tearDown(self)
        
        except NoSuchElementException:
            print(u"Elemento no presente")
            Functions.tearDown(self)
            
      
###############################################################################
##########################ACTION CHAINS########################################

    def action_chains(self, XPATH):
        time.sleep(3)
        self.localizador = self.driver.find_element(By.XPATH, XPATH )
        action = ActionChains(self.driver)
        action.move_to_element(self.localizador).click().perform()


        
    
    



         
