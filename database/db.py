import json

path_data_json = 'database/data.json'

questions = {}


user_db: dict = {}

# user_db: dict = {
#     'current_question': 1,
#     'current_test': ''
# }


def read_data(path):
    with open(path, "r") as json_file:
        return json.load(json_file)


def write_data(path):
    with open(path, "w") as json_file:
        json.dump(user_db, json_file)
