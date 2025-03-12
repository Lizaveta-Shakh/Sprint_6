import allure

from curl import  order_page_url
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage
from data import ExpectedText

class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Дождаться загрузку страницы заказа')
    def wait_for_order_page(self):
        self.wait_for_page(order_page_url)
        self.click_on_element(OrderPageLocators.COOKIE_ACCEPT_BUTTON)

    @allure.step('Заполнение полей ввода на странице заказа самоката')
    def fill_the_order_form(self, name, last_name, address, phone_number, delivery_date, rental_period, comment):
        self.send_keys_to_input(OrderPageLocators.NAME_FIELD, name)
        self.send_keys_to_input(OrderPageLocators.LAST_NAME_F, last_name)
        self.send_keys_to_input(OrderPageLocators.ADDRESS_F, address)
        self.click_on_element(OrderPageLocators.METRO_FIELD)
        self.scroll_to_element(OrderPageLocators.STATION_NAME)
        self.click_on_element(OrderPageLocators.STATION_NAME)
        self.send_keys_to_input(OrderPageLocators.PHONE_FIELD, phone_number)
        self.click_on_element(OrderPageLocators.FURTHER_BUTTON)


        self.click_on_element(OrderPageLocators.INPUT_DELIVERY_DATE)
        if delivery_date == "today":
            self.click_on_element(OrderPageLocators.CALENDAR_DATE_TODAY)
        else:
            self.click_on_element(OrderPageLocators.CALENDAR_DATE_TOMORROW)
        self.click_on_element(OrderPageLocators.FIELD_RENT_LIMIT)
        if rental_period == "1 день":
            self.click_on_element(OrderPageLocators.RENTAL_PERIOD_1_DAY)
        else:
            self.click_on_element(OrderPageLocators.RENTAL_PERIOD_2_DAYS)

        self.click_on_element(OrderPageLocators.INPUT_CHECKBOX_COLOR_BLACK)
        self.click_on_element(OrderPageLocators.COMMENT_FIELD)
        self.send_keys_to_input(OrderPageLocators.COMMENT_FIELD, comment)
        self.click_on_element(OrderPageLocators.ORDER_BUTTON_ORDER_PAGE)
        self.click_on_element(OrderPageLocators.CONFIRMATION_BUTTON)

    @allure.step('Получаем и сравниваем текст элемента окна готовности заказа')
    def check_order_created(self):
        return self.text_is_visible(OrderPageLocators.ORDER_DONE, ExpectedText.ORDER_CREATED_TEXT)

    @allure.step('Ждем появления кнопки просмотра заказа')
    def wait_find_element(self):
        self.find_element(OrderPageLocators.STATUS_BUTTON)




