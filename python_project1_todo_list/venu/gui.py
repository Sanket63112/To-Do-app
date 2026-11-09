import functions
import FreeSimpleGUI as sg
import time

sg.theme('black')

clock = sg.Text('',key='clock')
label = sg.Text('Enter a To-Do')
input_box = sg.InputText(tooltip='Enter a to-do', key='todo')
add_button = sg.Button(size=2, image_source='add.png', mouseover_colors='DarkBlue1', tooltip='Add Todo', key='Add')
list_box = sg.Listbox(functions.get_todo(), key='todos',
                      enable_events=True, size=[45, 10])
edit_button = sg.Button('Edit')
complete_button = sg.Button('Complete')
exit_button = sg.Button('Exit')

window = sg.Window('My To-Do App',
                   layout=[
                       [clock],
                       [label],
                       [input_box, add_button],
                       [list_box, edit_button, complete_button],
                       [exit_button]
                   ],
                   font=('Poppins', 15))

while True:
    event, value = window.read(timeout=1000)
    window['clock'].update(value=time.strftime('%d %b %Y %H:%M:%S'))
    print(event)
    print(value)
    match event:
        case 'Add':
            todos = functions.get_todo()
            new_todo = value['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todo(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')
        case 'Edit':
            try:
                todo_to_edit = value['todos'][0]
                new_todo = value['todo'] + '\n'
                todos = functions.get_todo()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todo(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup('Pls select one of todos to Edit',font=('Poppins',16))
        case 'Complete':
            try:
                todo_to_complete = value['todos'][0]
                todos = functions.get_todo()
                todos.remove(todo_to_complete)
                functions.write_todo(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup('Pls select one of todos to Complete',font=('Poppins',16))
        case 'Exit':
            break
        case 'todos':
            window['todo'].update(value=value['todos'][0])
        case sg.WIN_CLOSED:
            break

window.close()
