def validate_args(func):
    def inner(*args):
        counter = 0 #счетчик принимает изначальное значение 0
        lst = list(args) #получаем список аргументов
        for i in lst:
            if type(i) != int: #если хотя бы один из аргументов не типа int, то его значение увеличивается на 1
                counter +=1
        if counter == 0: #если счетчик равен 0, то все значения типа int и декорируемая цункция выполняется
             return func(*args)
        else:
            raise TypeError('Ошибка: введены данные неправильного типа')#в ином случае выдается ошибка TypeError
    return inner


@validate_args
def some_function(*args):
    print ('Функция выполняется')
    for i in args:
        print(type(i), ' ', i)

some_function()

