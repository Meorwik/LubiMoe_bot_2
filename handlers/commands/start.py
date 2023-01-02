from keyboards.keyboards import create_choose_address_keyboard
from aiogram.dispatcher.filters.builtin import CommandStart
from utils.users_requests import Request
from states.states import StateGroup
from data.texts import texts
from aiogram import types
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    user_request = Request()
    user_request.chat_id = message.from_user.id
    user_request.username = message.from_user.username
    user_request.first_name = message.from_user.first_name
    user_request.last_name = message.from_user.last_name
    await message.answer(f"Привет, {message.from_user.full_name}!\n{texts.get('addresses')}",
                         reply_markup=create_choose_address_keyboard())
    await StateGroup.in_choosing_address.set()
