import allure

from curl import order_page_url, main_page_url
from pages.main_page import MainPage

class TestButtons:
    @allure.title('После нажатия на "Заказать" в шапке страницы происходит переход на оформление заказа')
    def test_click_on_the_order_button_page_header_redirect_to_order(self, driver):
        main_page = MainPage(driver)
        main_page.wait_for_main_page()
        main_page.click_the_button_order_on_the_top()
        assert main_page.is_current_url(order_page_url)

    @allure.title('Нажатие на Заказать внизу страницы ведет на страницу оформления заказа')
    def test_click_on_the_order_button_below_redirect_to_order(self, driver):
        main_page = MainPage(driver)
        main_page.wait_for_main_page()
        main_page.scroll_and_click_order_button_below()
        assert main_page.is_current_url(order_page_url)

class TestLinks:
    @allure.title('После нажатия на лого Самокат в хедере происходит переход на главную Самоката')
    def test_click_on_the_scooter_logo_redirect_to_the_main_page(self, driver):
        main_page = MainPage(driver)
        main_page.wait_for_main_page()
        main_page.click_the_scooter_logo()
        assert main_page.is_current_url(main_page_url)

    @allure.title('После нажатия на лого Яндекс в хедере происходит переход на главную Дзена')
    def test_click_on_the_yandex_logo_redirect_to_the_dzen(self, driver):
        main_page = MainPage(driver)
        main_page.wait_for_main_page()
        main_page.click_the_yandex_logo()
        main_page.wait_for_two_windows()
        main_page.redirect_to_dzen()
        assert main_page.current_url_contains('dzen.ru')