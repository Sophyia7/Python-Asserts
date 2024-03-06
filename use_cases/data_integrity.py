from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=common/home")


# `assert "Your Store" in driver.title, "Website title is not as expected"`: This line is where the data integrity check happens. The `driver.title` property returns the title of the current page, and the `assert` statement checks if the string "Your Store" is in that title.
assert "Your Store" in driver.title, "Website title is not as expected"