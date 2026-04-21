from pages.api.ProjectsApi import ProjectApi
from config import BASE_URL_API
import allure
import pytest


@pytest.mark.api
@allure.feature("API")
@allure.story("Проекты")
@allure.title("Создание проекта")
@allure.severity(allure.severity_level.CRITICAL)
def test_create_project(auth_headers) -> None:
    api = ProjectApi(BASE_URL_API, auth_headers)
    with allure.step("Создать проект с названием 'API-проект'"):
        response = api.create_project("API-проект")
    with allure.step("Проверить, что в ответе есть id"):
        assert "id" in response
    with allure.step("Проверить, что id является строкой"):
        assert isinstance(response["id"], str)


@allure.feature("API")
@allure.story("Проекты")
@allure.title("Получение проекта по ID")
@allure.severity(allure.severity_level.NORMAL)
def test_get_project_by_id(auth_headers) -> None:
    api = ProjectApi(BASE_URL_API, auth_headers)
    with allure.step("Создать проект 'Проект для получения'"):
        create_response = api.create_project("Проект для получения")
    assert "id" in create_response
    project_id = create_response["id"]

    with allure.step(f"Получить проект по ID {project_id}"):
        project = api.get_project(project_id)
    with allure.step("Проверить, что ID проекта совпадает"):
        assert project["id"] == project_id
    with allure.step("Проверить, что название проекта совпадает"):
        assert project["title"] == "Проект для получения"


@allure.feature("API")
@allure.story("Проекты")
@allure.title("Обновление названия проекта")
@allure.severity(allure.severity_level.NORMAL)
def test_update_project(auth_headers) -> None:
    api = ProjectApi(BASE_URL_API, auth_headers)
    with allure.step("Создать проект 'Старое название'"):
        create_response = api.create_project("Старое название")
    assert "id" in create_response
    project_id = create_response["id"]

    with allure.step("Обновить название проекта на 'Новое название'"):
        update_response = api.update_project(project_id, "Новое название")
    with allure.step("Проверить, что в ответе есть id"):
        assert "id" in update_response
    with allure.step("Проверить, что id совпадает с id созданного проекта"):
        assert update_response["id"] == project_id
