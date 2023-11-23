"""JSON to file exercise"""

import json


def to_json_file(file_name_):
    """Serializes the object to a file"""

    data_object = {"list": [1, 2, 3, 4, 5],
                   "tuple": (1, 2, 3, 4, 5),
                   "string": "Hello World!",
                   "bool": False,
                   "null": None,
                   "int": 123,
                   "float": 3.14,
                   "dict": {"abc": True, "Hello": "World", 10: [2, 3, 4]}}
    with open(file_name_, 'w', encoding="utf-8") as json_file:
        json.dump(data_object, json_file)
    # YOUR CODE HERE


if __name__ == "__main__":
    import os

    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_name = f"{dir_path}/data.json"

    to_json_file(file_name)

    with open(file_name, "r", encoding="utf-8") as f:
        print(f.read())
