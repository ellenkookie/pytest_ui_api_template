from selenium.webdriver.support import expected_conditions as EC
from pages.AuthPage import AuthPage
from pages.MainPage import MainPage


def auth_test(browser):
    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login_as("elenhayro2000@gmail.com", "7_kMPA2TrLxKPlanit")
    assert auth_page.is_logged_in()
    # browser.save_screenshot("after_login.png")
    # print("✅ Авторизация успешна")

    main_page = MainPage(browser)
    main_page.open_profile()
    assert main_page.get_current_url().endswith("settings-account")
    display_name = main_page.get_display_name()
    assert display_name == "Elen Hayrapetyan"

