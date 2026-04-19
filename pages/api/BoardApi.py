import requests
import allure
from tenacity import retry, stop_after_attempt, wait_fixed

class BoardApi:
    def __init__(self, base_url: str, headers: dict):
        self.base_url = base_url
        self.headers = headers

    @retry(stop=stop_after_attempt(3), wait=wait_fixed(5))
    @allure.step("Получить список досок")
    def get_boards(self, project_id: str = None, include_deleted: bool = False, limit: int = 50,
                   offset: int = 0) -> dict:
        params = {
            "includeDeleted": str(include_deleted).lower(),
            "limit": limit,
            "offset": offset
        }
        if project_id:
            params["projectId"] = project_id

        resp = requests.get(
            f"{self.base_url}/boards",
            headers=self.headers,
            params=params,
            timeout=60
        )
        return resp.json()

    @retry(stop=stop_after_attempt(3), wait=wait_fixed(5))
    def create_board(self, project_id: str, title: str) -> dict:
        payload = {
                "title": title,
                "projectId": project_id
            }
        resp = requests.post(
                f"{self.base_url}/boards",
                json=payload,
                headers=self.headers,
                timeout=60
            )
        return resp.json()