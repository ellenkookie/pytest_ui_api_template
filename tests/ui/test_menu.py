import allure
from pages.ui.AuthPage import AuthPage
from pages.ui.MenuPage import MenuPage

@allure.feature("UI")
@allure.story("Меню")
@allure.title("Проверка отображения разделов меню")
@allure.description("Проверяет, что после входа в аккаунт все пункты меню отображаются")
@allure.severity(allure.severity_level.NORMAL)
def test_menu_sections_visible(browser, ui_credentials):
    with allure.step("Авторизация"):
        auth_page = AuthPage(browser)
        auth_page.go()
        auth_page.login_as(ui_credentials["email"], ui_credentials["password"])
        assert auth_page.is_logged_in()

    menu_page = MenuPage(browser)
    sections = ["Мой профиль", "Мои задачи", "Проекты", "Мессенджер", "Лента событий", "Отчеты"]
    with allure.step(f"Проверить наличие разделов: {sections}"):
        assert menu_page.are_menu_sections_visible(sections), "Не все разделы меню отображаются"

@allure.feature("UI")
@allure.story("Профиль")
@allure.title("Проверка видимости кнопки выхода")
@allure.severity(allure.severity_level.NORMAL)
def test_logout_button_visible(browser, ui_credentials):
    with allure.step("Авторизация"):
        auth_page = AuthPage(browser)
        auth_page.go()
        auth_page.login_as(ui_credentials["email"], ui_credentials["password"])

    menu_page = MenuPage(browser)
    with allure.step("Открыть профиль и проверить кнопку выхода"):
        menu_page.open_profile()
        assert menu_page.is_logout_button_visible(), "Кнопка выхода не отображается"


@allure.feature("UI")
@allure.story("Отчеты")
@allure.title("Проверка количества открытых задач в отчетах")
@allure.severity(allure.severity_level.CRITICAL)
def test_open_tasks_count(browser, ui_credentials):
    auth_page = AuthPage(browser)
    with allure.step("Авторизация"):
        auth_page.go()
        auth_page.login_as(ui_credentials["email"], ui_credentials["password"])
        assert auth_page.is_logged_in()

    menu_page = MenuPage(browser)
    with allure.step("Перейти в раздел 'Отчеты'"):
        menu_page.go_to_reports()

    with allure.step("Получить количество открытых задач"):
        tasks_count = menu_page.get_open_tasks_count()

    with allure.step(f"Проверить, что количество задач равно 20 (фактически: {tasks_count})"):
        assert tasks_count == 20, f"Ожидалось 20 открытых задач, получено {tasks_count}"