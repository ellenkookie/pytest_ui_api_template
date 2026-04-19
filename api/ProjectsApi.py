import requests
import allure

class ProjectApi:
    """Класс для работы с проектами API Yougile"""
    def __init__(self, base_url: str, headers: dict):
        self.base_url = base_url
        self.headers = headers

    @allure.step("Создать проект с названием '{title}'")
    def create_project(self, title: str, users: dict = None, timeout: int = 30) -> dict:
        payload = {"title": title}
        if users:
            payload["users"] = users
        resp = requests.post(
            f"{self.base_url}/projects",
            json=payload,
            headers=self.headers,
            timeout = timeout
        )
        return resp.json()

    @allure.step("Получить проект по ID {project_id}")
    def get_project(self, project_id: str, timeout: int = 30) -> dict:
        resp = requests.get(
            f"{self.base_url}/projects/{project_id}",
            headers=self.headers,
            timeout=timeout
        )
        return resp.json()

    @allure.step("Обновить проект {project_id}: новое название '{new_title}'")
    def update_project(self, project_id: str, new_title: str, timeout: int = 30) -> dict:
        payload = {"title": new_title}
        resp = requests.put(
            f"{self.base_url}/projects/{project_id}",
            json=payload,
            headers=self.headers,
            timeout=timeout
        )
        return resp.json()
