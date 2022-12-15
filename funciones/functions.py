from Estructura.funciones.inicializar import Inicializar 
from selenium import webdriver
import re
from webdriver_manager.firefox import GeckoDriverManager
from Estructura.pages.variables_Siged import Variables as var
from selenium.webdriver.common.by import By
import os 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException, NoSuchElementException,\
    NoAlertPresentException, NoSuchWindowException
from selenium.webdriver.support.ui import Select
from gettext import find
from _pytest.python import Function
from Estructura.funciones import inicializar
from pip._vendor.distlib.locators import Locator
from pickle import TRUE
from selenium.webdriver.common.keys import Keys
import openpyxl
Scenario = {}


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


###############################################################################
#########################SELECT################################################

    def select(self, XPATH):
        select = Select(self.driver.find_element(By.XPATH, XPATH))
        return select
        

###############################################################################
###########################IFRAME##############################################


    def switch_to_iframe(self, locator):
        iframe = self.driver.find_element(By.XPATH, locator)
        self.driver.switch_to.frame(iframe)
        

##################################################################################
########################SELECT BY TEXT############################################

    def select_by_text(self, xpath, text):
        get_xpath=Functions.select(self, xpath)
        get_xpath.select_by_visible_text(text)


##################################################################################
########################NEW_VENTANA###############################################

    def new_ventana(self, ventana="new_ventana"):
        new_window = self.driver.current_window_handle
        self.ventanas[ventana] = new_window
        self.driver.switch_to.window(self.ventanas[ventana])
        self.driver.maximize_window()
        print(self.ventanas)
        print("Estas en" + ventana + ":" + self.ventanas[ventana])
        
    def new_window(self, URL): #Se abre pestaña nueva con javascript
        self.driver.execute_script(f"window.open('{URL}','_blank');")
        Functions.page_has_loaded(self)
        

##################################################################################
#############################SEND SPECIFIC KEYS###################################

    def send_specific_keys(self, element, key):
        
        if key == "Enter":
            Functions.xpath_elemento(self, element).send_keys(Keys.ENTER)
        if key == "Tab":
            Functions.xpath_elemento(self, element).send_keys(Keys.TAB)
        if key == "Space":
            Functions.xpath_elemento(self, element).send_keys(Keys.SPACE)
        
            
##################################################################################
################################SEND KEYS#########################################            
            
    def send_keys(self, element, text):
        self.driver.find_element(By.XPATH, element).send_keys(text)
    
##################################################################################
###########################GET TEXT###############################################   
    
    def get_text(self, locator, MyTextElement = None):
        if MyTextElement is not None:
            self.locator = self.locator.format(MyTextElement)
            print(self.locator)
        elements = self.driver.find_element(By.XPATH, locator)
        
        print("get_text: " + locator)
        print("Text Value: " + elements.text)
        return elements.text   

##################################################################################
#################################MANEJO VENTANAS################################## 
    def page_has_loaded(self):
        driver = self.driver
        print("Checking if {} page is loaded".format(self.driver.current_url))#verifica url
        WebDriverWait(driver, 20).until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
        print("Pagina cargada")          
    
    
    def switch_to_ventana(self, ventana):
        if ventana in self.ventanas: #si la ventana existe, salata aca
            time.sleep(5)
            self.driver.switch_to.window(self.ventanas[ventana])
            Functions.page_has_loaded(self)
            print("Volviendo a" + ventana + ":" + self.ventanas[ventana])
        
        else: #si la venatana no existe, la agrega al diccionario y hace salto 
            time.sleep(5)
            self.nwindows = len(self.driver.window_handles) - 1
            self.ventanas[ventana] = self.driver.window_handles[int(self.nwindows)]
            self.driver.switch_to.window(self.ventanas[ventana])
            self.driver.maximize_window()
            print(self.ventanas)
            print("Estas en " + ventana + ":" + self.ventanas[ventana])
            Functions.page_has_loaded
    
    
#####################################################################################
###########################################JAVASCRIPT CLICK##########################

    def js_clic(self, locator, MyTextElement=None):
        Functions.esperar_elemento(self, locator, MyTextElement)
        
        try:
            if MyTextElement is not None:
                self.locator = self.locator.format(MyTextElement)
                print(self.locator)
            
                localizador = self.driver.find_element(By.XPATH, locator)
                self.driver.execute_script("arguments[0].click();", localizador)
                print(u"Se hizo click en:" + locator)
                return True
        
        except TimeoutException:
            print(u"js_click : No presente" + locator)
            Functions.tearDown(self)
            
            
