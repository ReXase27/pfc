from typing import Dict

from user import User


USER_STORE: Dict[int, User] = {}
next_id: int = 0


def register_user(username: str, password: str) -> None:
    if username in USER_STORE:
        raise ValueError("User already exists")

    global next_id

    USER_STORE[next_id] = User(username, password)
    next_id += 1


def login_user(username: str, password: str) -> User:
    for user in USER_STORE.values():
        if user.username == username and user.password == password:
            return user

    raise ValueError("Invalid username or password")