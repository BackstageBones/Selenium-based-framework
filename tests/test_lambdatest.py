import pytest
from pages.lambda_test_page import LambdaTestPage


@pytest.mark.usefixtures("driver_init")
class BasicChromeTest:
    pass


class TestUrlChrome(BasicChromeTest):
    def test_open_url(self):
        self.driver.get('https://lambdatest.github.io/sample-todo-app/')
        self.driver.maximize_window()

    @pytest.mark.parametrize("test_browser, test_url",
                             [
                                 pytest.param("chrome", "https://www.lambdatest.com/", marks=pytest.mark.basic),
                                 pytest.param("firefox", "https://www.lambdatest.com/blog/", marks=pytest.mark.basic),
                                 pytest.param("safari", "https://www.lambdatest.com/blog/", marks=pytest.mark.skip),
                             ]
                             )
    def test_open_url_v2(self, test_browser, test_url):
        if test_browser == "chrome":
            expected_title = "Next-Generation Mobile Apps and Cross Browser Testing Cloud | LambdaTest"

        if test_browser == "firefox":
            expected_title = "LambdaTest | A Cross Browser Testing Blog"
        self.driver.get(test_url)
        assert expected_title == self.driver.title

    @pytest.mark.parametrize("test_browser",
                             [
                                 pytest.param("chrome"),
                                 pytest.param("firefox")
                             ])
    def test_mark_checkboxes(self, test_browser):
        lambda_page = LambdaTestPage(self.driver)
        if test_browser == "chrome":
            lambda_page._open_webpage("https://lambdatest.github.io/sample-todo-app/")
            lambda_page.mark_all_checkboxes()
        elif test_browser == "firefox":
            lambda_page._open_webpage("https://www.lambdatest.com/blog/")
            expected_title = "LambdaTest Blogs"
            assert expected_title == lambda_page._get_page_title
