from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import ChromiumOptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver as ChromeDriver
from selenium.webdriver.firefox.webdriver import WebDriver as FireFoxDriver
from webdriver_manager.firefox import GeckoDriverManager


class SeleniumFactory:

    def set_chrome_options(self):
        options = ChromiumOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--headless=new")
        options.add_argument("--disable-extensions")
        options.add_argument("--no-sandbox")
        options.add_argument("disable-infobars")
        options.add_argument("enableNetwork")
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-dev-shm-usage")
        options.add_experimental_option("prefs", self.set_browser_preferences())
        options.set_capability("cloud:options", self.set_desired_capabilities())
        return options

    def set_browser_preferences(self):
        prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "excludeSwitches": ["enable-automation"],
            "safebrowsing.profile_enabled": False
        }
        return prefs

    def set_desired_capabilities(self):
        caps = DesiredCapabilities.CHROME.copy()
        caps["acceptSslCerts"] = True

    def create_chrome_driver(self):
        return ChromeDriver(options=self.set_chrome_options(), service=Service())

    def create_firefox_driver(self):
        return FireFoxDriver(service=Service(GeckoDriverManager().install()))
