from enum import Enum
import os
from time import sleep
from colorama import Fore

from store import login_user, register_user
from user import User
import shared


class Action(Enum):
    LOGIN = "l", "login"
    REGISTER = "r", "register"
    EXIT = "e", "exit", "end", "quit", "q"

def get_action(choice: str) -> Action:
    for action in Action:
        if choice in action.value:
            return action

    raise ValueError("Invalid action")

def exec_action(action: Action) -> None:
    match action:
            case Action.LOGIN:
                username = input(">> Username: ")
                password = input(">> Password: ")

                try:
                    shared.logged_user = login_user(username, password)

                    assert shared.logged_user is not None
                    print(Fore.GREEN + "Logged in!")
                    sleep(1)
                    os.system("clear")
                    
                except ValueError as e:
                    print(e)
                    
            case Action.REGISTER:
                username = input(">> Username: ")
                password = input(">> Password: ")
                try:
                    register_user(username, password)
                    print(Fore.GREEN + "Registered!")
                    sleep(1)
                    os.system("clear")

                except ValueError as e:
                    print(e)

            case Action.EXIT:
                print("Goodbye!")
                raise SystemExit(0)

            case _:
                print(Fore.RED + "Invalid option")
                os.system("clear")


class UserAction(Enum):
    CN = "cn", "change name"
    CP = "cp", "change password"
    PD = "pd", "print data"
    LOGOUT = "logout", "log out", "l", "lo"
    EXIT = "exit", "end", "quit", "q", "e"
    HELP = "help", "h", "?"

def get_user_action(choice: str) -> UserAction:
    for action in UserAction:
        if choice in action.value:
            return action

    raise ValueError("Invalid action")

def exec_user_action(action: UserAction, user: User) -> None:
    match action:
            case UserAction.CN:
                change_username(user)

            case UserAction.CP:
                change_password(user)

            case UserAction.PD:
                print_data(user)

            case UserAction.LOGOUT:
                logout()

            case UserAction.EXIT:
                print("Goodbye!")
                raise SystemExit(0)

            case UserAction.HELP:
                print_help()
                if input("[Press enter to continue]") == "":
                    os.system("clear")
                    

            case _:
                print(Fore.RED + "Invalid option")


def change_username(user: User) -> None:
    new_username = input(">> New username: ")
    user.change_name(new_username)

def change_password(user: User) -> None:
    new_password = input(">> New password: ")
    try_again = input(">> Confirm new password: ")

    if new_password == user.password:
        print(Fore.RED + "New password cannot be the same as old password")
        return

    if new_password != try_again:
        print(Fore.RED + "Passwords do not match")
        return
    
    user.change_password(new_password)

def print_data(user: User) -> None:
    print(f"Username: {user.username}")
    print(f"Password: {user.password}")

def logout() -> None:
    shared.logged_user = None

def print_help() -> None:
    help_menu = """
    cn, change name - Change your username
    cp, change password - Change your password
    pd, print data - Print your username and password
    logout, log out, l, lo - Log out of your account
    exit, end, quit, q, e - Exit the program
    help, h, ? - Print this help menu
    """

    print(help_menu)