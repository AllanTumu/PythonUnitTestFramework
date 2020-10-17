# Imports
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import HtmlTestRunner


class orangeHRMTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome("/home/mea/PycharmProjects/PythonUnitTestFramework/drivers/chromedriver")
        cls.driver.maximize_window()

    def test_homePageTitle(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        title = self.driver.title
        self.assertEqual("OrangeHRM", title, "Web title not matching")

    def test_login(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element_by_xpath("//input[@id='txtUsername']").send_keys("Admin")
        self.driver.find_element_by_xpath("//input[@id='txtPassword']").send_keys("admin123")
        self.driver.find_element_by_xpath("//*[@id='btnLogin']").click()
        title = self.driver.title
        self.assertEqual("OrangeHRM", title, "Web title not matching")

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
        print("Test Complete")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="..\\reports"))
