from Base.form import BaseForm
from selenium.webdriver.common.by import By
from Base.element import BaseElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
class AlertPage(BaseForm):

    ALERT_BUTTON = (By.XPATH, '//*[@id="alertButton"]')
    #ALERTS_BUTTON = (By.ID, "item-1")
    ALERTS_BUTTON = (By.XPATH, "//span[contains(text(), 'Alerts')]")
    ALERT_PAGE_BUTTON = (By.XPATH, '//div[@class="card mt-4 top-card"][3]')
    ELEMENT = (By.XPATH, "//h5[contains(text(), 'Alerts, Frame & Windows')]")
    BUTTON_CONFIRM = (By.ID, 'confirmButton')
    BUTTON_PROMPT = (By.ID, 'promtButton')
    #ALERT_PAGE_BUTTON = (By.XPATH, "//h5[contains(text(), 'Alerts, Frame & Windows')]")

    def go_to_alert_page(self, driver):
        BaseElement(driver, self.ALERT_PAGE_BUTTON, "Move from main page to alerts page").do_click()
        web_element = BaseElement(driver, self.ALERTS_BUTTON, "Select alerts item").get_element(driver)

    def click_alert_page(self, driver):
        web_element = BaseElement(self.ELEMENT, "Alert").get_element(driver)
        return driver.execute_script("arguments[0].click()", web_element)

    def click_alert(self, driver):

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        BaseElement(driver, self.ALERTS_BUTTON, "Alert Form").do_click()
        BaseElement(driver, self.ALERT_BUTTON, "Alert Button").do_click()

    def click_to_confirm_alert(self, driver):
        element = BaseElement(driver, self.BUTTON_CONFIRM, "Confirm Alert").get_element(driver)
        return driver.execute_script("arguments[0].click()", element)

    def click_to_prompt_alert(self, driver):
        element = BaseElement(driver, self.BUTTON_PROMPT, "Prompt Alert").get_element(driver)
        return driver.execute_script("arguments[0].click()", element)

    def switch_prompt(self, driver):
        prompt_alert = driver.switch_to.alert
        prompt_alert.send_keys("Test user")
        prompt_alert.accept()

    def accept_alert(self, driver):
        WebDriverWait(driver,20).until(EC.alert_is_present())
        driver.switch_to.alert.accept()