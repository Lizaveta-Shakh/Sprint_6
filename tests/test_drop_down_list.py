import allure
import pytest

import data

from pages.main_page import MainPage


class TestFAQ:
    @allure.title('При нажатии на вопрос отображается корректый текст ответа')
    @pytest.mark.parametrize('question_number, expected_text', data.Data.questions_answers)
    def test_click_on_question_returns_correct_answer(self, driver, question_number, expected_text):
        main_page = MainPage(driver)
        main_page.wait_for_main_page()
        main_page.wait_for_questions_list()
        main_page.click_on_question(question_number)
        main_page.wait_for_answer_visible(question_number)
        assert main_page.check_answer_text(expected_text, question_number)