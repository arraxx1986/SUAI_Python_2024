'''
Программа запрашивает на ввод целое положительное число.
Запуская рекурсию выводятся числа от введенного до 0 с шагом 1.
'''
def conter_to_zero(n):
    if n < 0:#при введении отрицательного числа выводится соответствующее сообщение и программа завершает работу
        print('Введено отрицательное число')
    else:
        print(n)#в консоль выводится число от введенного пользователем до 0
        if n > 0:
            return conter_to_zero(n-1)#функция вызывает саму себя, но значение n на 1 меньше. Базовый случай, когда n = 0.
try:#срабатывает при введении данных типа str или float
    n = int(input('Введите целое положительное число: '))
    conter_to_zero(n)
except ValueError:
    print('Введены данные неправильного типа')