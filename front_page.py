import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class FrontPage(unittest.TestCase):

    @classmethod
    def setUp(self):
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(options=options)
        self.base_url = "https://skleptest.pl/"
        self.header_all_black_tops_xpath =  '//*[@id="tyche_products-1"]/h3/span'
        self.expected_text = 'ALL BLACK TOPS'


    @classmethod
    def tearDown(self):
        self.driver.quit()

    def test_header_all_black_tops(self):
        driver = self.driver
        driver.get(self.base_url)
        header_all_black_tops_xpath_elememnt= driver.find_element(By.XPATH, self.header_all_black_tops_xpath )
        header_all_black_tops_text = header_all_black_tops_xpath_elememnt.text
        self.assertEqual(self.expected_text, header_all_black_tops_text, f'Something went wrong!' )




