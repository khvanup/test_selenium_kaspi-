from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class Base():

    def __init__(self, driver):
        self.driver = driver

    def getter(self, get_locator):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, get_locator)))

    def click_item(self, locator):
        self.getter(locator).click()

    def pause(self, sec=4):
        time.sleep(sec)

    def get_url(self):
        url = self.driver.current_url
        return url
    def assert_value(self, value, result):
        assert value == result