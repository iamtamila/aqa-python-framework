import pytest
from framework.models.post import Post
from framework.helpers.assertions import assert_status
pytestmark = pytest.mark.api

@pytest.mark.smoke
def test_get_post_returns_200_valid_schema(posts_client):
    response = posts_client.get_post(1)
    assert_status(response, 200)
    post = Post.model_validate(response.json())
    assert post.id == 1

def test_create_post_returns_201_valid_schema(posts_client):
    payload = {"title": "AQA", "body": "first post", "userId": 1}
    response = posts_client.create_post(payload)
    assert_status(response, 201)
    created = Post.model_validate(response.json())
    assert created.title == payload["title"]
    assert created.body == payload["body"]
    
@pytest.mark.parametrize("post_id", [0, -1, 9999])
def test_get_nonexistent_post_returns_404(posts_client, post_id):
    response = posts_client.get_post(post_id)
    assert_status(response, 404)




    