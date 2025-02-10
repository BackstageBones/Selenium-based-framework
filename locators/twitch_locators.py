from dataclasses import dataclass

from selenium.webdriver.common.by import By


@dataclass
class TwitchLocators:
    cookies_popup_close: By = (By.XPATH, "//button[@data-a-target='consent-banner-accept']")
    root_navbar: By = (By.XPATH, "//div[@class='Layout-sc-1xcs6mc-0 dShAUu']")
    search_loop: By = (By.XPATH, "//a[@href='/directory']")
    search_input: By = (By.XPATH, "//input[@type='search']")
    streams_preview_images: By = (By.XPATH, "//div[@class='Layout-sc-1xcs6mc-0 eFvOkl']//img")
    stream_preview: By = (By.XPATH, "//div[@data-a-target='player-controls']")
