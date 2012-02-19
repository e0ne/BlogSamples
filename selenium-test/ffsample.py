# -*- coding: UTF-8 -*-

import time
import unittest

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

class BaseTestCase(unittest.TestCase):
    """ TestCase classes that want to be parametrized should
        inherit from this class.
    """
    def __init__(self, methodName='runTest', browser=None):
        super(BaseTestCase, self).__init__(methodName)
        self.browser = browser

    @staticmethod
    def parametrize(testcase_klass, browser=None):
        """ Create a suite containing all tests taken from the given
            subclass, passing them the parameter 'param'.
        """
        testloader = unittest.TestLoader()
        testnames = testloader.getTestCaseNames(testcase_klass)
        suite = unittest.TestSuite()
        for name in testnames:
            suite.addTest(testcase_klass(name, browser=browser))
        return suite


class YahooTest(BaseTestCase):
    def test_search(self):
        self.browser.get("http://www.yahoo.com") # Load page
        assert "Yahoo!" in self.browser.title
        elem = self.browser.find_element_by_name("p") # Find the query box
        elem.send_keys("seleniumhq" + Keys.RETURN)
        time.sleep(0.2) # Let the page load, will be added to the API
        try:
            self.browser.find_element_by_xpath("//a[contains(@href,'http://seleniumhq.org')]")
        except NoSuchElementException:
            assert 0, "can't find seleniumhq"


class YandexTest(BaseTestCase):
    def test_search(self):
        try:
            self.browser.get("http://www.yandex.ru") # Load page
            assert u"Яндекс" in self.browser.title
            elem = self.browser.find_element_by_name("p") # Find the query box
            elem.send_keys("e0ne" + Keys.RETURN)
            time.sleep(0.2) # Let the page load, will be added to the API
            self.browser.find_element_by_xpath("//a[contains(@href,'http://seleniumhq.org')]")
        except NoSuchElementException:
            assert 0, "can't find seleniumhq"
