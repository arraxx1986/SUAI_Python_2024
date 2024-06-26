import time
#импортируем библиотеку time, чтобы дать время пользователю ознакомится с использованием программы калькулятор
print("""Программа "Калькулятор" предоставляет возможность
         проводить простые математические расчеты как с целыми числами,
         так и числами с плавающей точкой, а также сравнение чисел.
         Сначала необходимо выбрать режим работы калькулятора.
      
         В режиме математических операций запрашивается два числа, которые необходимо ввести по запросу программы
         Для суммы необходимо ввести "+"
         Для разности необходимо ввести "-"
         Для произведения необходимо ввести "*"
         Для деления необходимо ввести "/"
         Для возведения в степень необходимо ввести "**"
         Для извлечения квадратного корня необходимо ввести  "sqrt" """)
time.sleep(5)
#программа калькулятор
#импортируем библиотеку math
import math
print()
#выбираем тип float, потому что при выборе типа int и введении чисел типа float будет ошибка
flag = True
while flag:
    a = float(input("введите первое число a: "))
    b = float(input("введите второе число b: "))
    print("""Введите режим работы калькулятора:
        - математические операции (нажмите 1)
        - операции сравнения (нажмите 2)""")
    reg = int(input())
    if (reg == 1):
        m_op = input("введите знак математической операции: ")
        if (m_op=="+"):
            print("сумма введенных чисел равна: ", a+b, sep="")
        elif (m_op=="-"):
            print("разность введенных чисел равна: ", a-b, sep="")
        elif(m_op=="/"):
         #вводим дополнительное условие для предотвращения ошибки деления на 0
            if (b==0):
                 print("ошибка, деление на ноль не возможно")
            else:
                print("отношение введенных чисел равно: ", a/b, sep="")
        elif(m_op=="*"):
            print("произведение введенных чисел равно: ", a*b, sep="")
        elif(m_op=="**"):
            print("результат возведения первого числа в степень второго: ", a**b, sep="")
        elif(m_op=="sqrt"):
            print("результат извлечения квадратного корня из первого числа: ", math.sqrt(a), sep="")
            print("результат извлечения квадратного корня из второго числа: ", math.sqrt(b), sep="")
        else:
            print("введен знак, не соответствующий ни одной из математических операций")
    elif(reg==2):
        if (a==b):
            print("Первое число равно второму")
        elif (a > b):
            print("Первое число больше втрого")
        else:
            print("Первое число меньше второго")
    else:
        print("Введен неправильный режим калькулятора")
    print("Для выхода из программы нажмите *")
    print("Для дальнейшей работы программы нажмите Enter")
    esc = input()
    if (esc == "*"):
        flag = False
    else:
        continue

