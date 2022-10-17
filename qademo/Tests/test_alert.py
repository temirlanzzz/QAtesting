import pytest
from Pages.alert import AlertPage
from Config.urls import urls
@pytest.mark.usefixtures("get_driver")
class TestAlert():

    def test_alert_button(self):
        self.alertPage = AlertPage('Alert Page')
        self.driver.get(urls.BASE_URL)
        self.alertPage.go_to_alert_page(self.driver)
        self.alertPage.click_alert(self.driver)
        self.alertPage.accept_alert(self.driver)

        self.alertPage.click_to_confirm_alert(self.driver)
        self.alertPage.accept_alert(self.driver)

        self.alertPage.click_to_prompt_alert(self.driver)
        self.alertPage.switch_prompt(self.driver)




