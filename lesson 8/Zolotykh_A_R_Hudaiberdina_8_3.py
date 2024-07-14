try:
    s = []
    flag = True
    flag1 = True
    while flag1:
        while flag:
            try:
                n = input()
                if n == 'done':
                    flag = False
                else:
                    s.append(float(n))
            except ValueError:
                print('Введите число или done для завершения')
        flag1 = False
    print(s[11])
except IndexError:
    print('Отсутствует элемент списка c указанным индеком')


