import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class HelloWorld(unittest.TestCase):
    @classmethod
    #El decorador nos permite ejecutar las pruebas en una sola pagina
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
        cls.driver.implicitly_wait(10)
    
    #las 2 funciones que se muestran nos van a permitir ejecutar y mostrar las paginas en chrome
    def test_hello_world(self):
        self.driver.get('https://www.netflix.com')

    def test_visit_wikipedia(self):
        self.driver.get('https://www.wikipedia.org')

    @classmethod
    def tearDownClass(cls) -> None:
        #cerramos las ventanas una vez finalizadas las pruebas
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reports', report_name = 'hello-world-report'))
    '''este unittest nos dice que:
    1) las pruebas se van a guardar en una carpeta que se va a crear y se va a llamar report
    2) el nombre de la prueba se va a llamar hello-world-report y lo va a guardar como un archivo html'''