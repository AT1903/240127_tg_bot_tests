from aiogram import Router
from aiogram.types import Message
from lexicon import lexicon

ro: Router = Router()


@ro.message()
async def other_mess(mess: Message):
    await mess.answer(lexicon.ru['other'])
