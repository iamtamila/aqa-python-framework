import pytest
from framework.models.post import Post

def test_get_post_returns_200_valid_schema(posts_client):
    response = posts_client.get_post(1)
    assert response.status_code == 200, (
        f"Ожидаемый 200, получили {response.status_code}: {response.text}"
    )
    post = Post.model_validate(response.json())
    assert post.id == 1

def test_create_post_returns_201_valid_schema(posts_client):
    payload = {"title": "AQA", "body": "first post", "userId": 1}
    response = posts_client.create_post(payload)
    assert response.status_code == 201, response.text
    created = Post.model_validate(response.json())
    assert created.title == payload["title"]
    assert created.body == payload["body"]
    
@pytest.mark.parametrize("post_id", [0, -1, 9999])
def test_get_nonexistent_post_returns_404(posts_client, post_id):
    response = posts_client.get_post(post_id)
    assert response.status_code == 404, f"id={post_id}: {response.status_code}"




    