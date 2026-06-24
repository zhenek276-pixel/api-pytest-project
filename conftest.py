import pytest
from api_client import get_user, get_post


@pytest.fixture
def user_data():
    response = get_user(1)
    return response.json()


@pytest.fixture
def post_data():
    response = get_post(1)
    return response.json()


@pytest.fixture
def post_response():
    response = get_post(1)
    return response
