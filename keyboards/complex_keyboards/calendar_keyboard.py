from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData
from calendar import month_name, monthcalendar
from datetime import datetime, timedelta
from aiogram.types import CallbackQuery


# setting callback_data prefix and parts
calendar_callback = CallbackData('simple_calendar', 'act', 'year', 'month', 'day')
week_days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]


class DateKeyboard:
    def __init__(self):
        self.inline_kb = InlineKeyboardMarkup(row_width=7)
        self.ignore_callback = None  # for buttons with no answer

    # First row - Month and Year
    async def __add_month_heading(self, month):
        self.inline_kb.row()
        self.inline_kb.insert(InlineKeyboardButton(
            text=f'{month_name[month]}',
            callback_data=self.ignore_callback))

    # Second row - Week Days
    async def __add_week_days(self):
        self.inline_kb.row(*[InlineKeyboardButton(day, callback_data=self.ignore_callback) for day in week_days])

    # Calendar rows - Days of month
    async def __add_days_of_month(self, year, month):
        month_calendar = monthcalendar(year, month)
        for week in month_calendar:
            self.inline_kb.row()
            for day in week:
                if day == 0:
                    self.inline_kb.insert(InlineKeyboardButton("-", callback_data=self.ignore_callback))
                    continue
                self.inline_kb.insert(InlineKeyboardButton(
                    text=str(day),
                    callback_data=calendar_callback.new("DAY", year, month, day)))

    # Last row - Buttons
    async def __add_bottom_buttons(self, year, month):

        prev_month_button = InlineKeyboardButton(text="<<<",
                                                 callback_data=calendar_callback.new("PREV-MONTH", year, month, 0))

        back_button = InlineKeyboardButton("Назад", callback_data=calendar_callback.new("BACK", year, month, 0))

        next_month_button = InlineKeyboardButton(text=">>>",
                                                 callback_data=calendar_callback.new("NEXT-MONTH", year, month, 0))

        self.inline_kb.row(prev_month_button, back_button, next_month_button)

    async def process_selection(self, query: CallbackQuery, data) -> tuple:
        return_data = (False, None)
        temp_date = datetime(int(data['year']), int(data['month']), 1)
        # processing empty buttons, answering with no action
        if data['act'] == "IGNORE":
            await query.answer(cache_time=60)
        # user picked a day button, return date
        if data['act'] == "DAY":
            await query.message.delete_reply_markup()   # removing inline keyboard
            return_data = True, datetime(int(data['year']), int(data['month']), int(data['day']))

        if data['act'] == "PREV-MONTH":
            prev_date = temp_date - timedelta(days=1)
            await query.message.edit_reply_markup(await self.start_calendar(int(prev_date.year), int(prev_date.month)))
        # user navigates to next month, editing message with new calendar
        if data['act'] == "NEXT-MONTH":
            next_date = temp_date + timedelta(days=31)
            await query.message.edit_reply_markup(await self.start_calendar(int(next_date.year), int(next_date.month)))
        # at some point user clicks DAY button, returning date
        return return_data

    async def start_calendar(self, year: int = datetime.now().year, month: int = datetime.now().month):
        self.ignore_callback = calendar_callback.new("IGNORE", year, month, 0)
        await self.__add_month_heading(month)
        await self.__add_week_days()
        await self.__add_days_of_month(year, month)
        await self.__add_bottom_buttons(year, month)

        return self.inline_kb
