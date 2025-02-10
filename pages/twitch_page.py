import random

from locators.twitch_locators import TwitchLocators
from pages.basepage import BasePage


class TwitchPage(BasePage):
    url = 'https://m.twitch.tv/'

    def __init__(self, driver):
        super().__init__(driver)

    def close_cookies_banner(self):
        if self.actions.is_element_displayed(TwitchLocators.cookies_popup_close, timeout=5):
            self.actions.click_element(TwitchLocators.cookies_popup_close)

    def is_page_displayed(self) -> bool:
        self.close_cookies_banner()
        return self.actions.is_element_displayed(TwitchLocators.root_navbar)

    def click_loop_icon(self) -> None:
        self.actions.wait_for_element_visible(TwitchLocators.search_loop)
        self.actions.click_element(TwitchLocators.search_loop)

    def enter_searched_phrase(self, text) -> None:
        self.actions.send_text(TwitchLocators.search_input, text)

    def wait_for_twiches(self):
        return self.actions.are_any_elements_visible(TwitchLocators.streams_preview_images)

    def open_random_twitch(self):
        self.wait_for_twiches()
        self.actions.scroll_n_times(2)
        previews = self.wait_for_twiches()
        selected_twitch = random.choice(previews)
        self.actions.scroll_to_element_center(selected_twitch)
        self.actions.click_element(selected_twitch)

    def is_stream_visible(self) -> bool:
        return self.actions.is_element_displayed(TwitchLocators.stream_preview)
