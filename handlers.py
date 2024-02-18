from aiogram import types, F, Router, Bot
from aiogram.types import ReplyKeyboardRemove, CallbackQuery, KeyboardButton, InlineKeyboardMarkup
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

router = Router()

@router.message(Command("start"))
async def start_handler(message: types.Message):
	await message.answer(f"Hello {message.from_user.full_name}")