import allure
import pytest
from pages.api.BoardApi import BoardApi
from config import BASE_URL_API

@pytest.mark.api
@allure.feature("API")
@allure.story("Доски")
@allure.title("Получение списка досок проекта")
def test_get_boards_list(auth_headers, project_id):
    api = BoardApi(BASE_URL_API, auth_headers)
    with allure.step(f"Получить список досок для проекта {project_id}"):
        boards = api.get_boards(project_id=project_id)
    with allure.step("Проверить, что в ответе есть поле 'content'"):
        assert "content" in boards


@allure.feature("API")
@allure.story("Доски")
@allure.title("Создание доски в проекте")
@allure.severity(allure.severity_level.CRITICAL)
def test_create_board(auth_headers, project_id):
    board_api = BoardApi(BASE_URL_API, auth_headers)
    board_name = "Тестовая доска"

    with allure.step(f"Создать доску с названием '{board_name}' в проекте {project_id}"):
        response = board_api.create_board(project_id, board_name)

    with allure.step("Проверить, что в ответе есть поле 'id'"):
        assert "id" in response
