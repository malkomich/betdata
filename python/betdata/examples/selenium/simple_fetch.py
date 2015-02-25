from selenium import webdriver
import selenium.webdriver.support.ui as ui


# SELENIUM FOR DUMMIES #

# Configurar el driver para firefox (se puede usar chrome tambien)
profile = webdriver.FirefoxProfile()
browser = webdriver.Firefox(firefox_profile=profile)

# Primera peticion, la semilla que desecadenara todo
browser.get('http://www.livescore.com/')

# La lista de ligas

# La funcion wait es muy util para decirle a selenium que se para hasta que aparezca tal elemento.
# Por ejemplo, cuando se cargan cosas por ajax, formularios... o cualquier incluso en la carga inicial (se tarda
# un tiempo en descargar la pagina completa, aunque sean milisegundos)

wait = ui.WebDriverWait(browser, 20)          #el tiempo de espera

#Las funciones lambda son muy practicas porque se pueden definir "inline".
elems = wait.until(lambda browser: browser.find_elements_by_class_name("row"))
#La linea anterior de manera tradicional seria
'''
def callback(browser):
    return browser.find_elements_by_class_name("row")

elems = wait.until(callback)
'''

'''
Puedes usar: 'find_elements_by_class_name' para obtener un conjunto de elementos con esa clase (html, el atributo class)
             'find_element_by_class_name' lo mismo pero solo devuelve uno. Util cuando sabes que es unico (en vez de obtener un array de tamano 1)
Lo mismo para atributos id o cualquier otro tipo, no te costara encontrar todos los tipos en google
'''

# Como ves con la funcion lambda es mucho mas rapido y claro (como un atajo) pero si te parece lioso puedes usar el
# metodo tradicional de definir una funcion y pasarla como callback
#for elem in elems:
    # A su vez a cada elemento tambien puedes hacer un find_elements (que estaria acotado a solo ese elemento)
    # Por ejemplo, imagina que has hecho un browser.find_elements_by_tag_name("table") para obtener todas las tablas.
    # Luego a cada tabla le puedes hacer elem.find_elements_by_tag_name("tr") para iterar por sus filas
    # Tambien puedes simular clicks, escribir letras (para campos de texto), etc.
    # Mira https://selenium.googlecode.com/git/docs/api/py/webdriver_remote/selenium.webdriver.remote.webelement.html
    #print elem.text

# Vamos a obtener todas las ligas utilizando lo que ya sabemos
# Es muy util firebug e "inspeccionar codigo" para saber que tags o class tienen los elementos que queeremos



# Ver todas las ligas
content = wait.until(lambda browser: browser.find_element_by_class_name("content"))
#for league in content.find_elements_by_class_name("row"):
#    print league.find_element_by_class_name("left").text, "Fecha:", league.find_element_by_class_name("right").text

#Crear array
leagues = []
last_league = None #La liga actual, None es como el null de java
# Almacenar en un diccionario todas las ligas y sus partidos
# XPATH es la herramienta mas potente pero tambien la mas compleja. Vamos a ver un ejemplo
# Lo que hago es buscar todos los elementos con la clase "row" (correspondiente al nombre de la liga) o con "row-gray" (correspondiente a un partido)
# Dependiendo del tipo (si es liga o partido) hago una cosa u otra
for elem in content.find_elements_by_xpath("//div[contains(@class, 'row') or contains(@class, 'row-gray')]"):
    if elem.get_attribute("class") == "row row-tall mt4":
        # Cuando encontramos una liga nueva, miramos si el partido actual es nulo (solo ocurre en la primera iteracion)
        # y si no lo es, lo insertamos (esto sucede en cada cambio de liga)
        # El problema aqui es que la lista esta hecha "a pelo", unas entradas detras de otras en vez de una estructura
        # mas "amigable". Normalmente suelen tener una estructura mas facilona

        if last_league is not None:
            leagues.append(last_league)

        league_name = elem.find_element_by_tag_name("strong").text

        #Creamos un diccionario para guardar los datos de la nueva liga
        last_league = {
                "name": league_name,
                "matches": []
            }




    elif elem.get_attribute("class").startswith('row-gray'): #Uso el startswitch para que pille tanto "row-gray" como "row-gray even"
        #Un partido
        teams = elem.find_elements_by_class_name("ply")
        home_team = teams[0].text
        visitor_team = teams[1].text
        match_result = elem.find_element_by_class_name("sco").text
        match = {
            "home": home_team,
            "visitor": visitor_team,
            "result": match_result
        }
        last_league['matches'].append(match)


# Mostrar los datos
print leagues
#Ahora que lo tiene todo en un array bien bonito puedes hacer con los datos lo quieras (como guardarlos en base de datos, continuar "procesandolos", etc

#Este array que he sacado necesitaria ajustarte al formato de como se quieren guardar los datos (por ejemplo el tema de los goles, en vez de guardar el string "2 - 1"
# pues separarlo y poner como integer a cada equipo sus correspondientes goles y demas


#Como has visto, la unica dificultad aqui ha sido pensar las manera de recorrer el DOM, todo lo demas re reduce a "find_element_tal_y_cual" y recorrer arrays