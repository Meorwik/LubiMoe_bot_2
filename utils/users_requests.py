from dataclasses import dataclass
from json import dumps, loads


@dataclass
class Request:
    chat_id: int = None
    username: str = None
    first_name: str = None
    last_name: str = None
    address: str = None
    date: str = None
    time: str = None
    persons_name: str = None
    countOfGuests: int = None
    phoneNumber: int = None

    def to_dict(self):
        return loads(dumps(self, default=lambda o: o.__dict__, indent=4, ensure_ascii=False))
