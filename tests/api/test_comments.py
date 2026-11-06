import pytest
from pydantic import TypeAdapter  
from framework.models.comment import Comment
from framework.helpers.assertions import assert_status
pytestmark = pytest.mark.api

def test_get_posts_comments_returns_200(posts_client):
    response = posts_client.get_post_comments(1)
    assert_status(response, 200)
    comments = TypeAdapter(list[Comment]).validate_python(response.json())
    assert comments, "Комментарии к посту 1 не пришли"

    wrong = [c.id for c in comments if c.postId != 1]
    assert not wrong, f"Комментарии чужих постов: {wrong}"

    bad_emails = [c.email for c in comments if "@" not in c.email]
    assert not bad_emails, f"Комментарий без @ в email: {bad_emails}"