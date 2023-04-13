import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class find_elements(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
        driver = self.driver
        driver.get("http://demo-store.seleniumacademy.com")
        driver.maximize_window()
        driver.implicitly_wait(30)

    def test_search_tee(self):
        driver = self.driver
        search_field = driver.find_element(By.NAME,'q')
        search_field.clear()
        search_field.send_keys('tee')
        search_field.submit()

    def test_sat_shaker(self):
        driver = self.driver
        search_field = driver.find_element(By.NAME,'q')
        search_field.send_keys('salt shaker')
        search_field.submit()

        products = driver.find_elements(By.XPATH, '//*[@id="top"]/body/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/ul/li/div/h2/a')
        self.assertEqual(1, len(products))

    def tearDown(self) :
        self.driver.quit()

