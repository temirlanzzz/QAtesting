from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from Config.urls import urls
class BrowserFactory:

    @staticmethod
    def get_driver(browser):
        if browser == "edge":
            driver = webdriver.Edge(EdgeChromiumDriverManager().install())
        elif browser == "firefox":
            driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        else:
            driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        return driver
