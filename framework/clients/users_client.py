import requests
from framework.config import API_BASE_URL

class UsersClient:
    def __init__(self, base_url: str = API_BASE_URL):
        self.base_url = base_url
        self.session = requests.Session()

    def get_users(self) -> requests.Response:
        return self.session.get(f"{self.base_url}/users", timeout = 10)
    def get_user(self, user_id:int) -> requests.Response:
        return self.session.get(f"{self.base_url}/users/{user_id}", timeout = 10)

