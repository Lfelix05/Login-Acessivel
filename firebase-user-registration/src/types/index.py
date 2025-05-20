from typing import TypedDict

class UserData(TypedDict):
    email: str
    password: str
    accessibility: list[str]