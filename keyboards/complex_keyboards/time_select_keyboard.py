from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from datetime import datetime
from data.texts import texts
from math import ceil


list_with_time = texts.get("times")
CALLBACK_GO_BACK = "BACK"


class TimeKeyboard:
    def __init__(self):
        self.keyboard = InlineKeyboardMarkup(row_width=1)
        self.all_buttons_to_add = None
        self.times = list_with_time
        self.possible_pages = 0
        self.page_sep = 0
        self.on_page = 1

    @staticmethod
    def __init_time_list(date):
        if datetime.strptime(date[20:], '%Y:%m:%d').date() > datetime.now().date():
            return list_with_time

        elif datetime.strptime(date[20:], '%Y:%m:%d').date() == datetime.now().date():
            current_time = str(datetime.now().strftime("%H"))
            current_time_str = f"С {current_time}:00"
            if current_time_str in list_with_time:
                times = [time for time in list_with_time[list_with_time.index(current_time_str)+1:]]
                return times
            elif 8 <= int(current_time) < 17:
                return list_with_time
        else:
            return "closed"

    def __get_keyboard_sample(self, list_with_buttons):
        self.keyboard = InlineKeyboardMarkup(row_width=1).add(*list_with_buttons)
        return self.__create_bottom_buttons()

    def __create_time_buttons(self, date):
        times_to_show = self.__init_time_list(date=date)
        if times_to_show == "closed":
            self.all_buttons_to_add = [InlineKeyboardButton("Мы закрыты", callback_data="closed")]
            self.possible_pages = 1
            return False
        else:
            self.possible_pages = ceil(len(times_to_show) / 2)
            self.all_buttons_to_add = [InlineKeyboardButton(time, callback_data=time) for time in times_to_show]
            return True

    def __create_bottom_buttons(self):
        if self.possible_pages > 1:
            self.keyboard.add(InlineKeyboardButton("Написать своё время", callback_data="own_time"))
            return self.keyboard.row(
                InlineKeyboardButton("<<<", callback_data="<<<"),
                InlineKeyboardButton("Назад", callback_data=CALLBACK_GO_BACK),
                InlineKeyboardButton(">>>", callback_data=">>>"))

        elif self.possible_pages == 1 and len(self.all_buttons_to_add) > 1:
            self.keyboard.add(InlineKeyboardButton("Написать своё время", callback_data="own_time"))
            return self.keyboard.add(InlineKeyboardButton("Назад", callback_data=CALLBACK_GO_BACK))
        else:
            return self.keyboard.add(InlineKeyboardButton("Назад", callback_data=CALLBACK_GO_BACK))

    def start_keyboard(self, date):
        if self.__create_time_buttons(date=date):
            msg = "time_select"
        else:
            msg = 'closed'
        return msg, self.__get_keyboard_sample(self.all_buttons_to_add[:2])

    def go_upper(self):
        default_page_separator = 0
        page_go_upper_delimiter = 2

        if self.on_page + 1 <= self.possible_pages:
            self.page_sep += page_go_upper_delimiter
            self.on_page += 1
        else:
            self.page_sep = default_page_separator
            self.on_page = 1
        return self.__get_keyboard_sample(self.all_buttons_to_add[self.page_sep: self.page_sep + page_go_upper_delimiter])

    def go_down(self):
        default_page_separator = 0
        page_go_down_delimiter = 2
        max_sep = (self.possible_pages * 2) - 2

        if self.on_page > 1:
            self.page_sep -= page_go_down_delimiter
            self.on_page -= 1

        elif self.on_page <= 1 and self.page_sep <= default_page_separator:
            self.page_sep = max_sep
            self.on_page = self.possible_pages
        return self.__get_keyboard_sample(self.all_buttons_to_add[self.page_sep: self.page_sep + page_go_down_delimiter])

