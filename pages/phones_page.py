import time
from base.base import Base
from pages.product_page import product_page


class phones_class(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators

    locator_choose_city = "//*[@id='dialogService']/div/div[1]/div[1]/div/ul[1]/li[13]/a"
    locator_category = "//*[@id='scroll-to']/div[1]/div[1]/div/ul/li/span[1]"
    locator_price_filter_more_500 = "//*[@id='scroll-to']/div[1]/div[2]/div/div[7]/label[2]/span[1]"
    locator_select_brand_1 = "//*[@id='scroll-to']/div[1]/div[3]/div/div[1]/label[2]/span[1]"
    locator_sort_click = "//*[@id='scroll-to']/div[3]/div/div/div[2]/div"
    locator_sort_expensive = "//*[@id='scroll-to']/div[3]/div/div/div[2]/ul/li[4]"
    locator_select_product_1 = "//*[@id='scroll-to']/div[4]/div[1]/div[1]"

    def activities_phones_page(self, title_category):
        self.pause()
        print("\nCurrent url: " + self.driver.current_url)
        self.click_item(self.locator_choose_city)  # выбираем город
        print(f"Переход на страницу '{self.getter(self.locator_category).text}' - OK".replace('\n',' '))

        save_title_category_page = self.getter(self.locator_category).text.replace(' и ',' ')
        print(f"Сохранение '{save_title_category_page}' на странице категории, в переменную - ОК")

        self.assert_value(title_category, save_title_category_page)
        print(f"Соответствие '{save_title_category_page}' - ОК")

        self.pause()
        self.click_item(self.locator_price_filter_more_500)  # фильтруем по цене >500 тыс. тг
        print(f"Применение фильтра по цене' - ОК")
        self.pause()
        self.click_item(self.locator_select_brand_1)  # фильтруем по первому бренду
        print(f"Применение фильтра по бренду' - ОК")
        self.pause()
        self.click_item(self.locator_sort_click)  # выбор меню сортировки
        print(f"Нажатие на меню сортировки' - ОК")
        self.pause()
        self.click_item(self.locator_sort_expensive)  # сортировка по убыванию цены
        print(f"Сортировка по цене' - ОК")
        self.pause()
        self.click_item(self.locator_select_product_1)  # выбираем первый продукт
        print(f"Выбор продукта' - ОК")

        product_page(self.driver).activities_product_page() # переходим на страницу продукта
