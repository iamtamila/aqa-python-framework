import requests
from framework.config import API_BASE_URL


class PostsClient:
    def __init__(self, base_url: str = API_BASE_URL):
        self.base_url = base_url
        self.session = requests.Session()

    def get_post(self, post_id: int) -> requests.Response:
        return self.session.get(f"{self.base_url}/posts/{post_id}", timeout=10)

    def create_post(self, payload: dict) -> requests.Response:
        return self.session.post(f"{self.base_url}/posts", json=payload, timeout=10)

    def get_posts(self, user_id: int | None = None) -> requests.Response:
        params = {"userId": user_id} if user_id is not None else None
        return self.session.get(f"{self.base_url}/posts", params = params, timeout = 10)
