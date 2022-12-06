from Estructura.funciones.inicializar import Inicializar 
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from Estructura.pages.variables_Siged import Variables as var
from selenium.webdriver.common.by import By




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
        

##############################################################################

    def xpath_elemento(self, XPATH):
        element = self.driver.find_element(By.XPATH, XPATH)
        return element
    

    




         
