import pytest

from qase.pytest import qase
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

@qase.id(1)
def test_get_all_users_status_code():
    response = get_all_users()
    assert response.status_code == 200

def test_get_all_users_not_empty():
    response = get_all_users()
    data = response.json()

    assert response.status_code == 200
    assert len(data) > 0

def test_get_all_users_first_item_has_keys():
    response = get_all_users()
    data = response.json()

    assert response.status_code == 200

    first_user = data[0]

    assert "id" in first_user
    assert "name" in first_user
    assert "username" in first_user
    assert "email" in first_user
    assert "address" in first_user

def test_get_all_users_all_items_have_keys():
    response = get_all_users()
    data = response.json()
    assert response.status_code == 200
    for user in data:
        assert "id" in user
        assert "name" in user
        assert "username" in user
        assert "email" in user
        assert "address" in user

def test_get_all_users_address_has_keys():
    response = get_all_users()
    data = response.json()
    assert response.status_code == 200
    for user in data:
        address = user["address"]
        assert "street" in address
        assert "suite" in address
        assert "city" in address
        assert "zipcode" in address
        assert "geo" in address         

def test_get_all_users_geo_has_keys():
    response = get_all_users()
    data = response.json()

    assert response.status_code == 200

    for user in data:
        address = user["address"]
        geo = address["geo"]

        assert "lat" in geo
        assert "lng" in geo

def test_get_all_users_email_contains_at():
    response = get_all_users()
    data = response.json()
    assert response.status_code == 200    
    for user in data:
        email = user["email"]
        assert "@" in email
    
def test_get_all_users_username_not_empty():
    response = get_all_users()
    data = response.json()
    assert response.status_code == 200
    for user in data:
        username = user["username"]
        assert len(username) > 0

def test_get_all_users_id_is_integer():
    response = get_all_users()
    data = response.json()

    assert response.status_code == 200

    for user in data:
        user_id = user["id"]
        assert isinstance(user_id, int)
        
def test_get_all_users_company_has_keys():
    response = get_all_users()
    data = response.json()

    assert response.status_code == 200

    for user in data:
        company = user["company"]

        assert "name" in company
        assert "catchPhrase" in company
        assert "bs" in company

def test_get_all_users_company_name_not_empty():
    response = get_all_users()
    data = response.json()
    assert response.status_code == 200
    for user in data:
        company = user["company"]
        name = company["name"]
        assert len(name) > 0 