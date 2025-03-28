**Проект по атоматизации тестирования сервиса Яндекс.Самокат**

В проекте собраны UI-тесты веб-приложения Яндекс Самокат (https://qa-scooter.praktikum-services.ru/)


Для запуска автотестов необходим установленный браузер Mozilla Firefox.

**Стек**:
Python 3.11
PyTest
Selenium
Allure
Firefox 

**Установка зависимостей:** 
pip install -r requirements.txt

**Запуск тестов:** 
python -m pytest .\tests\ 

**Запустить Allure для просмотра отчетов**
allure serve allure-results

**Реализованные тесты:**

Файл **test_drop_down_list.py** содержит проверки раздела вопросов на главной странице.
test_click_on_question_returns_correct_answer - проверяет тексты ответа, в соответсвии с выбранным вопросов. Использована параметризация.

Файл **test_links.py** содержит проверки функциональности гиперссылок и кнопок на главной.
test_click_on_the_order_button_page_header_redirect_to_order проверяет, что при нажатии на кнопку заказать в хедере происходит переход на страницу заказа
test_click_on_the_order_button_below_redirect_to_order проверяет, что при нажатии на кнопку заказать на главной странице происходит переход на страницу заказа

test_click_on_the_scooter_logo_redirect_to_the_main_page - проверяет, что при нажатии на лого Самокат в хедере происходит переход на главную стр самоката
test_click_on_the_yandex_logo_redirect_to_the_dzen - проверка перехода на стр Дзена при нажатии на лого Яндекс в хедере

Файл **test_order.py** срдержит проверки создания заказа 
test_create_an_order_with_correct_data - проверяет, что при заполнении полей приофрмлении заказа корректными данными заказ создается.


