# Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

user_items = list(input("Введите несколько произвольных значений: "))
for i in range(1, len(user_items), 2):
    user_items[i-1], user_items[i] = user_items[i], user_items[i-1]
print(user_items)