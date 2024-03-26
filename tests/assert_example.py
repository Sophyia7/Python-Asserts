import sys
sys.path.append(sys.path[0] + "/..")
from base import SampleTest
import unittest

class AssertExamples(SampleTest):
  def test_page_title(self):
      driver = self.driver
      driver.get("https://lambdatest.github.io/sample-todo-app/")

          # Use the `assert` statement to verify if the page title is correct
      if driver.title == "To-do app":
          self.assertFalse(False, "Page title is correct")
      else:
          self.assertFalse(True, "Page title is incorrect")

      driver.close()


if __name__ == "__main__":
    unittest.main()