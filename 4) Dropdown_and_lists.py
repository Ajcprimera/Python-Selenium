import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import Select

class find_elements(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
        driver = self.driver
        driver.get("http://demo-store.seleniumacademy.com")
        driver.maximize_window()
        driver.implicitly_wait(15)

    def test_select_language(self):
        exp_option = ['English', 'French', 'German']
        #Lista de idiomas 
        act_option = []
        #Son las opciones del dropdown que se iran accediendo
        select_language = Select(self.driver.find_elements(By.ID, 'select-language'))
        self.assertEqual(3, len(select_language.options))
        for option in select_language.options:
            act_option.append(option.text)
            #Agregamos la opciones a la lista vacia
        
        self.assertListEqual(exp_option, act_option)
        #Verificamos si la cantidad de elementos es la misma de la lista que acbamos
        self.assertEqual('English', select_language.first_selected_option.text)
        select_language.select_by_visible_text('German')
        self.assertTrue('german' in self.driver.current_url)
        select_language = Select(self.driver.find_elements(By.ID,'select-language'))
        select_language.select_by_index(0)
    
    def tearDown(self) :
        self.driver.implicitly_wait(3)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)