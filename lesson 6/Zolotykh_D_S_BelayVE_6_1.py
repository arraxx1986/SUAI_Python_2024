s = input().split(' ')
""" на вход подается строка "Белай Василий 
Евгеньевич 29.06.1995", которая превращается с
разу в список(разделитель пробел)"""
s = s[:-1] + s[-1].split('.')
"""последний элемент списка разделяем по точке на 
новые элементы списка и присоединяем к предыдущим
print(s)"""
print(s)

