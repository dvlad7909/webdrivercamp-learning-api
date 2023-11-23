"""Read a file exercise"""


def read_a_file(filename):
    """Read 3-rd line function"""

    with open(filename, 'r', encoding="utf-8") as read_file:
        line = read_file.readlines()[2]
        print(line)


# YOUR CODE HERE

if __name__ == "__main__":
    import os

    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_name = f"{dir_path}/data.txt"

    read_a_file(file_name)
