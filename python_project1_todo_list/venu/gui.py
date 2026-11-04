import functions
import FreeSimpleGUI as sg

label = sg.Text('Enter a To-Do')
input_box = sg.InputText(tooltip='Enter a to-do', key='todo')
add_button = sg.Button('Add')

window = sg.Window('My To-Do App',
                   layout=[[label], [input_box,add_button]],
                   font=('Poppins',15))


while True:
    event, value = window.read()
    match event:
        case 'Add':
            todos = functions.get_todo()
            new_todo = value['todo'] + '/n'
            todos.append(new_todo)
            functions.write_todo(todos)
        case sg.WIN_CLOSED:
            break

window.close()