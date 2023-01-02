

from keyboards.keyboards import list_with_addresses, create_choose_date_keyboard
from aiogram.dispatcher import FSMContext
from utils.users_requests import Request
from states.states import StateGroup
from data.texts import texts
from loader import dp, bot
from aiogram import types


@dp.callback_query_handler(state=StateGroup.in_choosing_address)
async def respond_on_address_callbacks(call: types.CallbackQuery, state: FSMContext, user_request_object: Request):
    if call.data in list_with_addresses:

        user_request_object.address = call.data
        await call.answer(f"Вы выбрали: {call.data}")
        await bot.send_message(chat_id=call.from_user.id, text=texts.get("date"),
                               reply_markup=create_choose_date_keyboard())
        await state.set_state(StateGroup.in_choosing_date)
    else:
        await state.set_state(StateGroup.in_main_menu)


@dp.callback_query_handler(state=StateGroup.in_choosing_date)
async def respond_on_date_callbacks(call: types.CallbackQuery, state: FSMContext):
    if call.data == "0":
        print(1)
