from selenium.webdriver.support import expected_conditions as EC

class BaseForm:
    def __init__(self, name):
        self.formName = name

    def isFromOpen(self, locator):
        self.waits.until(EC.visibility_of_element_located(locator))

