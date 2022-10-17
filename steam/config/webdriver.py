from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
#singleton class for web driver
class WebDriver:
    class __WebDriver:
        def __init__(self):
            options = webdriver.ChromeOptions()
            options.add_argument("--incognito")
            options.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
            self.driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

    driver = None

    def __init__(self):
        if not self.driver:
            WebDriver.driver = WebDriver.__WebDriver().driver