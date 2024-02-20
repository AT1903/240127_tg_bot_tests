from aiogram import Bot
from aiogram.types import BotCommand
from lexicon import lexicon


async def set_menu(bot: Bot):
    my_menu = [BotCommand(command=comm, description=descp) for comm, descp in lexicon.ru['menu_commands'].items()]
    await bot.set_my_commands(my_menu)
