from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from base import SampleTest
import unittest

class DebugTest(SampleTest):

    def test_element_exists(self):
        self.driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=common/home")

        try:
            element = self.driver.find_element(By.ID, "mz-component")
            self.assertIn("expected text", element.text)
        except NoSuchElementException:
            assert False, "Element not found"

if __name__ == "__main__":
    unittest.main()
        
    
    
    
    
    
    
    
    
    
    
    










