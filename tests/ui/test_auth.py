import allure
from pages.ui.AuthPage import AuthPage
from pages.ui.MainPage import MainPage
import pytest


@pytest.mark.ui
@allure.feature("UI")
@allure.story("Авторизация")
@allure.title("Успешный вход в аккаунт")
@allure.severity(allure.severity_level.CRITICAL)
def test_auth(browser, ui_credentials) -> None:
    auth_page = AuthPage(browser)
    with allure.step("Перейти на страницу авторизации и войти"):
        auth_page.go()
        auth_page.login_as(ui_credentials["email"], ui_credentials["password"])

    with allure.step("Проверить, что авторизация прошла успешно"):
        assert auth_page.is_logged_in()


@allure.feature("UI")
@allure.story("Профиль")
@allure.title("Проверка URL профиля и отображаемого имени")
@allure.severity(allure.severity_level.NORMAL)
def test_profile_info(browser, ui_credentials) -> None:
    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login_as(ui_credentials["email"], ui_credentials["password"])
    assert auth_page.is_logged_in()

    main_page = MainPage(browser)
    with allure.step("Открыть страницу профиля"):
        main_page.open_profile()
    current_url = main_page.get_current_url()
    with allure.step(f"Проверить, что URL {current_url} заканчивается на settings-account"):
        assert main_page.get_current_url().endswith("settings-account")

    with allure.step("Проверить отображаемое имя пользователя"):
        display_name = main_page.get_display_name()
        assert display_name == "Elen Hayrapetyan"
