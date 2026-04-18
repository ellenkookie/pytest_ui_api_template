from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage:
    def __init__(self, driver: WebDriver) -> None:
        self.__driver = driver

    def get_current_url(self):
        return self.__driver.current_url

    def open_profile(self):
        profile_menu = WebDriverWait(self.__driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Мой профиль')]"))
        )
        profile_menu.click()

    def get_display_name(self) -> str:
        name_field = WebDriverWait(self.__driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@value='Elen Hayrapetyan']"))
        )
        return name_field.get_attribute("value")

