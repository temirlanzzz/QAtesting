import pytest
from Pages.iframe import IframePage
from Config.urls import urls
from Config.config import jsonFile


@pytest.mark.usefixtures("get_driver")
class TestNestedIframes():

    def test_iframe_page(self):
        self.iframePage = IframePage("Nested Frame Page")
        self.driver.get(urls.nested_frames)
        self.iframePage.parent_frame_switch(self.driver)
        self.driver.switch_to.frame(0)
        text_frame_child = self.iframePage.nested_frame_text(self.driver)
        text_json = jsonFile.read_json("../Data/iframe.json")
        assert text_frame_child == text_json