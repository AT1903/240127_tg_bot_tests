from aiogram.types import InlineKeyboardButton  # , InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
# -----------------------------
from lexicon import lexicon
# from database import database
# import services.test as test


def key_answer_creator(num: int) -> InlineKeyboardBuilder:

    buttons = InlineKeyboardBuilder()
    for n in range(1, num):
        buttons.add(InlineKeyboardButton(text=f'{lexicon.ru["answers"]}{n}', callback_data=f'clb_answer{n}'))

    return buttons.as_markup()
