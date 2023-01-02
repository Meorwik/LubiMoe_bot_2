from dataclasses import dataclass
from json import dumps


@dataclass
class Request:
    # date and time must be DATE TIME object
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

    def to_json(self):
        return dumps(self, default=lambda o: o.__dict__, indent=4, ensure_ascii=False)
