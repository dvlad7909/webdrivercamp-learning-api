"""Append to file"""
def append_to_file(data_, file_name_):
    """Append function"""

    with open(file_name_, 'a', encoding="utf-8") as append_file:
        append_file.write(data_)
    # with open(file_name_, 'r', encoding="utf-8") as read_file:
    #     length = len(read_file.readlines()[-1])

    return len(data_)


# YOUR CODE HERE

if __name__ == "__main__":
    import os

    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_name = f"{dir_path}/data.txt"

    data = "\nDon't Panic"

    print(f"Number of chars added: {append_to_file(data, file_name)}")

    data = "\nDon't Panic!!!"

    print(f"Number of chars added: {append_to_file(data, file_name)}")
