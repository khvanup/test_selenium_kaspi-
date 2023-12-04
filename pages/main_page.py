import time

import conftest
from base.base import Base
from pages.phones_page import phones_class
from pages.computers_page import computers_class
from pages.tv_audio_page import tv_audio_class
from conftest import set_up
from conftest import set_group

class main_class(Base):
    url = 'https://kaspi.kz/'
    locator_category_mobile_phones = "//*[@id='main']/div/div[2]/div/div[2]/div[1]/div/div/div[2]/div/a[1]/span[1]"
    locator_category_computers = "//*[@id='main']/div/div[2]/div/div[2]/div[1]/div/div/div[2]/div/a[2]/span[1]"
    locator_category_tv_audio = "//*[@id='main']/div/div[2]/div/div[2]/div[1]/div/div/div[2]/div/a[10]/span[1]"
    locator_next = "//*[@id='main']/div/div[2]/div/div[2]/div[2]/svg[2]/circle"
    locator_main = "//*[@id='searchComponent']/form/a"

    def __init__(self, driver):
        super().__init__(driver)
        self.conftest = None
        self.driver = driver

    def buy_phone_main_page(self):
        self.driver.get(self.url)

        print("\nCurrent url: " + self.driver.current_url)

        save_title_category_main_page = self.getter(self.locator_category_mobile_phones).text.replace('\n',' ')
        save_title_category_main_page = save_title_category_main_page.replace(', ',' ')
        print(f"Сохранение названия '{save_title_category_main_page}' на главной странице, в переменную - ОК")

        self.click_item(self.locator_category_mobile_phones)  # выбираем категорию "Телефоны и гаджеты"
        print(f"Переход к категории '{save_title_category_main_page}' - ОК")

        phones_class(self.driver).activities_phones_page(save_title_category_main_page)
        self.click_item(self.locator_main)
        self.driver.close()

    def buy_computer_main_page(self):
        self.driver.get(self.url)

        print("\nCurrent url: " + self.driver.current_url)

        save_title_category_main_page = self.getter(self.locator_category_computers).text.replace('\n',' ')
        print(f"Сохранение названия '{save_title_category_main_page}' на главной странице, в переменную - ОК")

        self.click_item(self.locator_category_computers)  # выбираем категорию "Компьютеры"
        print(f"Переход к категории '{save_title_category_main_page}' - ОК")

        computers_class(self.driver).activities_computer_class(save_title_category_main_page)
        self.click_item(self.locator_main)
        self.driver.close()

    def buy_tv_audio_page(self):
        self.driver.get(self.url)

        print("\nCurrent url: " + self.driver.current_url)

        save_title_category_main_page = self.getter(self.locator_category_tv_audio).text.replace('\n',' ')
        print(f"Сохранение названия '{save_title_category_main_page}' на главной странице, в переменную - ОК")

        self.click_item(self.locator_category_tv_audio)  # выбираем категорию ТВ и Аудио
        print(f"Переход к категории '{save_title_category_main_page}' - ОК")

        tv_audio_class(self.driver).activities_tv_audio_page(save_title_category_main_page)
        self.click_item(self.locator_main)
        self.driver.close()
