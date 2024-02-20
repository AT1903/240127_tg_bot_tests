from aiogram.types import InlineKeyboardButton
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def create_ikb(width: int, **kwargs: str) -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()
    my_buttons = []

    for b, clb in kwargs.items():
        my_buttons.append(InlineKeyboardButton(text=b, callback_data=clb))

    kb_builder.row(*my_buttons, width=width)
    return kb_builder.as_markup()
