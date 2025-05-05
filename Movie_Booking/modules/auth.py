import json
import hashlib
import os
from modules.utils import hash_password, load_json, save_json

USERS_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'users.json')

def load_users():
    if not os.path.exists(USERS_FILE):
        return []
    with open(USERS_FILE, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_users(users):
    with open(USERS_FILE, 'w') as f:
        json.dump(users, f, indent=4)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register(username: str, password: str):
    users = load_json(USERS_FILE) or []
    if any(user['username'] == username for user in users):
        raise Exception("Username sudah digunakan.")
    users.append({
        'username': username,
        'password': hash_password(password)
    })
    save_json(USERS_FILE, users)

def login(username, password):
    users = load_users()
    hashed = hash_password(password)
    return any(user['username'] == username and user['password'] == hashed for user in users)
