from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.ui as ui
import sys

def regionExists(region):

    reglist = ['euw', 'na', 'eune', 'las', 'oce', 'kr', 'lan', 'br', 'ru', 'tr']

    if str.lower(region) in reglist:
        return True
    else:
        return False


summoner = sys.argv[1]
region = sys.argv[2]

if (len(sys.argv) == 3) and (regionExists(region)):

    # Configurar el driver para firefox
    profile = webdriver.FirefoxProfile()
    browser = webdriver.Firefox(firefox_profile=profile)

    # Peticion a la pagina
    browser.get('https://wasted-on-lol.com/')

    wait = ui.WebDriverWait(browser, 10)

    regionButton = wait.until(lambda browser: browser.find_element_by_id("choose_region"))
    regionButton.click()

    labels = wait.until(lambda browser:browser.find_elements_by_xpath("//*[@id='head_modal_region']/div/div/label"))

    cont = 0
    contLabel = 0
    for reg in browser.find_elements_by_xpath("//*[@id='head_modal_region']/div/div/label/div/input"):
        cont += 1
        if reg.get_attribute("value") == str.lower(region):
            contLabel = cont

    labels[contLabel-1].click()
    close = wait.until(lambda browser: browser.find_element_by_xpath("//*[@id='head_modal_region']/div/a"))
    close.click()

    inputText = wait.until(lambda browser: browser.find_element_by_id("head_search"))
    inputText.send_keys(summoner, Keys.ENTER)

    try:
        cadLevelRank = wait.until(lambda browser: browser.find_element_by_id("player_level").text).split(" ")
        level = cadLevelRank[1]
        rank = cadLevelRank[3]
        div = cadLevelRank[4]
        horas = wait.until(lambda browser: browser.find_element_by_id("time_wasted_h").text)
        dias = wait.until(lambda browser: browser.find_element_by_id("time_wasted_j").text)
        print("Invocador: " + summoner + " Nivel: " + level)
        print("Clasificatoria: " + rank + " " + div)
        print("Horas: " + horas + " Dias: " + dias)
    except:
        print(summoner + " no existe en " + region)


else:
    if not regionExists(region):
        print("La region indicada no es valida")
    else:
        print("Error en los argumentos. El comando ha de ser: python wastedOnLol.py <Nombre de invocador> <Region>")
