# Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух
# аргументов.
def my_func(x, y, z):
    list = [x, y, z]

    max_1 = max(list)
    list.remove(max_1)
    max_2 = max(list)
    print(f'{max_1} + {max_2} = {max_1 + max_2}')


my_func(float(input("Введите первое число: ")),
        float(input("Введите второе число: ")),
        float(input("Введите третье число: ")))
