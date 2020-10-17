import unittest
from selenium import webdriver


# Search Engine test
class SearchEngineTest(unittest.TestCase):
    def test_google(self):
        self.driver = webdriver.Chrome(
            executable_path="/home/mea/PycharmProjects/PythonUnitTestFramework/drivers/chromedriver")
        self.driver.get("https://www.google.com/")
        print("Title of the page is", self.driver.title)
        self.driver.close()

    def test_firefox(self):
        self.driver = webdriver.Firefox(
            executable_path="/home/mea/PycharmProjects/PythonUnitTestFramework/drivers/geckodriver")
        self.driver.get("https://www.google.com/")
        print("Title of the page is", self.driver.title)
        self.driver.close()


if __name__ == "__main__":
    unittest.main()