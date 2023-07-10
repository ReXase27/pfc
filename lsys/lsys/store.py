from typing import Optional, Sequence

from user import User


USER_STORE: Sequence[User] = []


def register_user(username: str, password: str) -> None:
    """
    Register a new user with the given username and password.

    Raises:
        ValueError: If a user with the given username already exists.
    """
    if username in USER_STORE:
        raise ValueError("User already exists")

    USER_STORE.append(User(username, password))


def login_user(username: str, password: str) -> Optional[User]:
    """
    Attempt to log in a user with the given username and password.

    Returns:
        The User object if the login is successful, 
        or None if the username or password is incorrect.
    """
    for user in USER_STORE:
        if user.username == username and user.password == password:
            return user

    return None