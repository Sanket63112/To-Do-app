password = input("enter the password")

result = {}

if len(password) >= 8:
    result['length'] = True
else:
    result['length'] = False

digit = False
for i in password:
    if i.isdigit():  # newfunction
        digit = True
result['digit'] = digit

uppercase = False
for i in password:
    if i.isupper(): # newfunction
        uppercase = True
result['uppercase'] = uppercase

if all(result.values()):    # newfunction
    print('Strong password')
else:
    print('Weak password')
