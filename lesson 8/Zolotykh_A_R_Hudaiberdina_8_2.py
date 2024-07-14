class InvalidOperationError(Exception):#задаем класс для собственного исключения
    def __init__(self, text = 'Выбран неверный тип операции'):
        self.text = text
        super().__init__(self.text)#тупо скопировал, чтобы работало. Для нормального понимания нужно ООП.
try:
    n1 = float(input('Введите первое число: '))
    n2 = float(input('Введите второе число: '))
    action = input('Введите тип операции: ')
    if action == '+':
        print(n1 + n2)
    elif action == '-':
        print(n1 - n2)
    elif action == '*':
        print(n1 * n2)
    elif action == '/':
        print(n1/n2)
    elif action not in ('+-*/'):
        raise InvalidOperationError#вызываем собственное исключение
except ZeroDivisionError:
    print('Деление на 0 не возможно')#отлавливаем исключение в случае деления на 0
except ValueError:
    print('Введен неверный тип данных')#отлавливаем исключение, когда введен неправильный тип данных, т.е. не int и не float
# except InvalidOperationError:
#     print('Выбран неверный тип операции')#отлаливаем собственное исключение при его возникновении, если раскоментировать