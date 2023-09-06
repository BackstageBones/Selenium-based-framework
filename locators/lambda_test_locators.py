from dataclasses import dataclass
from selenium.webdriver.common.by import By

class LambdaTestLocators:
    checkboxes: By = (By.XPATH, "//input[@type='checkbox']")