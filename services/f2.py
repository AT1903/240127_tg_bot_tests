import json
from lexicon import lexicon
from keyboards import create_inline_keyb
import os
path_json_data = 'database/new_data_user.json'
path_base_tests = 'data_tests'


def json_to_dict(path_json: str) -> dict:
    # Возвращает словарь из JSON по заданному пути
    with open(path_json, 'r', encoding="utf-8") as f:
        d = json.load(f)
    return d


def fun_start_comm():
    # сформировать сообщение   # приветствие    # активные тесты
    out_text = lexicon.ru['start_text']
    # сформировать клавиатуру    # продолжить активные тесты    # выбрать новый тест
    out_key = create_inline_keyb.create_ikb(1, **lexicon.ru['start_keyb'])
    return (out_text, out_key)


def fun_m1_new_test():
    # поиск все каталогов в базе данных
    dict_for_kyeb = {}
    i = 0
    for dir in sorted(os.listdir(path_base_tests)):
        print(dir)
        dict_for_kyeb[dir] = f'button_newtest_{i}'
        i = i + 1

    out_text = lexicon.ru['m1_new_test']
    out_key = create_inline_keyb.create_ikb(1, **dict_for_kyeb)
    return (out_text, out_key)


def fun_m1_continue_test():
    ud = json_to_dict(path_json_data)
    # сообщение - сохраненные тесты
    out_text = lexicon.ru['continue_test_text']
    # клавиатура - названия всех сохраненых
    key1 = {}
    for i in ud['my_tests']:
        key1[ud['my_tests'][i]['name']] = f'continue_test_button_{i}'
        # итоговый вид : key1 = {'А1' : 'continue_test_button_1'} - название теста и callbackdata для обработки нажатия
    # добавляем в клавиатуру кнопку из лексикона
    key1.update(lexicon.ru['continue_test_keyb'])
    out_key = create_inline_keyb.create_ikb(1, **key1)
    return (out_text, out_key)


def fun_m2_continue_test_button(clb: str):
    ud = json_to_dict(path_json_data)
    num_test = clb.split('_')[-1]
    out_text = f'Тест - {ud["my_tests"][num_test]["name"]}\n'
    test_mode = ud["my_tests"][num_test]["test_mode"]
    out_text += f'Режим тестирования: {lexicon.ru["test_mode"][test_mode]}\n'
    out_text += f'Всего билетов: {len(ud["my_tests"][num_test]["tickets"])}\n'
    out_text += f'Вопросов в одном билете: {len(ud["my_tests"][num_test]["tickets"]["1"]["questions"])}\n'

    out_key = create_inline_keyb.create_ikb(1, **{'тестовая кнопка': 'button'})

    return (out_text, out_key)


def select_new_test():
    # сообщение - сохраненные тесты
    # клавиатура - названия всех доступных
    pass


# print(continue_test(), sep='\n')
