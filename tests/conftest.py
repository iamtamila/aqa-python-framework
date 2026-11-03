import pytest
from framework.clients.users_client import UsersClient
from framework.clients.posts_client import PostsClient

@pytest.fixture(scope="session")
def posts_client():
    client = PostsClient()
    yield client
    client.session.close()

@pytest.fixture(scope="session")
def users_client():
    client = UsersClient()
    yield client
    client.session.close()
    