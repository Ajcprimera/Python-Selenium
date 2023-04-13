import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By 
from time import sleep
#Esta libreria nos ayuda a poner un tiempo de pausa entre cada cosa que deseemos realizar

class automatizedNavigation(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
        driver = self.driver
        driver.get("https://www.google.com/")
        driver.maximize_window()
        driver.implicitly_wait(15)

    def test_browser_navigation(self):
        driver = self.driver
        search_field = driver.find_element(By.NAME, 'q')
        search_field.clear()
        search_field.send_keys('platzi')
        search_field.submit()

        driver.back()
        #Retroceder en el navegador
        sleep(3)
        driver.forward()
        #Nos permite avanzar a la pagina en la que estabamos
        sleep(3)
        #Ponemos un tiempo de espera de 3 seg
        driver.refresh()
        #Nos permite refrescar el navegador
        sleep(3)

    def tearDown(self) :
        self.driver.close()

if __name__ == '__main__':
    unittest.main(verbosity=2)