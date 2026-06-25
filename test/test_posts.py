import pytest

from api_client import get_post, create_post, update_post, patch_post, delete_post, get_all_posts


def test_post_title(post_data):
    assert post_data["title"] == "sunt aut facere repellat provident occaecati excepturi optio reprehenderit"

def test_post_id(post_data):
    assert post_data["id"] == 1

def test_post_user_id_from_fixture(post_data):
    assert post_data["userId"] == 1

def test_post_status_code():
    response = get_post(1)

    assert response.status_code == 200

@pytest.mark.parametrize(
    "post_id, expected_user_id",
    [
        (1, 1),
        (2, 1),
        (11, 2)
        
    ]
)

def test_post_user_id_parametrize(post_id, expected_user_id):
    response = get_post(post_id)

    data = response.json()

    assert response.status_code == 200
    assert data["userId"] == expected_user_id


def test_create_post():
    payload = {
        "title": "Test title",
        "body": "Test body",
        "userId": 1
    }

    response = create_post(payload)
    data = response.json()

    assert response.status_code == 201
    assert data["title"] == "Test title"
    assert data["body"] == "Test body"
    assert data["userId"] == 1

def test_update_post():
    payload = {
        "id": 1,
        "title": "Updated title",
        "body": "Updated body",
        "userId": 1
    }

    response = update_post(1, payload)
    data = response.json()

    assert response.status_code == 200
    assert data["id"] == 1
    assert data["title"] == "Updated title"
    assert data["body"] == "Updated body"
    assert data["userId"] == 1

def test_patch_post_title():
    payload = {
        "title": "Patched title"
    }

    response = patch_post(1, payload)
    data = response.json()

    assert response.status_code == 200
    assert data["title"] == "Patched title"

def test_delete_post():
    response = delete_post(1)

    assert response.status_code == 200

def test_get_all_posts_status_code():
    response = get_all_posts()
    assert response.status_code == 200

def test_get_all_posts_not_empty():
    response = get_all_posts()
    data = response.json()

    assert response.status_code == 200
    assert isinstance(data, list)
    assert len(data) > 0

def test_get_all_posts_first_item_has_keys():
    response = get_all_posts()
    data = response.json()
    first_post = data[0]

    assert response.status_code == 200
    assert "id" in first_post
    assert "title" in first_post
    assert "body" in first_post
    assert "userId" in first_post

def test_get_all_posts_all_items_have_keys():
    response = get_all_posts()
    data = response.json()

    assert response.status_code == 200

    for post in data:
        assert "id" in post
        assert "title" in post
        assert "body" in post
        assert "userId" in post