######################################################################################
##########################################SCROLL######################################

    def scroll_to(self, locator):
        
        try:
            localizador = self.driver.find_element(By.XPATH, locator)
            self.driver.execute_script("arguments[0].scrollIntoView();", localizador)
            print(u"scroll_to: " + locator)
            return True
        
        
        except TimeoutException:
            print(u"Scroll_to : No se encontro")
            Functions.tearDown(self)
    

######################################################################################
########################################ESPERAR#######################################

    def esperar(self, timeLoad):
        print("Esperar: Inicia("+str(timeLoad)+")")
                
        try:
                totalWait = 0
                while (totalWait < timeLoad):
                    time.sleep(1)
                    totalWait = totalWait + 1
                    print(totalWait)
        finally:
            print("Esperar: Carga finalizada")


######################################################################################
######################################ALERT WINDOWS###################################

    def alert_windows(self, accept="accept"):
        
        try:
            wait= WebDriverWait(self.driver, 30)
            wait.until(EC.alert_is_present(), print("Esperando alerta...")) #espera una alerta 
            
            alert= self.driver.switch_to.alert #vamos a la ventana
            
            print(alert.text)
            
            if accept.lower() == "accept":
                alert.accept()
                print("Click in accept")
            else:
                alert.dismiss()
                print("Click in Dismiss")
                
        
        except TimeoutException:
            print("Alerta no presente")
        except NoAlertPresentException:
            print("Alerta no presente")
        except NoSuchWindowException:
            print("Alerta no presente")
            
    
    #####################################################################################
    #####################################ASSERT Y VERIFICATION###########################
    #Assert: Es si esta o no el objeto y listo
    #VERIFICACION: Esta el objeto y que hago
    
    def check_element(self, locator): #Devuelve true o false si esta o no el elemento
        
        try:
            wait = WebDriverWait(self.driver, 15)
            wait.until(EC.visibility_of_element_located((By.XPATH, locator)))
            print(u"check element: Se visualizo el elemento" + locator)
            return True
            
        except TimeoutException:
            print(u"No se encontro el elemento" + locator)
            return False
        except NoSuchElementException:
            print(u"No se encontro el elemento")
            return False
    
    
    def assert_text(self, locator, text): 
        objtext = self.driver.find_element(By.XPATH, locator).text
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.presence_of_element_located((By.XPATH, locator)))
    
        print("El valor mostrado en: " + locator + " es: " + objtext + " y el esperado es: " + text)
        assert text == objtext, "Los valores comparados no coinciden"
    
    
##########################################################################################
##################################DICCIONARIOS############################################

    def save_variable_scenary(self, element, variable):
        Scenario[variable] = Functions.get_text(self, element)
        print(Scenario)
        print("Se almaceno el valor: " + variable + " : " + Scenario[variable])
            
    def get_variable_scenary(self, variable):
        self.variable = Scenario[variable]
        print(f"get_variable_scenary: {self.variable}")
        return self.variable
        
    def compare_with_variable(self, element, variable):
        variable_scenary = str(Scenario[variable])
        element_text = str(Functions.get_text(self, element))
        _exist = (variable_scenary in element_text)
        print("Verificando si: " + variable_scenary + " esta presente en: " + element_text)
        assert variable_scenary in element_text, f"{variable_scenary} != {element_text}"
    
    
###########################################################################################
##############################CAPTURA DE PANTALLA##########################################


    def crear_path(self):
        def hora_actual():
            hora = time.strftime("%H%M%S")
            return hora
        dia = time.strftime("%d-$m-%Y")
        
        GeneralPath = Inicializar.Path_Evidencias
        DriverTest = Inicializar.nave
        TestCase = self.__class__.__name__ #extrae el nombre de la clase
        horaAct = hora_actual()
        x = re.search("Context", TestCase)
        if (x):
            path = GeneralPath + "/" + dia + "/" + DriverTest + "/" + horaAct + "/"
        else: 
            path = GeneralPath + "/" + dia + "/" + TestCase + "/" + DriverTest + "/" + horaAct + "/"
        
        if not os.path.exists(path):
            os.makedirs(path)
        return path


    
    
    
    
    
    
    
    
    
    
    
    
    
          
            
            
