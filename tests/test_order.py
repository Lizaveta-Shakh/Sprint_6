import allure
import pytest

from data import PERSON_1, PERSON_2
from pages.order_page import OrderPage

from data import ExpectedText

class TestOrder:
    @allure.title('Оформление заказа')
    @pytest.mark.parametrize('testpersons', [PERSON_1, PERSON_2])
    def test_create_an_order_with_correct_data(self, driver, testpersons):
        order_page = OrderPage(driver)
        order_page.wait_for_order_page()
        order_page.fill_the_order_form(
            testpersons['name'],
            testpersons['last_name'],
            testpersons['address'],
            testpersons['phone_number'],
            testpersons['delivery_date'],
            testpersons['rental_period'],
            testpersons['comment']
        )
        assert order_page.check_order_created()
