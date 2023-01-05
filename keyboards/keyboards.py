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
        self.const_times = []
        self.times_to_add = []
        self.possible_pages = 0
        self.page: int = 1

    def __create_not_today_time_list_(self):
        self.times_to_add, self.const_times = list_with_time, list_with_time
        self.possible_pages = len(self.times_to_add) // 2
        return True

    def __create_today_time_list_(self):
        current_time = datetime.datetime.now().strftime("%H")
        print(current_time)
        for time in list_with_time:
            if current_time in time[2:4]:
                self.times_to_add = list_with_time[list_with_time.index(time) + 1:]
                self.possible_pages = len(self.times_to_add) // 2
                self.const_times = self.times_to_add
                return True
        return False

    def __full_or_closed(self):
        if len(self.times_to_add) == 0 and current_time[0] == "0":
            return False
        else:
            self.times_to_add = list_with_time
            self.possible_pages = len(self.times_to_add) // 2
            self.const_times = self.times_to_add
            return True

    def __create_bottom_buttons(self, is_open: bool):
        if is_open and self.possible_pages > 1:
            self.keyboard.add(InlineKeyboardButton(text="Написать своё время", callback_data="own_time"))
            return self.keyboard.row(
                InlineKeyboardButton(text="<<<", callback_data="<<<"),
                InlineKeyboardButton("Назад", callback_data=CALLBACK_GO_BACK),
                InlineKeyboardButton(text=">>>", callback_data=">>>"))

        elif is_open and self.possible_pages == 1:
            self.keyboard.add(InlineKeyboardButton(text="Написать своё время", callback_data="own_time"))
            return self.create_back_button()
        else:
            return self.create_back_button()

    def create_back_button(self):
        return self.keyboard.add(InlineKeyboardButton("Назад", callback_data=CALLBACK_GO_BACK))

    def go_page_down(self):
        self.page -= 1
        self.create_time_select_keyboard("down")
        return self.keyboard

    def go_page_upper(self):
        self.page += 1
        self.create_time_select_keyboard("up")
        return self.keyboard

    def create_time_list_for_keyboard(self, date):
        if date != str(datetime.datetime.now().date()):
            return self.__create_not_today_time_list_()
        else:
            if self.__create_today_time_list_():
                return True
            else:
                return self.__full_or_closed()

    def create_time_select_keyboard(self, sep):
        self.keyboard = InlineKeyboardMarkup(row_width=1)
        temp_times_to_add = self.times_to_add
        cut_list = []
        if sep == "up":
            if self.page > self.possible_pages:
                self.page = 1
                self.keyboard.add(*[InlineKeyboardButton(text=i, callback_data=i) for i in temp_times_to_add[:2]])
                cut_list = [temp_times_to_add[:2]]
                print(cut_list, self.times_to_add)
                temp_times_to_add = temp_times_to_add[2:]
            else:
                cut_list = [temp_times_to_add[:2]]
                self.keyboard.add(*[InlineKeyboardButton(text=i, callback_data=i) for i in temp_times_to_add[:2]])
                temp_times_to_add = temp_times_to_add[2:]

    # TODO: FINISH "<<<" BUTTON
        elif sep == "down":
            if self.page < 1:
                if cut_list:
                    self.keyboard.add(*[InlineKeyboardButton(text=i, callback_data=i) for i in cut_list])
                    self.page = self.possible_pages
            else:
                self.keyboard.add(*[InlineKeyboardButton(text=i, callback_data=i) for i in cut_list])
                print(self.times_to_add + cut_list)
                pass

        self.times_to_add = temp_times_to_add
        if len(self.times_to_add) == 0:
            self.times_to_add = self.const_times

        self.__create_bottom_buttons(True)
        return self.keyboard
