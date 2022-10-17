from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Config.config import config
class BaseElement:

    def __init__(self, driver, locator, name):
        self.uniqueLocator = locator
        self.name = name
        self.waits = WebDriverWait(driver, timeout=config.timeout)

    def do_click(self):
        self.waits.until(EC.visibility_of_element_located(self.uniqueLocator))
        self.waits.until(EC.element_to_be_clickable(self.uniqueLocator)).click()

    def send_text(self, text):
        self.waits.until(EC.visibility_of_element_located(self.uniqueLocator)).send_keys(text)

    def get_element(self, driver):
        return driver.find_element(*self.uniqueLocator)

    def switch_to_iframe(self):
        self.waits.until(EC.frame_to_be_available_and_switch_to_it(self.uniqueLocator))

    def get_text(self):
        return self.waits.until(EC.visibility_of_element_located(self.uniqueLocator)).text