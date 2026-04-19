from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class AuthPage:
    def __init__(self, driver: WebDriver) -> None:
        self.__url = "https://ru.yougile.com/team/"
        self.__driver = driver

    @allure.step("Перейти на страницу авторизации")
    def go(self):
        self.__driver.get(self.__url)

    @allure.step("Авторизоваться под {email}:{password}")
    def login_as(self, email: str, password: str):
        # Ввести email
        email_field = WebDriverWait(self.__driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "input[type='email']"))
        )
        email_field.send_keys(email)

        # Ввести пароль
        password_field = WebDriverWait(self.__driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "input[type='password']"))
        )
        password_field.send_keys(password)

        # Нажать "Войти"
        submit_btn = WebDriverWait(self.__driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Войти')]"))
        )
        submit_btn.click()

    def is_logged_in(self) -> bool:
        try:
            WebDriverWait(self.__driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'Мой профиль')]"))
            )
            return True
        except:
            return False
