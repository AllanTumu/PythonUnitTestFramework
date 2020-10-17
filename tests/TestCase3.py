import unittest
from selenium import webdriver


def setUpModule():
    print("Before Module")


def afterModule():
    print("After Module")


class AppTesting(unittest.TestCase):

    @classmethod
    def setUp(self):
        print("Before")

    @classmethod
    def tearDown(self) -> None:
        print("After")

    @classmethod
    def setUpClass(cls) -> None:
        print("Launching Application")

    @classmethod
    def tearDownClass(cls) -> None:
        print("Closing application")

    def testSearch(self):
        print("This is a search Test")

    def testPrepaidCharge(self):
        print("This is a Prepaid charge Test")


if __name__ == "__main":
    unittest.main()
