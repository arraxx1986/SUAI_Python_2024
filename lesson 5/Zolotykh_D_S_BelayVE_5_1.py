number = int(input("Введите целое число: "))
if (number >= 0):
    print("Число принадлежит диапазону [0; +бесконечность)")
    l = [2, 3, 5]
    count = 0
    for i in l:
        if (number%i == 0):
            print(f"Число кратно {i}")
            count +=1
    if count == 0:
        print("Число не кратно 2, 3, 5")
else:
    print("Число не принадлежит диапазону [0; +бесконечность)")

