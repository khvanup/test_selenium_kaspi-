import time

from pages.main_page import main_class
from conftest import set_up
from conftest import set_group
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.common.exceptions import TimeoutException




def initialization():
    options = webdriver.ChromeOptions()

    options.page_load_strategy = 'eager'
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_argument('--incognito')
    options.add_argument('--headless')
    options.add_argument("--window-size=1920,1080")
    options.add_experimental_option('detach', True)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    path_chrome = Service(executable_path=r'C:\\Users\\Admin\\PycharmProjects\\resource\\chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=path_chrome)
    driver.set_page_load_timeout(1500)



    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    return driver

@pytest.mark.run(order=2)
def test_buy_phone(set_up):
    main_class(initialization()).buy_phone_main_page()

@pytest.mark.run(order=3)
def test_buy_computer(set_up):
    main_class(initialization()).buy_computer_main_page()

@pytest.mark.run(order=1)
def test_buy_tv_audio(set_group, set_up):
    main_class(initialization()).buy_tv_audio_page()

