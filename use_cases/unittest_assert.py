import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class TestHomePage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=common/home")

    def test_title(self):
        assert "Your Store" in self.driver.title, "Website title is not as expected"
    
    def test_element_presence(self):
        try:
            element = self.driver.find_element(By.ID, "cart-total-drawer")
            self.assertTrue(element is not None, "Element not found")
        except NoSuchElementException:
            assert False, "Element not found"

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()