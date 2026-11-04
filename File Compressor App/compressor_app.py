import FreeSimpleGUI as sg
from Zip_compressor import make_archive

label1 = sg.Text('Choose the files to compress')
input1 = sg.Input()
choose_button1 = sg.FilesBrowse('Choose',key='files')

label2 = sg.Text('Choose the files to compress')
input2 = sg.Input()
choose_button2 = sg.FolderBrowse('Choose', key='folders')
compress_button = sg.Button('Compress')
output_label = sg.Text(key='output', text_color='green')

window = sg.Window('File Compressor',
                   layout=[
                       [label1,input1, choose_button1],
                       [label2,input2,choose_button2],
                       [compress_button, output_label]
                   ]
                )
while True:
    event, value = window.read()
    print(event)
    print(value)
    filepaths = value['files'].split(';')
    destination = value['folders']
    make_archive(filepaths,destination)
    window['output'].update('Files are compressed!')

window.close()
