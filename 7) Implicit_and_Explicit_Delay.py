import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

class explicitDelay(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
        driver = self.driver
        driver.get("http://demo-store.seleniumacademy.com")
        driver.maximize_window()
        driver.implicitly_wait(15)

    def test_account_link(self):
        WebDriverWait(self.driver, 10).until(lambda s: s.find_element(By.ID, 'select-language').get_attribute('length')=='3')
        #Esperamos 10 seg hasta que se cumpla la funcion
        account =  WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, 'ACCOUNT')))
        account.click()

    
    def test_create_new_customer(self):
        self.driver.find_element(By.LINK_TEXT, 'ACCOUNT')
        my_account = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT,'My Account')))
        #Esperamos un tiempo de 10 seg hasta que se loccalice el elemento
        my_account.click()

        create_my_account = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, 'CREATE AN ACCOUNT')))
        #De igual manera que el anterior esparamos un tiempo determindo de 20 seg hasta que el elemento sea localizado
        create_my_account.click()

        WebDriverWait(self.driver, 10).until(EC.title_contains('Create New Customer Account'))

    def tearDown(self) :
        self.driver.close()

if __name__ == '__main__':
    unittest.main(verbosity=2)