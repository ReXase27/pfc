from __future__ import annotations
import logging
from colorama import Back
import colorama

from actions import exec_action, exec_user_action, get_action, get_user_action
import shared


def main() -> int:
    colorama.init(autoreset=True)
    logging.basicConfig(level=logging.INFO)

    while True:
        if shared.logged_user is None:
            user_input = input(
                f"{Back.CYAN}Would you like to login or register? (l/r){Back.RESET}\n"
            )
            try:
                exec_action(get_action(user_input))
            except ValueError as e:
                logging.error(e)

        else:
            print(f"{Back.CYAN}[SYSTEM]: Type 'help' or '?' for a list of commands\n")
            user_input = input(
                f"[{shared.logged_user.username}] >>\t" # noqa
            )  
            try:
                exec_user_action(get_user_action(user_input), shared.logged_user)
            except ValueError as e:
                logging.error(e)


if __name__ == "__main__":
    raise SystemExit(main())
