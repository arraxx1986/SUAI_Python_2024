def filter_words (length):#внешняя функция принимает параметр length, ограничивающий длинну слова
    def inner_func(s):#внутренняя функция принимает список слов для дальнейшей фильтрации
        return list(filter(lambda x: len(x) == length, s))# используем функцию filter и лямбда-функцию для отбора слов из списка s, длинна которых равна параметру length
    return inner_func
