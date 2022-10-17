import pytest
from Pages.iframe import IframePage
from Config.urls import urls
@pytest.mark.usefixtures("get_driver")
class TestFrame():

    def test_iframe_page(self):
        self.iframePage = IframePage("Frame page")
        self.driver.get(urls.iframe)
        self.iframePage.iframe1_switch(self.driver)
        text_frame1 = self.iframePage.frame_text(self.driver)
        self.iframePage.def_content(self.driver)
        self.iframePage.iframe2_switch(self.driver)
        text_frame2 = self.iframePage.frame_text(self.driver)
        assert text_frame1 == text_frame2