from aiogram.dispatcher.filters.builtin import CommandStart, CommandHelp
from keyboards.keyboards import create_main_menu_keyboard
from states.states import StateGroup
from data.texts import texts
from aiogram import types
from loader import dp


@dp.message_handler(CommandHelp(), state="*")
async def run_main_menu(message: types.Message):
    await StateGroup.in_main_menu.set()
    await message.answer(f"Привет, {message.chat.full_name}!\n{texts.get('greetings')}",
                         reply_markup=create_main_menu_keyboard())


