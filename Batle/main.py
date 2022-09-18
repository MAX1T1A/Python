def matrix(flo):
    for u in range(len(flo)):
        for j in range(len(flo[u])):
            print(flo[u][j], end=' ')
        print()


floor = [
    [' ', '  а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'к'],
    [' 1|', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
    [' 2|', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
    [' 3|', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
    [' 4|', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
    [' 5|', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
    [' 6|', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
    [' 7|', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
    [' 8|', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
    [' 9|', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
    ['10|', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_']
]

matrix(floor)


letters = {'а': 1,
           'б': 2,
           'в': 3,
           'г': 4,
           'д': 5,
           'е': 6,
           'ж': 7,
           'з': 8,
           'и': 9,
           'к': 10
           }


Caesar_encryption = {
    'а': 'ъ',
    'б': 'ё',
    'в': 'э',
    'г': 'ь',
    'д': 'и',
    'е': 'у',
    'ж': 'м',
    'з': 'ч',
    'и': 'к',
    'к': 'г',
    '1': '90',
    '2': '93',
    '3': '80',
    '4': '69',
    '5': '67',
    '6': '50',
    '7': '74',
    '8': '60',
    '9': '82',
    '10': '58'
}


Caesar_decoding = {
    'ъ': 'а',
    'ё': 'б',
    'э': 'в',
    'ь': 'г',
    'и': 'д',
    'у': 'е',
    'м': 'ж',
    'ч': 'з',
    'к': 'и',
    'г': 'к',
    '90': '1',
    '93': '2',
    '80': '3',
    '69': '4',
    '67': '5',
    '50': '6',
    '74': '7',
    '60': '8',
    '82': '9',
    '58': '10'
}


Caesar = []
count_boss = 1
while count_boss <= 4:
    print('\n\nКакой вид техники вы хотите разместить?'
          '\nКорабли по 1 клетке - 1(обозначение)'
          '\nКорабли по 2 клетки - 2(обозначение)'
          '\nКорабли по 3 клетки - 3(обозначение)'
          '\nКорабль 4 клетки - 4(обозначение)')
    boss_input = input()
    if boss_input == '1':
        count_first_teh = 1
        while count_first_teh <= 4:
            print('Укажите координаты буквы и числа:')
            isXinCODE = input('Координаты по букве: ').lower()
            X = letters[isXinCODE]
            Caesar.append(Caesar_encryption[isXinCODE])
            isYinCODE = input('Координаты по числу: ')
            Y = int(isYinCODE)
            Caesar.append(Caesar_encryption[str(isYinCODE)])
            floor[Y][X] = 1
            matrix(floor)
            count_first_teh += 1

    elif boss_input == '2':
        count_second_teh = 1
        while count_second_teh <= 6:
            print('Укажите координаты буквы и числа:')
            isXinCODE = input('Координаты по букве: ').lower()
            X = letters[isXinCODE]
            Caesar.append(Caesar_encryption[isXinCODE])
            isYinCODE = input('Координаты по числу: ')
            Y = int(isYinCODE)
            Caesar.append(Caesar_encryption[str(isYinCODE)])
            floor[Y][X] = 2
            matrix(floor)
            count_second_teh += 1

    elif boss_input == '3':
        count_third_teh = 1
        while count_third_teh <= 6:
            print('Укажите координаты буквы и числа:')
            isXinCODE = input('Координаты по букве: ').lower()
            X = letters[isXinCODE]
            Caesar.append(Caesar_encryption[isXinCODE])
            isYinCODE = input('Координаты по числу: ')
            Y = int(isYinCODE)
            Caesar.append(Caesar_encryption[str(isYinCODE)])
            floor[Y][X] = 3
            matrix(floor)
            count_third_teh += 1

    elif boss_input == '4':
        count_fourth_teh = 1
        while count_fourth_teh <= 4:
            print('Укажите координаты буквы и числа:')
            isXinCODE = input('Координаты по букве: ').lower()
            X = letters[isXinCODE]
            Caesar.append(Caesar_encryption[isXinCODE])
            isYinCODE = input('Координаты по числу: ')
            Y = int(isYinCODE)
            Caesar.append(Caesar_encryption[str(isYinCODE)])
            floor[Y][X] = 4
            matrix(floor)
            count_fourth_teh += 1
    else:
        print('Вы ничего не ввели!')

    count_boss += 1


print('Код для вашего соперника\n',
      " ".join(map(str, Caesar)))


user_into = input('Введите код, который вам передал соперник').split()
for i in user_into:
    Caesar.append(Caesar_decoding[i])


print('\n\n\nИгра началась!!!')
count_boss_second = 1
while count_boss_second <= 20:
    print('Укажите координаты буквы и числа:')
    X = letters[input('Координаты по букве: ').lower()]
    Y = int(input('Координаты по числу: '))
    if floor[Y][X] == 1:
        floor[Y][X] = '×'
        print('Уничтожил!')
    elif floor[Y][X] == 2:
        floor[Y][X] = '×'
        print('Попал!')
    elif floor[Y][X] == 3:
        floor[Y][X] = '×'
        print('Попал!')
    elif floor[Y][X] == 4:
        floor[Y][X] = '×'
        print('Попал!')
    else:
        print('Мимо!!!!')

    count_boss_second += 1
