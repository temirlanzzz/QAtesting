from Base.form import BaseForm
from selenium.webdriver.common.by import By
from Base.element import BaseElement

class IframePage(BaseForm):
    IFRAME1 = (By.ID, 'frame1')
    IFRAME2 = (By.ID, 'frame2')
    FRAME_TEXT = (By.ID, 'sampleHeading')
    PARENT_FRAME = (By.ID, 'frame1')
    TEXT_NESTED_FRAME = (By.TAG_NAME, "body")

    def iframe1_switch(self, driver):
        return driver.switch_to.frame(BaseElement(driver, self.IFRAME1, "Frame 1").get_element(driver))

    def iframe2_switch(self, driver):
        return driver.switch_to.frame(BaseElement(driver, self.IFRAME2, "Frame 2").get_element(driver))

    def frame_text(self, driver):
        element = BaseElement(driver, self.FRAME_TEXT, "Frame text").get_element(driver)
        return element.text

    def def_content(self, driver):
        return driver.switch_to.default_content()

    def parent_frame_switch(self, driver):
        return driver.switch_to.frame(BaseElement(driver, self.PARENT_FRAME, "Parent Frame").get_element(driver))

    def nested_frame_text(self, driver):
        element = BaseElement(driver, self.TEXT_NESTED_FRAME, "Nested frame").get_element(driver)
        return element.text