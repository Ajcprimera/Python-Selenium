import csv,unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By 
from ddt import ddt, data, unpack

def get_data(file_name):
    row= []
    data = open(file_name, 'r')
    reader = csv.reader(data)
    next(reader, None)

    for i in reader:
        row.append(i)
    return row

@ddt
class datadriventesting(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
        driver = self.driver
        driver.get("http://demo-store.seleniumacademy.com")
        driver.maximize_window()
        driver.implicitly_wait(15)

    @data(*get_data('testdata.csv'))
    @unpack

    def test_search_ddt(self, search_value, expected_count):
        driver = self.driver

        search_field = driver.find_element(By.NAME, 'q')
        search_field.clear()
        search_field.send_keys(search_value)
        search_field.submit()

        products = driver.find_elements(By.XPATH, '//h2[@class="product-name"]/a')
        expected_count = int(expected_count)

        if expected_count > 0:
            self.assertEqual(expected_count, len(products))
        else:
            message = driver.find_element(By.CLASS_NAME, 'not-msg')
            self.assertEqual('Your search returns no results.', message)

        print(f'Found {len(products)} products')

        '''print(f'Found {len(products)} products')

        for i in products:
            print(i.text)

        self.assertEqual(expected_count, len(products))'''

    def tearDown(self) :
        self.driver.close()

if __name__ == '__main__':
    unittest.main(verbosity=2)