from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from data.texts import texts
import datetime

# LISTS WITH TEXT DATA
main_menu_button_callbacks = ["Book_", "KitchenAndBar_", "Reviews_", "ContactsAndAddresses_"]
list_with_addresses = ["Розыбакиева, 111", "Желтоксан, 118"]
list_with_time = texts.get("times")
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


def create_temp_date_keyboard():
    keyboard = InlineKeyboardMarkup(row_width=1).add(
        InlineKeyboardButton(text="Today", callback_data=str(datetime.date.today())),
        InlineKeyboardButton(text="Today", callback_data=str(datetime.date.today())),
        InlineKeyboardButton(text='Назад', callback_data=CALLBACK_GO_BACK)
    )
    return keyboard


# COMPLEX KEYBOARDS
class TimeKeyboard:
    def __init__(self):
        self.keyboard = InlineKeyboardMarkup(row_width=1)
        self.times_to_add = []
        self.page: int = 1

    def go_page_down(self):
        self.page -= 1

    def go_page_upper(self):
        self.page += 1

    def create_time_list_for_keyboard(self):
        current_time = datetime.datetime.now().strftime("%H")
        current_time = "20"
        for time in list_with_time:
            if current_time in time[2:4]:
                self.times_to_add = list_with_time[list_with_time.index(time) + 1:]

    def create_time_select_keyboard(self):
        self.keyboard = InlineKeyboardMarkup(row_width=1)
        if len(self.times_to_add) <= 2:
            self.keyboard.add(*[InlineKeyboardButton(text=i, callback_data=i) for i in self.times_to_add])
            if self.page > 1:
                self.keyboard.add(InlineKeyboardButton(text="<<<", callback_data="<<<"))
        else:
            self.keyboard.add(*[InlineKeyboardButton(text=i, callback_data=i) for i in self.times_to_add[:2]])
            self.keyboard.add(InlineKeyboardButton(text=">>>", callback_data=">>>"))

            if self.page > 1:
                self.keyboard.add(InlineKeyboardButton(text="<<<", callback_data="<<<"))

            self.times_to_add = [time for time in self.times_to_add[2:]]

        self.keyboard.add(InlineKeyboardButton("Назад", callback_data=CALLBACK_GO_BACK))
        return self.keyboard
