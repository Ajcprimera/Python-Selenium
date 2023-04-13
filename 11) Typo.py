import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

class typos(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
        driver = self.driver
        driver.get("http://the-internet.herokuapp.com")
        driver.maximize_window()
        driver.find_element(By.LINK_TEXT,'Typos').click()
        driver.implicitly_wait(15)

    def test_find_typo(self):
        driver = self.driver

        paragraph = driver.find_element(By.CSS_SELECTOR, '#content > div > p:nth-child(3)')
        text_check = paragraph.text
        print(text_check)
        tries = 1
        correct_text = "Sometimes you'll see a typo, other times you won't."

        while text_check != correct_text:
            #mientras el texto sea diferente al que estamos intentado 
            #ver la correfcion, este se va a seguir ejecutando
            driver.refresh()
            text_check = driver.find_element(By.CSS_SELECTOR, '#content > div > p:nth-child(3)').text
            tries +=1
            #refrescamos la pagina hasta que aparesca
        if tries == 1:
            print('it tooks one try')
        else:
            print(f"It took {tries} tries to find the types")

        


    def tearDown(self) :
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)