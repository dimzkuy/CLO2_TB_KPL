# modules/utils.py
import json
import hashlib
import os
from typing import TypeVar, Generic, List, Optional

T = TypeVar('T')  # T adalah tipe generik

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def load_json(filepath: str) -> Optional[T]:
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r') as f:
        try:
            return json.load(f)  # type: ignore
        except json.JSONDecodeError:
            return None

def save_json(filepath: str, data: T) -> None:
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=4)
