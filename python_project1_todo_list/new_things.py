mylist = ['hello', 'mercedes', 'benz', 'porch']

mylist[0].title()

len(mylist)

mylist.pop(3)

mylist.append('porch')

print(mylist[0])
#or
mylist.__getitem__(0)

mylist[2]= 'suzuki'
# or
mylist.__setitem__(2,'suziki')

# you can change items in list by indexing but not in string
filename = '1.fileloop.txt'
# filename[1] = '-' gives error
filename = filename.replace('.', '-', 1)

# when u read a file once, its cursor now goes to end of file, so if you once again read that
#it will not read anything as it was already at end of file

# list comprehension:
mylist_updated = [name.title() for name in mylist]
filenames = ['1.filelopp.txt', '2.document.txt', '3.music.mp3']

for filename in filenames:
    filename = filename.replace('.', '-', 1)
    print(filename)

# for missing arguments in function calling it gives typeerror:

