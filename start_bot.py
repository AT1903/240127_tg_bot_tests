from aiogram import Dispatcher, Bot

# ===============
from config import bot_config
from handlers import other_handlers, commaand_handlers
from keyboards import menu


def start_bot():
    my_bot_conf = bot_config.set_bot_config()
    print(my_bot_conf.config.token)
    print(my_bot_conf.config.admins)

    my_bot: Bot = Bot(token=my_bot_conf.config.token)
    dp: Dispatcher = Dispatcher()
    dp.startup.register(menu.set_menu)
    dp.include_router(commaand_handlers.ro)
    dp.include_router(other_handlers.ro)
    dp.run_polling(my_bot)


if __name__ == ('__main__'):
    print('----START----')
    start_bot()
