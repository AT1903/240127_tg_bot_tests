from aiogram import Router
from aiogram.types import Message
from aiogram.types import CallbackQuery
from aiogram.filters import Command
# from aiogram import F
# -----------------------------
from services import f2
from services import services_test_fun
from keyboards import inline_key_tests
from filters import filters
from database import db
# from lexicon import lexicon


path_json_test = 'tests/A1_out.json'
path_text_test = 'tests/A1_out.txt'


ro: Router = Router()

quest = 1


# Команда <<Старт>>
@ro.message(Command(commands=['start']))
async def proc_comm_start(mess: Message):

    out_tex, out_key = f2.fun_start_comm()
    await mess.answer(
        text=out_tex,
        reply_markup=out_key)


# меню 2 уровень
# Обработка нажатия кнопки с названием теста который необходимо продолжить
@ro.callback_query(filters.filter_continue_test_button())
async def m1_button_continue_test(clb: CallbackQuery, clb_data: str):
    out_tex, out_key = f2.fun_m2_continue_test_button(clb_data)
    await clb.message.edit_text(
        text=out_tex,
        reply_markup=out_key)


# меню 1 уровень
# Обработка нажатия кнопки новый тест
@ro.callback_query(filters.filter_m1_new_test())
async def m1_new_test(clb: CallbackQuery):
    out_tex, out_key = f2.fun_m1_new_test()
    await clb.message.edit_text(
        text=out_tex,
        reply_markup=out_key)


# меню 1 уровень
# Обработка нажатия кнопки <<Продолжить тест>>
@ro.callback_query(filters.filter_continue_test())
async def m2_proc_continue_test(clb: CallbackQuery):
    out_tex, out_key = f2.fun_m1_continue_test()
    await clb.message.edit_text(
        text=out_tex,
        reply_markup=out_key)


# Выбор ответа
@ro.callback_query(filters.filter_clb_answer())
async def button_clb_answer(clb: CallbackQuery):

    db.user_db['current_question'] += 1
    # получаем класс с вопросом и количесвом кнопок
    mess_test = services_test_fun.get_text_question(db.questions, db.user_db['current_question'])

    # Записываем в память текущий впрос
    db.write_data(db.path_data_json)

    await clb.message.edit_text(
        text=mess_test.text_for_message,
        reply_markup=inline_key_tests.key_answer_creator(mess_test.num_buttons))


# Обработка нажатия кнопки Продолжить тест
# @ro.callback_query(filters.filter_continue_test())
# async def button_continue_test(clb: CallbackQuery):

#     db.user_db['current_question'] += 1
#     # получаем класс с вопросом и количесвом кнопок
#     mess_test = services_test_fun.get_text_question(db.questions, db.user_db['current_question'])

#     # Записываем в память текущий впрос
#     db.write_data(db.path_data_json)

#     await clb.message.edit_text(
#         text=mess_test.text_for_message,
#         reply_markup=inline_key_tests.key_answer_creator(mess_test.num_buttons))
# #
#         butt = {'Кнопка1': 'Clb1',
#             'Кнопка2': 'Clb1',
#             'Кноп3': 'Clb1'}
#     f2.start_comm()
    # # Записываем в словарь вопросы из json
    # db.questions = services_test_fun.questions_to_dict(path_json_test)

    # # Читаем из памяти актуальный вопрос и тест
    # db.user_db = db.read_data(db.path_data_json)

    # # получаем класс с вопросом и количесвом кнопок
    # mess_test = services_test_fun.get_text_question(db.questions, db.user_db['current_question'])

    # current_question = db.user_db['current_question']
    # questions_text = open_test.questions[current_question]
    # num_rows = len(open_test.questions[current_question])
    # questions_text.insert(1, '')
#
#
#
#
#
#
#
#
#
#
#
    # database.book = file_handling.prepare_book(file_handling.book_path)
    # await mess.answer(
    #     text=test.questions[quest][0],
    #     reply_markup=inline_key_tests.key_tests_creator(test.questions[quest]))

# # Кнопка вправо
# @ro.callback_query(F.data == 'button_right')
# async def button_right(cll: CallbackQuery):
#     database.user_db['page'] += 1
#     await cll.message.edit_text(
#         text=database.book[database.user_db['page']],
#         reply_markup=inline_keyboards.key_page_creator(database.user_db['page']))


# # Кнопка влево
# @ro.callback_query(F.data == 'button_left')
# async def button_left(cll: CallbackQuery):
#     database.user_db['page'] -= 1
#     await cll.message.edit_text(
#         text=database.book[database.user_db['page']],
#         reply_markup=inline_keyboards.key_page_creator(database.user_db['page']))


# # Добавить закладку
# @ro.callback_query(F.data == 'button_page')
# async def button_page(cll: CallbackQuery):
#     database.user_db['bookmarks'].add(database.user_db['page'])
#     await cll.answer(
#         text=lexicon.ru['button_page']
#         )


# # открыть закладки
# @ro.message(Command(commands=['bookmarks']))
# async def bookmarks_open(mess: Message):
#     await mess.answer(
#         text=lexicon.ru['bookmarks_open'],
#         reply_markup=inline_keyboards.key_bm_creator().as_markup())


# # Редактировать закладки
# @ro.callback_query(F.data == 'button_edit')
# async def bookmarks_edit(clb: CallbackQuery):
#     await clb.message.edit_text(
#         text=lexicon.ru['bookmarks_edit'],
#         reply_markup=inline_keyboards.key_bm_delet_creator().as_markup())


# # открыть закладку
# @ro.callback_query(filters.filter_bm())
# async def filter_bm_fun(clb: CallbackQuery):
#     database.user_db['page'] = int(clb.data[5:])
#     await clb.message.edit_text(
#         text=database.book[database.user_db['page']],
#         reply_markup=inline_keyboards.key_page_creator(database.user_db['page']))


# # удалить закладку
# @ro.callback_query(filters.filter_bm_del())
# async def filter_bm_del(clb: CallbackQuery):
#     database.user_db['bookmarks'].remove(int(clb.data[6:]))
#     await clb.message.edit_text(
#         text=lexicon.ru['bookmarks_edit'],
#         reply_markup=inline_keyboards.key_bm_delet_creator().as_markup())


# # вернуться к книге
# @ro.callback_query(F.data == 'button_back_read')
# async def button_back_read(clb: CallbackQuery):
#     await clb.message.edit_text(
#         text=database.book[database.user_db['page']],
#         reply_markup=inline_keyboards.key_page_creator(database.user_db['page']))


# # вернуться к закладкам
# @ro.callback_query(F.data == 'button_back_bm')
# async def button_back_bm(clb: CallbackQuery):
#     await clb.message.edit_text(
#         text=lexicon.ru['bookmarks_open'],
#         reply_markup=inline_keyboards.key_bm_creator().as_markup())
