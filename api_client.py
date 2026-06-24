import requests
from config import BASE_URL, USERS_ENDPOINT, POSTS_ENDPOINT

def get_user(user_id):
    return requests.get(f"{BASE_URL}{USERS_ENDPOINT}/{user_id}", timeout=10)

def get_post(post_id):
    return requests.get(f"{BASE_URL}{POSTS_ENDPOINT}/{post_id}", timeout=10)

def create_post(payload):
    return requests.post(f"{BASE_URL}{POSTS_ENDPOINT}", timeout=10, json=payload)

def update_post(post_id, payload):
    return requests.put(f"{BASE_URL}{POSTS_ENDPOINT}/{post_id}", json=payload)

def patch_post(post_id, payload):
    return requests.patch(f"{BASE_URL}{POSTS_ENDPOINT}/{post_id}", json=payload)

def delete_post(post_id):
    return requests.delete(f"{BASE_URL}{POSTS_ENDPOINT}/{post_id}")