import requests
from framework.config import API_BASE_URL

class TodosClient:
    def __init__(self, base_url: str = API_BASE_URL):
        self.base_url = base_url
        self.session = requests.Session()

    def get_todos(self, completed: bool | None = None) -> requests.Response:
        params = {"completed": "true" if completed else "false"} if completed is not None else None
        return self.session.get(f"{self.base_url}/todos", params = params, timeout = 10)