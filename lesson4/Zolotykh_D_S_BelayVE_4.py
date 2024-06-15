while True:
    print("Перед Вами программа, определяющая четверть координатной плоскости по значениям координат")
    point_number = int(input("Введите количество оцениваемых точек: "))
    for i in range (point_number):
        print("Проводим оценку точки №",i+1, sep="")
        x_value = int(input("Введите значение координаты X: "))
        y_value = int(input("ведите значение координаты Y: "))
        if (x_value>0 and y_value>0):
            print("Первая четверть координатной плоскости")
        elif(x_value<0 and y_value>0):
            print("Вторая четверть координатной плоскости")
        elif(x_value<0 and y_value<0):
            print("Третья четверть координатной плоскости")
        elif(x_value>0 and y_value<0):
            print("Четвертая четверть координатной плоскости")
        elif(x_value==0 and y_value==0):
            print("Центр координат")
        elif(x_value==0 and (y_value>0 or y_value<0)):
            print("Точка лежит на оси Y")
        elif((x_value<0 or x_value>0) and y_value==0):
            print("Точка лежит на оси X")
    print("Для выхода из программы нажмите: *")
    print("Для продолжения программы нажмите клавишу Enter")
    a = input()
    if a == "*":
        break
    else:
        continue
