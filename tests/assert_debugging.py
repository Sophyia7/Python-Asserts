import sys
sys.path.append(sys.path[0] + "/..")
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
            self.driver.execute_script("lambda-status=failed")

if __name__ == "__main__":
    unittest.main()   