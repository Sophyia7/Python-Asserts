from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()
driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=common/home")

try:
    element = driver.find_element(By.ID, "mz-component")
except NoSuchElementException:
    assert False, "Element not found"