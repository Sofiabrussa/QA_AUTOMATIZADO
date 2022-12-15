import os

class Inicializar(): 
    # Directorio base
    basedir = os.path.abspath(os.path.join(__file__, "../.."))
    DateFormat = "%d/%m/%Y"

    # JsonData
    vari = basedir + u"\pages"
    json = basedir + u"\pages"
    
    enviroment = "Test" #en que ambiente se esta probando 
    
    # Directorio de evidencia 
    Path_Evidencias = basedir + u"/data/capturas"
    
    nave = u"Firefox"
    URL = "https://siged.test.cba.gov.ar/"

    
    