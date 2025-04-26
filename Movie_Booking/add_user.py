import json
import hashlib
import os

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

def add_user():
    username = input("Masukkan username baru: ").strip()
    password = input("Masukkan password: ").strip()

    users = load_users()

    if any(u['username'] == username for u in users):
        print(f"❌ Username '{username}' sudah ada.")
        return

    hashed_pw = hash_password(password)
    users.append({
        'username': username,
        'password': hashed_pw
    })

    save_users(users)
    print(f"✅ User '{username}' berhasil ditambahkan!")

if __name__ == '__main__':
    add_user()
