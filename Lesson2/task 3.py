# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

seasons = {"Зима": (1, 2, 12),
           "Весна": (3, 4, 5),
           "Лето": (6, 7, 8),
           "Осень": (9, 10, 11)}
result_season = None
month = int(input("Введите номер месяца: "))
for key in seasons.keys():
    if month in seasons[key]:
        result_season = key
if result_season is None:
    print("Такого месяца не существует!")
else:
    print(result_season)
