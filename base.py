import os
import unittest
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.common.by import By

username = os.environ.get("LT_USERNAME")
access_key = os.environ.get("LT_ACCESS_KEY")


class SampleTest(unittest.TestCase):

    # setUp runs before each test case
    def setUp(self):
        lt_options = {
            "user": username,
            "accessKey": access_key,
            "build": "Python Asserts Tests with Selenium",
            "name": "Python Asserts Tests with Selenium",
            "platformName": "Windows 11",
            "w3c": True,
            "browserName": "Chrome",
            "browserVersion": "latest",
            "selenium_version": "4.0.0"
        }
        
        browser_options = ChromeOptions()
        browser_options.set_capability('LT:Options', lt_options)

        self.driver = webdriver.Remote(
            command_executor="http://hub.lambdatest.com:80/wd/hub",
            options=browser_options)


if __name__ == "__main__":
    unittest.main()