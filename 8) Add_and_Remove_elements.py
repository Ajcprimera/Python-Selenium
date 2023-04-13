import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

class addremove(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
        driver = self.driver
        driver.get("http://the-internet.herokuapp.com")
        driver.maximize_window()
        driver.find_element(By.LINK_TEXT,'Add/Remove Elements').click()
        driver.implicitly_wait(15)

    def test_add_remove(self):
        driver = self.driver
        elements_added = int(input('How many elements will you add?: '))
        elements_removed = int(input('How many elements will you remove?: '))
        total_elements = elements_added-elements_removed
        add_button = driver.find_element(By.XPATH, '//*[@id="content"]/div/button')

        sleep(3)
        for i in range(elements_added):
            #este ciclo for nos permite clickear la cantidad de veces que indico el usuario
            add_button.click()

        for i in range(elements_removed):
            #el manejo nos errores nos ayuda a que si el usuario introdujo una mayor cantida que elementos
            #a borrar este nos va a el error
            try:
                delete_button = driver.find_element(By.XPATH,'//*[@id="elements"]/button[1]')
                delete_button.click()
            except:
                print('You are trying to delete more elements the existent')
                break
        
        if total_elements > 0:
            print(f'there are {total_elements} on the screen')
            #Nos muestra la cantidad de elementos en la pagina
        else:
            print('there are 0 elements on the screen')
        sleep(3)

    def tearDown(self) :
        self.driver.close()

if __name__ == '__main__':
    unittest.main(verbosity=2)