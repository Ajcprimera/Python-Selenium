import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class dynamicControls(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
        driver = self.driver
        driver.get("http://the-internet.herokuapp.com")
        driver.maximize_window()
        driver.find_element(By.LINK_TEXT,'Dynamic Controls').click()
        driver.implicitly_wait(15)

    def test_dynamic_controls(self):
        driver = self.driver
        checkbox = driver.find_element(By.CSS_SELECTOR, '#checkbox')
        checkbox.click()

        remove_add = driver.find_element(By.CSS_SELECTOR, '#checkbox-example > button')
        remove_add.click()

        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#checkbox-example > button')))
        #esperamos hasta que el boton este habilitado

        enable_disable = driver.find_element(By.CSS_SELECTOR, '#input-example > button')
        enable_disable.click()

        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#input-example > button')))
        #hacemos los mismo, pero ahora con el boton de habilitar y deshabilitar
        text_area = driver.find_element(By.CSS_SELECTOR, '#input-example > input[type=text]')
        text_area.send_keys('platzi')
        enable_disable.click()

    def tearDown(self) :
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)