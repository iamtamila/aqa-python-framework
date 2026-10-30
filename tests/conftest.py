import pytest
from framework.clients.posts_client import PostsClient

@pytest.fixture(scope="session")
def posts_client():
    client = PostsClient()
    yield client
    client.session.close()
