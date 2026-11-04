import functions
import FreeSimpleGUI as sg

label = sg.Text('Enter a To-Do')
input_box = sg.InputText(tooltip='Enter a to-do', key='todo')
add_button = sg.Button('Add')
list_box = sg.Listbox(functions.get_todo(), key='todos',
                      enable_events=True, size=[45, 10])
edit_button = sg.Button('Edit')

window = sg.Window('My To-Do App',
                   layout=[
                       [label],
                       [input_box, add_button],
                       [list_box, edit_button]
                   ],
                   font=('Poppins', 15))

while True:
    event, value = window.read()
    print(event)
    print(value)
    match event:
        case 'Add':
            todos = functions.get_todo()
            new_todo = value['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todo(todos)
            window['todos'].update(values=todos)
        case 'Edit':
            todo_to_edit = value['todos'][0]
            new_todo = value['todo'] + '\n'
            todos = functions.get_todo()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todo(todos)
            window['todos'].update(values=todos)
        case 'todos':
            window['todo'].update(value=value['todos'][0])
        case sg.WIN_CLOSED:
            break

window.close()
