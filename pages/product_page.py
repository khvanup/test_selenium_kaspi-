import time
from base.base import Base


class product_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    locator_open_menu_colour = "//*[@id='ItemView']/div[2]/div/div[2]/div/div[2]/div[1]/div"
    locator_select_colour = "//*[@id='ItemView']/div[2]/div/div[2]/div/div[2]/div[1]/div[2]/div[1]/label"
    locator_open_view = "//*[@id='ItemView']/div[2]/div/div[1]/div/div[1]/div/div[1]/ul/li[1]/div/img"
    locator_next_view = "//*[@id='LightboxComponent']/div[2]/div/div[2]/button"
    locator_close_view = "//*[@class='lightbox__button lightbox__button--close']"
    locator_credit_6 = "//*[@id='offers']/div/div/div/div/div[2]/div/span[2]"
    locator_credit_12 = "//*[@id='offers']/div/div/div/div/div[2]/div/span[3]"
    locator_choose_seller = "//*[@id='offers']/div/div/div[1]/table/tbody/tr[1]/td[7]/div/div"
    locator_close = "//*[@id='dialogService']/div/div[1]/div[2]"
    locator_title_sellers = "//*[@id='ItemView']/div[3]/div/ul/li[1]"
    locator_main = "//*[@id='searchComponent']/form/a"



    def activities_product_page(self):
        print("\nCurrent url: " + self.driver.current_url)

        save_title_sellers = self.getter(self.locator_title_sellers).text.replace('\n',' ')
        print(f"Сохранение '{save_title_sellers}' на странице продукта, в переменную - ОК")


        self.assert_value("Продавцы", save_title_sellers)
        print(f"Соответствие '{save_title_sellers}' - ОК")

        self.pause(1)
        try:
            self.click_item(self.locator_open_menu_colour)  # нажимаем на меню цвета
            print(f"Нажатие на меню выбора цвета - ОК")
            self.pause(2)
            self.click_item(self.locator_select_colour)  # выбор цвета
            print(f"Выбор цвета - ОК")
            self.pause(2)
        except BaseException:
            pass
        self.click_item(self.locator_open_view)  # открываем превью
        print(f"Показ првеью - ОК")
        self.pause(1)
        try:
            self.click_item(self.locator_next_view) # следущее превью
            print(f"Нажатие на следующее превью - ОК")
            self.pause(1)
        except BaseException:
            pass
        self.driver.execute_script("window.scrollTo(0, 400)")
        print(f"Прокрутка страницы - ОК")
        self.pause(1)
        self.click_item(self.locator_close_view) # закрываем превью
        print(f"Закрытие првеью - ОК")


        self.pause(1)
        self.click_item(self.locator_credit_6) # рассрочка на 6 месяцев
        print(f"Выбор рассрочки на 6 месяцев' - ОК")
        self.pause(2)
        self.click_item(self.locator_credit_12) # рассрочка на 12 месяцев
        print(f"Выбор рассрочки на 12 месяцев' - ОК")
        self.pause(2)
        self.click_item(self.locator_choose_seller)  # выбираем продавца
        print(f"Выбор продавца' - ОК")
        self.pause(1)
        self.click_item(self.locator_close)  # закрываем QR
        print(f"Закрытие QR - ОК")
        self.click_item(self.locator_main)
