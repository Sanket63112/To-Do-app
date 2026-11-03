
# message = "Enter the task:"
# todo = input(message)
# print(todo)
# print(f"type :{type(message)}")
#--------------------------------------------------

# string methods
message = "Enter the task:"
todos = []
while True:
    todo = input(message)
    todos.append(todo)
    print(todo.capitalize())
    print("mylist : {todos}")
