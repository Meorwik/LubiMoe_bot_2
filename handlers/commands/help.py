from aiogram.dispatcher.filters.builtin import CommandHelp, CommandStart
from aiogram import types
from loader import dp


@dp.message_handler(CommandStart(), state="*")
async def bot_help(message: types.Message):
    text = ("Команды: ",
            "/start - Запустить бота",
            "/help - Показать все команды")
    
    await message.answer("\n".join(text))