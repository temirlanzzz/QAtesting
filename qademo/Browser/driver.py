import pytest
from Patterns.singleton import Singleton
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from .browser_factory import BrowserFactory
class GetDriver(metaclass=Singleton):

    def __init__(self):
        self.driver = BrowserFactory.get_driver("chrome")

    def getWait(self):
        return WebDriverWait(self.driver, timeout=10)