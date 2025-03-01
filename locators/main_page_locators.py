from selenium.webdriver.common.by import By

class MainPageLocators:
    ORDER_BUTTON_TOP = [By.CSS_SELECTOR, '[class^=Header_Nav] button']
    ORDER_BUTTON_BELOW = [By.CSS_SELECTOR, '[class^=Home_FinishButton] button']
    FAQ_LINK = [By.CSS_SELECTOR, '[class^=Home_FourPart] [class^=Home_SubHeader]']
    SCOOTER_LINK = [By.CSS_SELECTOR, '[class^=Header_Logo] [class^=Header_LogoScooter]']
    YANDEX_LINK = [By.CSS_SELECTOR, '[class^=Header_Logo] [class^=Header_LogoYandex]']
    PAGE = [By.CSS_SELECTOR, '[class^=Home_FourPart]']

    @staticmethod
    def question_number(question):
        return By.CSS_SELECTOR, f'.accordion .accordion__item:nth-child({question}) .accordion__heading div'

    @staticmethod
    def answer_number(answer):
        return By.CSS_SELECTOR, f'.accordion .accordion__item:nth-child({answer}) .accordion__panel'


