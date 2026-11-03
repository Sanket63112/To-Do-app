message = "type add or show or exit or edit or complete:"


# problems faced:
# 1. what if user gave input which is incorrect
# 2. how to handle input if its int / float
# 3. storing todos in txt file, available when program is not running

while True:
    user_action = input(message)
    user_action = user_action.strip()
    match user_action:
        case 'add':
            todo = input("enter a todo: ") + '\n'

            # file = open('todos.txt', 'r')
            # todos = file.readlines()
            # file.close()

                    #or

            with open('../todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            with open('../todos.txt', 'w') as file:
                file.writelines(todos)

        case 'show':
            # print(todos)
            # for i in range(len(todos)):
            with open('../todos.txt', 'r') as file:
                todos = file.readlines()

            # new_todo = [ item.strip('\n') for item in todos]

            for i, todo in enumerate(todos):
                todo = todo.strip('\n')   # same as above list comprehension
                print(f"{i+1}. {todo.capitalize()}")
        case 'edit':
            number = int(input("enter the index : "))
            number = number - 1

            with open('../todos.txt', 'r') as file:
                todos = file.readlines()

            new_todo = input(message)
            todos[number] = new_todo

            with open('../todos.txt', 'w') as file:
                file.writelines(todos)
        case 'complete':
            number = int(input("enter the index : "))
            number = number - 1

            with open('../todos.txt', 'r') as file:
                todos = file.readlines()
            completed_todo = todos[number].strip('\n')
            todos.pop(number)

            with open('../todos.txt', 'w') as file:
                file.writelines(todos)
            print(f'Great!, you have completed - {completed_todo} task!')
        case 'exit':
            break
        case _:
            print('pls enter correctly')

print('closed todo app!')