FILENAME = '../todos.txt'


def get_todo(filename=FILENAME):
    #doc string
    """Reads file from computer and return the contents """
    with open(filename, 'r') as file:
        todos_local = file.readlines()
    return todos_local


def write_todo(todos_w, filename=FILENAME):
    """Write the contents in todos_w in text files todos.txt"""
    with open(filename, 'w') as file:
        file.writelines(todos_w)


if __name__ == "__main__":
    print("helllo")
