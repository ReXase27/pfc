from dataclasses import dataclass


@dataclass(frozen=False, repr=True, eq=True, order=False)
class User:
    username: str
    password: str

    def change_name(self, new_name: str) -> None:
        self.username = new_name

    def change_password(self, new_password: str) -> None:
        self.password = new_password