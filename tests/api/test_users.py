import pytest

def test_users_list_returns_10_users(users_client):
    response = users_client.get_users()
    assert response.status_code == 200, response.text

    users = response.json()
    assert isinstance(users, list),  f"Ожидали список, пришло: {type(users)}"
    assert len(users) == 10, f"Ожидали 10 пользователей, пришло {len(users)}"

def test_all_user_emails_contain_at_sign(users_client):
    users = users_client.get_users().json()
    bad_emails = [u["email"] for u in users if "@" not in u["email"]]
    assert not bad_emails, f"email без @: {bad_emails}"

def test_users_id_are_unique(users_client):
    users = users_client.get_users().json()
    ids = [u["id"] for u in users]
    assert len(ids) == len(set(ids)), f"there're duplicates id: {ids}"

def test_user_has_address_with_city_and_geo(users_client):
    user = users_client.get_user(1).json()
    address = user["address"]           # вкладываемся на уровень глубже
    assert address["city"], "city is empty"   # пустая строка = False → тест упадёт
    assert "geo" in address, f"Нет координат в адресе: {address}"

@pytest.mark.parametrize("user_id", [1, 5, 10])
def test_posts_filtered_by_user_belong_only_to_that_user(posts_client, user_id):
    posts = posts_client.get_posts(user_id=user_id).json()

    # Сначала проверяем, что список не пустой. Иначе следующая проверка
    # «все посты принадлежат пользователю» пройдёт на пустом списке — ложный зелёный тест!
    assert posts, f"for userId={user_id} has no posts returned"

    wrong_posts = [p["id"] for p in posts if p["userId"] != user_id]
    assert not wrong_posts, f"filter userId={user_id} returned other users' posts: {wrong_posts}"

@pytest.mark.parametrize("user_id", [0, 999, -1])
def test_user_non_existent_id_is_404(users_client, user_id):
    response = users_client.get_user(user_id)
    assert response.status_code == 404, f"id={user_id}: {response.status_code}"