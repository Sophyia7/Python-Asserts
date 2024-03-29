import sys
sys.path.append(sys.path[0] + "/..")
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from base import SampleTest
import unittest



class InputValidation(SampleTest):
    def test_email_password(self):

        driver = self.driver
        driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=account/login")

        try:
            # Find the email and password fields
            email = driver.find_element(By.ID, "input-email")
            password = driver.find_element(By.ID, "input-password")

            # Input some test data
            email.send_keys("testexample.com")
            password.send_keys("testpassword")

            # Validate the input
            assert "@" in email.get_attribute("value"), "Invalid email address"
            assert len(password.get_attribute("value")) > 0, "Password field is empty"

            # Find and click the login button
            login_button = driver.find_element(By.CSS_SELECTOR, "input.btn.btn-primary")
            login_button.click()

        except NoSuchElementException as e:
            print(f"An error occurred: {e}")

        finally:
            driver.quit()

if __name__ == "__main__":
    unittest.main()