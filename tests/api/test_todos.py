import pytest
from pydantic import TypeAdapter  
from framework.models.todo import Todo
from framework.helpers.assertions import assert_status
pytestmark = pytest.mark.api

@pytest.mark.smoke
def test_get_todos_return_200(todos_client):
    response = todos_client.get_todos()
    assert_status(response, 200)
    todos = TypeAdapter(list[Todo]).validate_python(response.json())
    assert todos, f"Задачи не пришли"

def test_get_todos_with_completed_return_200(todos_client):
    response = todos_client.get_todos(completed = True)
    assert_status(response, 200)
    todos = TypeAdapter(list[Todo]).validate_python(response.json())
    assert todos, f"no todos returned"
    wrong = [t.id for t in todos if t.completed is not True]
    assert not wrong, f"the following todos not completed: {wrong}"
