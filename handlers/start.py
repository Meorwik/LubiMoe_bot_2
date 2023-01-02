from keyboards.keyboards import create_choose_address_keyboard
from aiogram.dispatcher.filters.builtin import CommandStart
from data.texts import texts
from aiogram import types
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}!\n{texts.get('addresses')}",
                         reply_markup=create_choose_address_keyboard())
