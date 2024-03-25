import sys
sys.path.append(sys.path[0] + "/..")
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from base import SampleTest

class TestHomePage(SampleTest):

    def test_title(self):
        # try:
        driver = self.driver

        # Url
        driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=common/home")
        assert "Your Store" in self.driver.title, "Website title is not as expected"
    
    def test_element_presence(self):

      driver = self.driver

      driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=common/home")

      try:
          element = self.driver.find_element(By.ID, "cart-total-drawer")
          self.assertTrue(element is not None, "Element not found")
      except NoSuchElementException:
          assert False, "Element not found"

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()