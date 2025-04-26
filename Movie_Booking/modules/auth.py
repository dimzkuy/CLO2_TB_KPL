import json
import hashlib
import os

USERS_FILE = 'data/users.json'

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

def register(username, password):
    users = load_users()
    if any(user['username'] == username for user in users):
        raise Exception("Username sudah digunakan.")
    users.append({
        'username': username,
        'password': hash_password(password)
    })
    save_users(users)

def login(username, password):
    users = load_users()
    hashed = hash_password(password)
    return any(user['username'] == username and user['password'] == hashed for user in users)
