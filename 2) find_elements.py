import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By 
#Esta libreria nos permite conseguir los elementos de una pagina web

class find_elements(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
        driver = self.driver
        driver.get("http://demo-store.seleniumacademy.com")
        driver.maximize_window()
        driver.implicitly_wait(15)

    def test_search_text_field(self):
        #Conseguir el elemento mediante el ID de la pagina web
        search_field = self.driver.find_element(By.ID,"search")

    def test_search_text_field_by_name(self):
        #Conseguir el elemento mediante el NOMBRE de la pagina web
        search_field = self.driver.find_element(By.NAME,"q")

    def test_search_text_field_class_name(self):
        #Conseguir el elemento mediante el NOMBRE DE LA CLASE de la pagina web
        search_field = self.driver.find_element(By.CLASS_NAME,"input-text")

    def test_search_button_enabled(self):
        button = self.driver.find_element(By.CLASS_NAME,"button")

    def test_count_promo_banner_images(self):
        banner_list = self.driver.find_element(By.CLASS_NAME, "promos")
        #Conseguir el elemento mediante el TAG de la pagina web
        banners = banner_list.find_elements(By.TAG_NAME, "img")
        #El assertEqual nos permite saber si una condicion se cumple o no
        self.assertEqual(3, len(banners))

    def test_vip_promo(self):
        #Conseguir el elemento mediante la ruta XPATTH de la pagina web
        vip_promo = self.driver.find_element(By.XPATH, '//*[@id="top"]/body/div/div[2]/div[2]/div/div/div[2]/div[1]/ul/li[4]/a/img')

    def test_shopping_cart(self):
        #Conseguir el elemento mediante el CSS de la pagina web
        shopping_cart = self.driver.find_element(By.CSS_SELECTOR,"div.header-minicart span.icon")

    def tearDown(self) :
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)