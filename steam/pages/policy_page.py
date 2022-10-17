from selenium.webdriver.common.by import By
from seleniumpagefactory.Pagefactory import PageFactory

class PolicyPage(PageFactory):
    
    def __init__(self, driver):
        self.driver = driver
    
    locators = {
        "CSS_POLICY_LINK" :  ("CSS", "a[target='_blank'][rel='noreferrer'][href='https://store.steampowered.com/privacy_agreement/?snr=1_44_44_']"),
        "ID_ACCEPT_COOKIES_BUTTON" :  ("ID", "acceptAllButton"),
        "ID_SWITCH_LANGUAGES" :  ("ID", "languages"),
    }
    
    def policyPrecondition(self, url):
        self.driver.get(url)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        if self.ID_ACCEPT_COOKIES_BUTTON.visibility_of_element_located():
            self.ID_ACCEPT_COOKIES_BUTTON.click_button()
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.CSS_POLICY_LINK.click_button()
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def getTitle(self):
        return self.driver.title

    def languagesSwitchVisible(self):
        return self.ID_SWITCH_LANGUAGES.visibility_of_element_located()

    def getSignDate(self):
        element = self.driver.find_element(By.ID, "newsColumn") # div that contains <i> Date </i>
        return element.find_element(By.XPATH, "//*[contains(text(), 'Revision Date:')]")

