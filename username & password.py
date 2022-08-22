username = 'nazanin barmaki'
password = 67389260
counter = 0

while (counter < 3):
    name = input('please enter user:')
    pas = int(input('please enter pass:'))

    if (name == username) and (pas == password):
        print('welcom')
        break
    else:
        print('password or username incorect')
        counter = counter + 1

    if ( counter > 2):
        print ('access denid')
