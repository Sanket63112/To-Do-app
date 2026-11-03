message = "type add or show or exit or edit or complete:"

from functions import get_todo, write_todo
import time

now = time.strftime('%B %d, %Y, %H:%M:%S')
print("It's ",now)

# problems faced:
# 1. what if user gave input which is incorrect
# 2. how to handle input if its int / float
# 3. storing todos in txt file, available when program is not running

while True:
    user_action = input(message)
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:] + '\n'

        # file = open('todos.txt', 'r')
        # todos = file.readlines()
        # file.close()

        #or

        todos = get_todo()

        todos.append(todo)

        write_todo(todos)

    elif user_action.startswith('show'):
        # print(todos)
        # for i in range(len(todos)):
        todos = get_todo()

        # new_todo = [ item.strip('\n') for item in todos]

        for i, todo in enumerate(todos):
            todo = todo.strip('\n')  # same as above list comprehension
            print(f"{i + 1}. {todo.capitalize()}")
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = get_todo()

            new_todo = input(f'Edit new {number + 1} todo:')
            todos[number] = new_todo

            write_todo(todos)

        except ValueError:
            print('Your input is not valid, expecting number')
            continue
    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            number = number - 1

            todos = get_todo()
            completed_todo = todos[number].strip('\n')
            todos.pop(number)

            write_todo(todos)
            print(f'Great!, you have completed - {completed_todo} task!')
        except IndexError or ValueError:
            print('Your input is not valid, expecting number')
            continue
    elif user_action.startswith('exit'):
        break
    else:
        print('pls enter correctly')

print('closed todo app!')
