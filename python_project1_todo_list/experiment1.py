import glob

myfilepath = glob.glob('*.txt')

for filepath in myfilepath:
    with open(filepath,'r') as file:
        print(file.read())