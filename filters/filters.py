from aiogram.filters import BaseFilter
from aiogram.types import CallbackQuery


# фильтр кнопка - продолжить тест
class filter_m1_new_test (BaseFilter):
    async def __call__(self, clb: CallbackQuery) -> bool:
        if 'm1_start_new_test' in clb.data:
            return True


# фильтр кнопка - выбрать сохраненный тест
class filter_continue_test_button (BaseFilter):
    async def __call__(self, clb: CallbackQuery) -> str:
        if 'continue_test_button' in clb.data:
            return {'clb_data': clb.data}


# фильтр кнопка - продолжить тест
class filter_continue_test (BaseFilter):
    async def __call__(self, clb: CallbackQuery) -> bool:
        if 'continue_test' in clb.data:
            return True


# фильтр какой либо ответ
class filter_clb_answer (BaseFilter):
    async def __call__(self, clb: CallbackQuery) -> bool:
        if 'clb_answer' in clb.data:
            return True


# # фильтр кнопок с закладками
# class filter_bm (BaseFilter):
#     async def __call__(self, clb: CallbackQuery) -> bool:
#         if 'bm_go' in clb.data:
#             return True


# # фильтр кнопок с командой удалить закладки
# class filter_bm_del (BaseFilter):
#     async def __call__(self, clb: CallbackQuery) -> bool:
#         if 'bm_del' in clb.data:
#             return True
