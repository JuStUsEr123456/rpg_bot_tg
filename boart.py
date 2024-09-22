from dctatpin_of_bot import *
from aiogram.types import KeyboardButton, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from rpg import *


def kb_rows(names):
    start_old = ReplyKeyboardBuilder()
    for x in names:
        start_old.button(text=x)
    return start_old.adjust(3).as_markup(resize_keyboard=True)
