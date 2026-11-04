import functions
import FreeSimpleGUI as sg

label = sg.Text('Enter a To-Do')
input_box = sg.InputText(tooltip='Enter a to-do')
add_button = sg.Button('Add')

window = sg.Window('My To-Do App', layout=[[label, input_box,add_button]])
window.read()
window.close()