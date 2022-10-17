import pytest
from config.webdriver import WebDriver
@pytest.fixture(scope='class')
def chrome_init_driver(request):
    chrome_driver = WebDriver().driver
    request.cls.driver = chrome_driver
    yield
    chrome_driver.quit()

