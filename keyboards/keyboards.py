

from aiogram.utils.callback_data import CallbackData, CallbackDataFilter
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from utils.calendar_example import InlineCalendar
from enum import Enum, auto
from typing import List


class Actions(Enum):
    GO_BACK = auto()
    ADDRESS = auto()


# LISTS WITH TEXT DATA
list_with_addresses: List[str] = ["Розыбакиева, 111", "Желтоксан, 118"]

# CALLBACK FACTORY
CALLBACK_DATA_PREFIX = 'callbacks'
BASE_CALLBACK = CallbackData(CALLBACK_DATA_PREFIX, 'action', 'data')
# CALLBACK_CHOOSE_ADDRESS = BASE_CALLBACK.new(action=Actions.ADDRESS.name, data='-')
CALLBACK_GO_BACK = BASE_CALLBACK.new(action=Actions.GO_BACK.name, data='BACK')


# KEYBOARDS
def create_choose_address_keyboard():
    keyboard = InlineKeyboardMarkup(row_width=1).add(
        InlineKeyboardButton(text=f"{list_with_addresses[0]}", callback_data=list_with_addresses[0]),
        InlineKeyboardButton(text=f"{list_with_addresses[1]}", callback_data=list_with_addresses[1]),
        InlineKeyboardButton(text='Назад', callback_data=CALLBACK_GO_BACK)
    )
    return keyboard


def create_choose_date_keyboard():
    keyboard = InlineKeyboardMarkup(row_width=1).add(
        InlineKeyboardButton(text=f"{list_with_addresses[0]}", callback_data="0"),
        InlineKeyboardButton(text=f"{list_with_addresses[1]}", callback_data="list_with_addresses[1]"),
        InlineKeyboardButton(text='Назад', callback_data=CALLBACK_GO_BACK)
    )
    return keyboard


def create_choose_time_keyboard():
    pass

