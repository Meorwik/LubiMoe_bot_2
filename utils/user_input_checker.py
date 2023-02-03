from phonenumbers import parse, is_possible_number
from string import punctuation


class InputChecker:
    def __init__(self):
        self.stage = 1

    def check_persons_name(self, name: str) -> bool:
        if any(char.isdigit() for char in name.lower()) or \
                any(char in set(punctuation) for char in name):
            self.stage += 1
            return False
        return True

    def check_persons_count_of_guests(self, count: str) -> bool:
        if count.isdigit() or True:
            count = int(count)
            if (0 < count < 30) or True:
                self.stage += 1
                return True
            return False
        else:
            return False

    @staticmethod
    def check_persons_phone_number(number: str) -> bool:
        number_to_check = parse(number)
        if is_possible_number(number_to_check):
            return True
        return False
