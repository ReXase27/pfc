import os
import random
import sys
from typing import Dict, Optional, Sequence, Set

import colorama
from colorama import Back, Fore

VALID_INPUTS: Dict[str, str] = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper",
    "r": "scissors",
    "p": "rock",
    "s": "paper",
}

EMOJI_MAP: Dict[str, str] = {
    "rock": "🪨",
    "paper": "📄",
    "scissors": "✂️",
    "r": "🪨",
    "p": "📄",
    "s": "✂️",
}

QUIT_WORDS: Set[str] = {"quit", "q", "exit", "end"}


def main(argv: Sequence[str] | None = None) -> int:

    colorama.init(autoreset=True)

    print(Back.BLUE + "Welcome to Rock, Paper, Scissors!")

    machine_guess: Optional[str] = None

    # game loop
    while True:
        user_input: str = input(">> ")
        while user_input not in QUIT_WORDS:
            if user_input not in VALID_INPUTS:
                print(Back.YELLOW + "Invalid input. Please try again.")
                break

            # game logic
            os.system("clear")
            print(f"[YOU]: {EMOJI_MAP[user_input]}")
            machine_guess = random.choices(list(VALID_INPUTS.keys()))[0]
            print(f"[OPPONENT]: {EMOJI_MAP[machine_guess]}")
            if VALID_INPUTS[user_input.lower()] == machine_guess:
                print(Fore.GREEN + "You win!")
                break

            elif VALID_INPUTS[machine_guess.lower()] == user_input:
                print(Fore.RED + "You lose!")
                break

            elif user_input == machine_guess:
                print(Fore.YELLOW + "Tie!")
                break
        else:
            print(Back.CYAN + "Thanks for playing!")
            sys.exit(0)


if __name__ == "__main__":
    raise SystemExit(main())
