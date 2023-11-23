"""From JSON file exercise"""

import json


def from_json_file(file_name_):
    """Read JSON object from the file"""

    with open(file_name_, 'r', encoding="utf-8") as json_file:
        return json.load(json_file)


# YOUR CODE HERE

if __name__ == "__main__":
    import os

    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_name = f"{dir_path}/data.json"

    data_object = from_json_file(file_name)

    print(data_object)
    print(type(data_object))
    print()
    for key, val in data_object.items():
        print(f"{key}: {type(val).__name__}")
