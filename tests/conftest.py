import pytest
import requests
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from config import LOGIN, PASSWORD, COMPANY_ID, BASE_URL_API
from config import UI_LOGIN, UI_PASSWORD
from pages.api.ProjectsApi import ProjectApi

# ---------- UI фикстуры ----------
@pytest.fixture(scope="function")
def browser():
    with allure.step("Открыть и настроить браузер"):
        browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        browser.implicitly_wait(10)
        browser.maximize_window()
        yield browser

    with allure.step("Закрыть браузер"):
        browser.quit()


@pytest.fixture
def ui_credentials():
    return {"email": UI_LOGIN, "password": UI_PASSWORD}

# ---------- API фикстуры ----------
@pytest.fixture(scope="session")
def auth_headers():
    payload = {
        "login": LOGIN,
        "password": PASSWORD,
        "companyId": COMPANY_ID
    }
    resp = requests.post(f"{BASE_URL_API}/auth/keys/get", json=payload)
    keys = resp.json()
    token = None
    for key_info in keys:
        if not key_info.get("deleted"):
            token = key_info["key"]
            break
    assert token is not None, "Не удалось получить токен"
    return {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }


@pytest.fixture(scope="session")
def project_id(auth_headers):
    api = ProjectApi(BASE_URL_API, auth_headers)
    response = api.create_project("Проект для досок")
    return response["id"]