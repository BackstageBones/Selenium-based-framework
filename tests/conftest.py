import pytest
from pages.selenium_factory import SeleniumFactory
from pages.selenium_actions import SeleniumActions


@pytest.fixture(scope="class")
def chrome_driver_init(request):
    chrome_driver = SeleniumFactory().create_chrome_driver()
    request.cls.driver = chrome_driver
    yield
    chrome_driver.close()
    chrome_driver.quit()


@pytest.fixture(scope="class")
def firefox_driver_init(request):
    ff_driver = SeleniumFactory().create_firefox_driver()
    request.cls.driver = ff_driver
    yield
    ff_driver.close()
    ff_driver.quit()


@pytest.fixture(params=["chrome", "firefox"], scope="class")
def driver_init(request):
    if request.param == "chrome":
        web_driver = SeleniumFactory().create_chrome_driver()
    elif request.param == "firefox":
        web_driver = SeleniumFactory().create_firefox_driver()
    else:
        raise AttributeError("Driver not supported")
    request.cls.driver = web_driver
    yield
    web_driver.close()
    web_driver.quit()
