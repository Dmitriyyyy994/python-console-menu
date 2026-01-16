balance = 1000

while True:
    print('1 - показати баланс')
    print('2 - додати гроші')
    print('3 - зняти гроші')
    print('0 - вихід')

    choice = input('Вибери дію: ')

    if choice == '1':
        print('Ваш баланс:', balance)

    elif choice == '2':
        amount = int(input('Введи суму: '))
        balance += amount
        print('Новий баланс: ', balance)

    elif choice == '3':
        amount = int(input('Введи суму:'))
        balance -= amount
        print('Новий баланс: ', balance)

    elif choice == '0':
        print('Вихід')
        break
