import pytest

from api_client import get_user, get_all_users

def test_user_name(user_data):
    assert user_data["username"] == "Bret"


def test_user_email_from_fixture(user_data):
    assert user_data["email"] == "Sincere@april.biz"

def test_user_id(user_data):
    assert user_data["id"] == 1

def test_users_404():
    response = get_user(9999)

    assert response.status_code == 404

@pytest.mark.parametrize(
    "user_id, expected_username",
    [
        (1, "Bret"),
        (2, "Antonette"),
        (3, "Samantha"),
        (4, "Karianne"),
        (5, "Kamren"),
        (6, "Leopoldo_Corkery"),
        (7, "Elwyn.Skiles")
    ]
)
def test_user_username(user_id, expected_username):
    response = get_user(user_id)
    data = response.json()

    assert response.status_code == 200
    assert data["username"] == expected_username

@pytest.mark.parametrize(
    "user_id, expected_email",
    [
        (1, "Sincere@april.biz"),
        (2, "Shanna@melissa.tv"),
        (3, "Nathan@yesenia.net")
    ]
)

def test_user_email_parametrize(user_id, expected_email):
    response = get_user(user_id)
    data = response.json()

    assert response.status_code == 200
    assert data["email"] == expected_email

def test_get_all_users_status_code():
    response = get_all_users()
    assert response.status_code == 200