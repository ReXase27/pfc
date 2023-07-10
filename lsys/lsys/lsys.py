from __future__ import annotations
from colorama import Back
import colorama

from actions import exec_action, exec_user_action, get_action, get_user_action
import shared


def main() -> int:
    colorama.init(autoreset=True)

    while True:
        if shared.logged_user is None:
            user_input = input(
                f"{Back.CYAN}Would you like to login or register? (l/r){Back.RESET}\n"
            )
            try:
                exec_action(get_action(user_input))
            except ValueError as e:
                print(e)

        else:
            print(f"{Back.CYAN}[SYSTEM]:\tEnter 'help' or '?' for a list of commands\n")
            user_input = input(
                f"[{shared.logged_user.username}] >>\t" # noqa
            )  
            try:
                exec_user_action(get_user_action(user_input), shared.logged_user)
            except ValueError as e:
                print(e)


if __name__ == "__main__":
    raise SystemExit(main())
