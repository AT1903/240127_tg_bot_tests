from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
# -----------------------------
from lexicon import lexicon
from database import db

my_i_butt: InlineKeyboardButton = InlineKeyboardButton(text='Тест кнопки', callback_data='my_i_butt')
i_key: InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard=[[my_i_butt]])


def key_page_creator(num_page: int) -> InlineKeyboardMarkup:
    button_left: InlineKeyboardButton = InlineKeyboardButton(
        text=lexicon.ru['button_left'],
        callback_data='button_left')

    button_right: InlineKeyboardButton = InlineKeyboardButton(
        text=lexicon.ru['button_right'],
        callback_data='button_right')

    button_page: InlineKeyboardButton = InlineKeyboardButton(
        text=str(f'{num_page}/{len(db.book)}'),
        callback_data='button_page')

    return InlineKeyboardMarkup(inline_keyboard=[[button_left, button_page, button_right]])


def key_bm_creator() -> InlineKeyboardBuilder:
    buttons = InlineKeyboardBuilder()
    button_back_read = InlineKeyboardButton(text=lexicon.ru['button_back_read'], callback_data='button_back_read')
    button_edit = InlineKeyboardButton(text=lexicon.ru['button_edit'], callback_data='button_edit')

    for bm in db.user_db['bookmarks']:
        buttons.row(InlineKeyboardButton(text=f'{bm} - {db.book[bm][:100]}', callback_data=f'bm_go{bm}'))
    buttons.row(button_back_read, button_edit)
    return buttons


def key_bm_delet_creator() -> InlineKeyboardBuilder:
    buttons = InlineKeyboardBuilder()
    button_back_bm = InlineKeyboardButton(text=lexicon.ru['button_back_bm'], callback_data='button_back_bm')
    for bm in db.user_db['bookmarks']:
        buttons.row(InlineKeyboardButton(text=f'Х - {bm} - {db.book[bm][:100]}', callback_data=f'bm_del{bm}'))
    buttons.row(button_back_bm)
    return buttons
