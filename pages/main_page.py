import allure

from curl import main_page_url
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Ожидание загрузки главной страницы')
    def wait_for_main_page(self):
        self.wait_for_page(main_page_url)

    @allure.step('Ожидание загрузки блока вопросов')
    def wait_for_questions_list(self):
        self.wait_for_element(MainPageLocators.FAQ_LINK)

    @allure.step('Развернуть ответ вопроса')
    def click_on_question(self, question_number, timeout=10):
        question_locator = MainPageLocators.question_number(question_number)
        self.scroll_to_element(question_locator)
        self.js_click_on_element(question_locator, timeout)

    @allure.step('Ожидание видимости ответа')
    def wait_for_answer_visible(self, answer_number):
        self.wait_for_element(MainPageLocators.answer_number(answer_number))

    @allure.step('Проверка текста ответа')
    def check_answer_text(self, expected_text, answer_number):
        actual_text = self.get_text_on_element(MainPageLocators.answer_number(answer_number))
        return actual_text == expected_text

    @allure.step('Ожидание перехода на "Дзен"')
    def redirect_to_dzen(self):
        self.wait_url_change('dzen')

    @allure.step('Нажать на кнопку Заказать вверху страницы')
    def click_the_button_order_on_the_top(self):
        self.click_on_element(MainPageLocators.ORDER_BUTTON_TOP)

    @allure.step('Скролл и клик на кнопку Заказать внизу страницы')
    def scroll_and_click_order_button_below(self):
        self.scroll_to_element(MainPageLocators.ORDER_BUTTON_BELOW)
        self.click_on_element(MainPageLocators.ORDER_BUTTON_BELOW, timeout=50)

    @allure.step('Клик на логотип самоката')
    def click_the_scooter_logo(self):
        self.click_on_element(MainPageLocators.SCOOTER_LINK)

    @allure.step('Клик на логотип Яндекса')
    def click_the_yandex_logo(self):
        self.click_on_element(MainPageLocators.YANDEX_LINK)





