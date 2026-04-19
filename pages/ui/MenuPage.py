from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class MenuPage:
    def __init__(self, driver: WebDriver):
        self.__driver = driver

    @allure.step("Проверить, что все разделы меню отображаются")
    def are_menu_sections_visible(self, sections: list) -> bool:
        for section in sections:
            try:
                WebDriverWait(self.__driver, 5).until(
                    EC.visibility_of_element_located((By.XPATH, f"//*[contains(text(), '{section}')]"))
                )
            except:
                return False
        return True

    @allure.step("Открыть страницу профиля")
    def open_profile(self):
        profile_menu = WebDriverWait(self.__driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Мой профиль')]"))
        )
        profile_menu.click()

    @allure.step("Проверить, что кнопка выхода отображается")
    def is_logout_button_visible(self) -> bool:
        try:
            WebDriverWait(self.__driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-testid='logout-link']"))
            )
            return True
        except:
            return False

    @allure.step("Перейти в раздел 'Отчеты'")
    def go_to_reports(self):
        reports_link = WebDriverWait(self.__driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[text()='Отчеты']"))
        )
        reports_link.click()

    @allure.step("Получить количество открытых задач")
    def get_open_tasks_count(self) -> int:
        count_element = WebDriverWait(self.__driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".stats-aggregated-report__num"))
        )
        text = count_element.text
        return int(text) if text.isdigit() else 0