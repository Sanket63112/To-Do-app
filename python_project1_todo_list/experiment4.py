import webbrowser

user_search = input('Enter what to search:')
#use open to serach in broweser
print('searching in broweser')
webbrowser.open('https://google.com/search?q='+ user_search)