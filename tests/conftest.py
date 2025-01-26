import pytest

from pages.selenium_factory import SeleniumFactory


@pytest.fixture(params=["browser", "mobile"], scope="class")
def driver_init(request):
    browser = request.param.get("browser", "chrome")
    mobile = request.param.get("mobile", "False")
    driver = SeleniumFactory.create_driver(browser, mobile)
    request.cls.driver = driver
    yield driver
    driver.close()
    driver.quit()
