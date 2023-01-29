from keyboards.simple_keyboards.simple_keyboards import create_choose_address_keyboard, list_with_addresses
from keyboards.complex_keyboards.calendar_keyboard import DateKeyboard, calendar_callback
from keyboards.complex_keyboards.time_select_keyboard import TimeKeyboard
from handlers.commands.start import run_main_menu
from utils.db_api.db_api import DataBaseManager
from aiogram.dispatcher import FSMContext
from utils.users_requests import Request
from states.states import StateGroup
from datetime import datetime
from data.texts import texts
from aiogram import types
from loader import dp, bot


@dp.callback_query_handler(state=StateGroup.in_main_menu)
async def handle_main_menu(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    if call.data == "Book_":

        user_request = Request()
        user_request.chat_id = call.from_user.id
        user_request.username = call.from_user.username
        user_request.first_name = call.from_user.first_name
        user_request.last_name = call.from_user.last_name

        async with state.proxy() as data: data["request"] = user_request
        await call.message.answer(text=texts.get("addresses"), reply_markup=create_choose_address_keyboard())
        await StateGroup.in_choosing_address.set()


@dp.callback_query_handler(state=StateGroup.in_choosing_address)
async def handle_addresses_callbacks(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    if call.data in list_with_addresses:

        async with state.proxy() as data: data["request"].address = call.data
        await call.message.answer(text=texts.get("date"), reply_markup=await DateKeyboard().start_calendar())
        await call.answer(text=f"Вы выбрали: {call.data}")
        await state.set_state(StateGroup.in_choosing_date)

    elif call.data == "BACK":
        await run_main_menu(call.message)


@dp.callback_query_handler(calendar_callback.filter(), state=StateGroup.in_choosing_date)
async def handle_date_callbacks(call: types.CallbackQuery, state: FSMContext, callback_data: dict):
    selected, date = await DateKeyboard().process_selection(call, callback_data)

    if selected:
        await call.message.delete()
        time_choosing_keyboard = TimeKeyboard()
        if time_choosing_keyboard.create_time_buttons(call.data):
            await call.message.answer(text=f"{texts.get('time_select')}",
                                      reply_markup=time_choosing_keyboard.start_keyboard())
        else:
            await call.message.answer(text=f"{texts.get('closed')}",
                                      reply_markup=time_choosing_keyboard.start_keyboard())

        async with state.proxy() as data:
            data["request"].date = str(datetime.strptime(call.data[20:], '%Y:%m:%d').date())
            data["keyboard"] = time_choosing_keyboard
        await state.set_state(StateGroup.in_choosing_time)

    elif "BACK" in call.data:
        await call.message.delete()
        await call.message.answer(text=texts.get("addresses"), reply_markup=create_choose_address_keyboard())
        await StateGroup.in_choosing_address.set()


@dp.callback_query_handler(state=StateGroup.in_choosing_time)
async def handle_time_callbacks(call: types.CallbackQuery, state: FSMContext):
    if call.data in texts.get("times"):
        await call.message.delete()

        data_base_manager = DataBaseManager()
        await data_base_manager.connect()

        async with state.proxy() as data:
            data["request"].time = call.data
            await data_base_manager.add_new_info(
                table_name="requests",
                info=[i for i in data["request"].to_dict().values()])

        await data_base_manager.disconnect()
        del data_base_manager

    elif call.data == ">>>":
        async with state.proxy() as data:
            time_choosing_keyboard = data['keyboard']
            await call.message.edit_reply_markup(reply_markup=time_choosing_keyboard.go_upper())

    elif call.data == "<<<":
        async with state.proxy() as data:
            time_choosing_keyboard = data['keyboard']
            await call.message.edit_reply_markup(reply_markup=time_choosing_keyboard.go_down())

    elif call.data == "own_time":
        pass

    else:
        await call.message.delete()
        await call.message.answer(text=texts.get("date"), reply_markup=await DateKeyboard().start_calendar())
        await state.set_state(StateGroup.in_choosing_date)
