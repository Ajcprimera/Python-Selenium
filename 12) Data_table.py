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
        driver.find_element(By.LINK_TEXT,'Sortable Data Tables').click()
        driver.implicitly_wait(15)

    def test_sort_tables(self):
        driver = self.driver
        table_data = [[] for i in range(5)]
        print(table_data)

        for i in range(5):
            header = driver.find_element(By.XPATH, f'//*[@id="table1"]/thead/tr/th[{i+1}]')
            table_data[i].append(header.text)
            for j in range(4):
                row_data = driver.find_element(By.XPATH, f'//*[@id="table1"]/tbody/tr[{j+1}]/td[{i+1}]')
                table_data[i].append(row_data.text)
        print(table_data)


    def tearDown(self) :
        self.driver.close()

if __name__ == '__main__':
    unittest.main(verbosity=2)
    