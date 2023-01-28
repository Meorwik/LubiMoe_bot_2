from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from data.texts import texts
from math import ceil
import datetime

# LISTS WITH TEXT DATA
main_menu_button_callbacks = ["Book_", "KitchenAndBar_", "Reviews_", "ContactsAndAddresses_"]
list_with_addresses = ["Розыбакиева, 111", "Желтоксан, 118"]
CALLBACK_GO_BACK = "BACK"


# SIMPLE KEYBOARDS
def create_main_menu_keyboard():
    keyboard = InlineKeyboardMarkup(row_width=1).add(
        InlineKeyboardButton("Забронировать 🔐", callback_data=main_menu_button_callbacks[0]),
        InlineKeyboardButton("Меню 📕", callback_data=main_menu_button_callbacks[1]),
        InlineKeyboardButton("Отзывы 📈", callback_data=main_menu_button_callbacks[2]),
        InlineKeyboardButton("Контакты и адреса 👤", callback_data=main_menu_button_callbacks[3])
    )
    return keyboard


def create_choose_address_keyboard():
    keyboard = InlineKeyboardMarkup(row_width=1).add(
        InlineKeyboardButton(text=list_with_addresses[0], callback_data=list_with_addresses[0]),
        InlineKeyboardButton(text=list_with_addresses[1], callback_data=list_with_addresses[1]),
        InlineKeyboardButton(text='Назад', callback_data=CALLBACK_GO_BACK)
    )
    return keyboard


