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
        driver.get("https://mercadolibre.com/")
        driver.maximize_window()
        driver.implicitly_wait(15)
    
    def test_search_ps4(self):
        driver = self.driver
        country = driver.find_element(By.ID, 'CO')
        country.click()

        search_field = driver.find_element(By.NAME, 'as_word')
        search_field.clear()
        search_field.send_keys('playstation 4')
        search_field.submit()
        sleep(3)

        location = driver.find_element(By.PARTIAL_LINK_TEXT, 'Bogotá D.C.')
        driver.execute_script("arguments[0].click();", location)
        sleep(3)

        condition= driver.find_element(By.PARTIAL_LINK_TEXT, 'Nuevo')
        driver.execute_script("arguments[0].click();", condition)
        sleep(3)

        order_menu = driver.find_element(By.CLASS_NAME, 'andes-dropdown__display-values')
        order_menu.click()

        higher_price = driver.find_element(By.CSS_SELECTOR, '#andes-dropdown-más-relevantes-list-option-price_desc > div > div > span')
        driver.execute_script("arguments[0].click();", higher_price)
        sleep(3)

        articles = []
        prices = []

        for i in range (5):
            article_name =driver.find_element(By.XPATH, f'//*[@id="root-app"]/div/div[2]/section/ol/li[{i+1}]/div/div/div[2]/div[1]/a/h2').text
            articles.append(article_name)

            article_price = driver.find_element(By.XPATH, f'//*[@id="root-app"]/div/div[2]/section/ol/li[{i+1}]/div/div/div[2]/div[2]/div[1]/div[1]/div/div/div/span[1]/span[2]/span[2]').text
            prices.append(article_price)

        dictionary = {articles : prices for (articles, prices) in zip (articles, prices)}
        print(dictionary)

    def tearDown(self) :
        self.driver.close()

if __name__ == '__main__':
    unittest.main(verbosity=2)
