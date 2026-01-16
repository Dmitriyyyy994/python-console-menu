while True:
    print('1 - привітатись')
    print('2 - перевірити вік')
    print('3 - порахувати суму двох чисел')
    print('0 - вихід')

    choice = input('Виберіть число: ')

    if choice == '1':
        print('Привіт!')

    elif choice == '2':
        age = int(input('Введіть вік: '))
        if age < 0 or age > 120:
            print('Некоректний вік')
        elif age < 18:
            print('Неповнолітній')
        else:
            print('Повнолітній')

    elif choice == '3':
        a = int(input('Перше число: '))
        b = int(input('Друге число: '))
        print('Сума: ', a + b)

    elif choice == '0':
        print('Вихід з програми!')
        break

    else:
        print('Некоректний вибір')
