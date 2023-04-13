import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep


class dynamicElements(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
        driver = self.driver
        driver.get("http://the-internet.herokuapp.com")
        driver.maximize_window()
        driver.find_element(By.LINK_TEXT,'Disappearing Elements').click()
        driver.implicitly_wait(15)
    
    def test_dynamic_elements(self):
        driver = self.driver
        tries = 1
        #Capturo los elementos de la lista
        elements = driver.find_elements(By.TAG_NAME,'li')

        while len(elements) < 5:
            #Si los elementos que encontré son menores a 5 recargo la pagina y vuelvo a "contar" los elementos de la lista
            print('Elements in the list', len(elements))
            driver.refresh()
            elements = driver.find_elements(By.TAG_NAME,'li')
            #Sumo otro intento
            tries += 1
            #Espero 1 segundo para que poder ver cuántas veces ha recargado
            sleep(3)

        print(f'it tooks {tries} tries to catch Gallery')

    def tearDown(self) :
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)