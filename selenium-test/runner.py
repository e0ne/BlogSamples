import unittest

from selenium import webdriver

from ffsample import BaseTestCase, YahooTest, YandexTest

def suite():
    firefox = webdriver.Firefox() # Get local session of firefox
    suite = unittest.TestSuite()
    suite.addTest(BaseTestCase.parametrize(YahooTest, browser=firefox))
    suite.addTest(BaseTestCase.parametrize(YandexTest, browser=firefox))
    unittest.TextTestRunner(verbosity=2).run(suite)
    firefox.close()

if __name__ == "__main__":
    #unittest.main()
    suite()