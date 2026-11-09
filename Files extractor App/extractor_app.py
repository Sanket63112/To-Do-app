import FreeSimpleGUI as sg
from zip_extractor import archive

sg.theme('Black')

label1 = sg.Text('Select the zipfile:')
input1 = sg.Input()
choose_button1 = sg.FileBrowse('Choose',key='file')

label2 = sg.Text('Select the folder:')
input2 = sg.Input()
choose_button2 = sg.FolderBrowse('Choose',key='folder')
extract_button = sg.Button('Extract')
output_label = sg.Text(key="output")

window = sg.Window('Archieve Extractor',
                   layout=[
                       [label1,input1,choose_button1],
                       [label2,input2,choose_button2],
                       [extract_button,output_label]
                   ])
while True:
    event, value = window.read()
    print(event,value)
    archive_path = value['file']
    dest_path = value['folder']
    archive(archive_path,dest_path)
    window["output"].update(value='Successfully extracted!!')

window.close()