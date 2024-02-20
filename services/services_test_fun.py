import json
from dataclasses import dataclass
path_json_test = 'tests/A1_out.json'
path_text_test = 'tests/A1_out.txt'


@dataclass
class class_questions_text:
    text_for_message: str = ''
    num_buttons: int = 0


def text_questions_to_json(path_input_txt: str, path_output_json: str):
    # 02.02.2024
    # Преобразуем текстовый вариант в формат json по заданному пути

    out: dict = {
        'properties': {},
        'questions': {}
        }
    num: int = 1
    print(out)

    with open(path_input_txt, 'r', encoding='utf-8') as f:
        q = f.readlines()
        list_q = []

    for row in q:
        if row == '\n':
            out['questions'][f'{num}'] = list_q
            # out['questions'][list_q[0]] = [list_q[1:]]
            num += 1
            list_q = []
        else:
            list_q.append(row.strip())

    with open(path_output_json, 'w', encoding='utf-8') as json_file:
        json.dump(out, json_file, ensure_ascii=False)


def get_question(path_json: str, number: int) -> list:
    # 02.02.2024
    # Возвращает список: [вопрос, ответ1, ответ2, ...] из JSON по заданному пути
    with open(path_json, 'r', encoding="utf-8") as f:
        d = json.load(f)
    if f'{number}' in d['questions']:
        return d['questions'][f'{number}']
    else:
        return ['final']


def questions_to_dict(path_json: str) -> dict:
    # 02.02.2024
    # Возвращает словарь: с вопросами из JSON по заданному пути
    with open(path_json, 'r', encoding="utf-8") as f:
        d = json.load(f)
    return d


def get_question_from_dict(d: str, number: int) -> list:
    # 02.02.2024
    # Возвращает список: [вопрос, ответ1, ответ2, ...] из словаря
    if f'{number}' in d['questions']:
        return d['questions'][f'{number}']
    else:
        return ['final']


def get_text_question(d: str, number: int) -> class_questions_text:
    # возвращает обект class_questions_text с текстом
    q = get_question_from_dict(d, number)
    # убираем знак +
    for i in range(1, len(q)):
        if q[i][-1] == '+':
            q[i] = q[i][:-1]

    out = class_questions_text()
    out.text_for_message = '\n\n'.join(i for i in q)
    out.num_buttons = len(q)
    # print(out.text_for_message)
    return out
def chit():


# quest = questions_to_dict(path_json_test)
# # get_text_question(d=quest, number=34)
# print(len(quest['questions']))
# res = {}
# for i in range(1, len(quest['questions']) + 1):
#     # print(f'Вопрос {i}')
#     for i in quest['questions'][f'{i}']:
#         for w in i.split():

#             if w not in res:
#                 res[w] = [0, 0]
# print(res)
    res = {}
    for i in range(1, len(quest['questions']) + 1):
        # print(f'Вопрос {i}')
        for r in range(1,len(quest['questions'][f'{i}'])):
            # print(quest['questions'][f'{i}'][r])
            # print(quest['questions'][f'{i}'][r][-1])
            if quest['questions'][f'{i}'][r][-1] == '+':
                for w in quest['questions'][f'{i}'][r][:-2].split():
                    if w in res:
                        res[w][0] += 1
                    else:
                        res[w] = [1, 0]
            else:
                for w in quest['questions'][f'{i}'][r][:-1].split():
                    if w in res:
                        res[w][1] += 1
                    else:
                        res[w] = [0, 1]

    for i in res:
        if res[i][1] == 0 and res[i][0] > 2:
            print(i, res[i])
    print('__________________________')
    for i in res:
        if res[i][0] > 0 and res[i][1] > 0 and res[i][1]/res[i][0] > 8:
            print(i, res[i])
        # print(res[i])

# for i in quest['questions']['1']:
#     for w in i.split():
#         if w not in res:
#             res[w] = 1

# print(res)
