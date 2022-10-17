import pytest
from Browser.browser_factory import BrowserFactory

@pytest.fixture(scope='class')
def get_driver(request):
    driver = BrowserFactory.get_driver('chrome')
    request.cls.driver = driver
    yield
    driver.quit()
