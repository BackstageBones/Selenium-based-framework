from datetime import datetime
import allure
import pytest
from assertpy import assert_that

from pages.twitch_page import TwitchPage


@pytest.mark.parametrize('driver_init', [{'browser': 'chrome', 'mobile': True}], indirect=True)
class TestTwitch:

    @allure.title("Test Twitch stream preview")
    @allure.description(
        "This test attempts to open starcraft II stream preview.\n Fails if any error happens.")
    @allure.tag("NewUI", "Essentials", "Authentication")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label("owner", "Adrian Miendlarzewski")
    @allure.link("https://github.com/BackstageBones/Selenium-based-framework/tree/twitch-preview", name="repository")
    @allure.issue("some test issue")
    @allure.testcase("some test case")
    @pytest.mark.usefixtures('driver_init')
    def test_stream_preview(self):
        tw_page = TwitchPage(self.driver)
        tw_page._open_webpage(TwitchPage.url)
        assert_that(tw_page.is_page_displayed(),
                    "Twitch mobile website not visible").is_true()
        tw_page.click_loop_icon()
        tw_page.enter_searched_phrase("StarCraft II")
        assert_that(tw_page.is_page_displayed()).is_true()
        assert_that(tw_page.wait_for_twiches(),
                    "No streams available").is_not_none().is_iterable()
        tw_page.open_random_twitch()
        assert_that(tw_page.is_stream_visible(),
                    "Stream preview not visible").is_true()
        png_name = 'stream_evidence_{}.png'.format(datetime.now().strftime('%Y%m%d_%H%M%S'))
        self.driver.save_screenshot(png_name)
