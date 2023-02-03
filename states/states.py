from aiogram.dispatcher.filters.state import State, StatesGroup


class StateGroup(StatesGroup):
    in_main_menu = State()
    in_choosing_address = State()
    in_choosing_date = State()
    in_choosing_time = State()
    in_choosing_room = State()
    in_filling_persons_request = State()

