import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By 

class compareProducts(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
        driver = self.driver
        driver.get("http://demo-store.seleniumacademy.com")
        driver.maximize_window()
        driver.implicitly_wait(15)

    def test_compare_products(self):
        driver = self.driver
        search_field = driver.find_element(By.NAME, 'q')
        search_field.clear()
        #una muy buena practica es limpiar los campos de textos para verificar que no contengan nada
        search_field.send_keys('tee')
        #enviamos las palabras enviadas por el teclado
        search_field.submit()
        #nos permite darle enter para que inicie la busquedad

        driver.find_element(By.CLASS_NAME, 'link-compare').click()
        driver.find_element(By.LINK_TEXT, 'Clear All').click()

        alert = driver.switch_to.alert
        #nos permite cambiar el foco hacia la alerta que nos esta mandando la pagina
        alert_text = alert.text
        #obtenemos el texto de la alerts
        self.assertEqual('Are you sure you would like to remove all products from your comparison?', alert_text)
        #verificamos que sea el mismo que el de la alerta como validacion
        alert.accept()
        #le damos OK a la alerta

    def tearDown(self) :
        self.driver.close()

if __name__ == '__main__':
    unittest.main(verbosity=2)