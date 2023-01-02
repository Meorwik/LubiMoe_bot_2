from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from utils.
from typing import List

addresses: List[str] = ["Розыбакиева, 111", "Желтоксан, 118"]


def create_choose_address_keyboard():
    keyboard = InlineKeyboardMarkup(row_width=1).add(
        InlineKeyboardButton(text=f"{addresses[0]}", callback_data=addresses[0]),
        InlineKeyboardButton(text=f"{addresses[1]}", callback_data=addresses[1]),
        InlineKeyboardButton(text='Назад', callback_data="back")
    )
    return keyboard


def create_choose_date_keyboard():
    pass


def create_choose_time_keyboard():
    pass

