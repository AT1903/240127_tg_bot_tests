def _get_part_text(in_text, start_pos, size):
    part_text: str = ''
    end_text = ',.!:;?'
    end_pos: int = 0
    max_pos = start_pos + size

    if max_pos >= len(in_text):
        end_pos = len(in_text)

    elif in_text[max_pos - 1] in end_text and max_pos >= len(in_text):
        end_pos = len(in_text)

    elif in_text[max_pos - 1] in end_text and in_text[max_pos] not in end_text:
        end_pos = max_pos
    else:
        check = False
        for i in range(size):
            if in_text[max_pos - 1 - i] not in end_text:
                check = True
            if in_text[max_pos - 1 - i] in end_text and check:
                end_pos = max_pos - i
                break

    part_text = in_text[start_pos:end_pos]  # .strip()

    return [part_text, len(part_text)]


book: dict[int, str] = {}
PAGE_SIZE = 1000

book_path = "Blejd.txt"
# my_dict = {}


def prepare_book(path: str) -> dict:
    my_file = open(path, 'r', encoding="utf-8")
    my_book = my_file.read()
    my_file.close()
    my_dict = {}
    start_p = 0
    num_page = 1
    next_sym = 0
    while start_p < len(my_book):
        new_part = _get_part_text(my_book, start_p, PAGE_SIZE)
        my_dict[num_page] = new_part[0].strip()
        next_sym = new_part[1]
        num_page += 1
        start_p = start_p + next_sym + 1
    return my_dict


prepare_book(book_path)
# for k, v in my_dict.items():
#     print(k, len(v), v, sep='\n---------------------------\n')
