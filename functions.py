
FILEPATH = r"todos.txt"


def get_todos(filepath_local = FILEPATH):
    """
    # todos = file.read()  # Returns string of entire text file
    # todos = file.readline()   # Returns only one row as a string type
    # todos = file.readlines()  # all lines are read and returned as a list
    """
    with open(filepath_local, 'r') as file_local:  # r"..." stands for "raw string" - use with backslashes.
        # Using "with" makes closing file unnecessary - it prevents memory leaks
        todos_local = file_local.readlines()  # Returns list of strings,
    return todos_local


def write_todos(todos_arg, filepath_local = FILEPATH):
    """todos_arg - list to write
    """
    with open(filepath_local, 'w') as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print(get_todos())