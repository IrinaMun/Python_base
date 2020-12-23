# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

seasons = {"зима": (1, 2, 12),
           "весна": (3, 4, 5),
           "лето": (6, 7, 8),
           "осень": (9, 10, 11)}
result_season = None
month = int(input("Введите номер месяца: "))
for key in seasons.keys():
    if month in seasons[key]:
        result_season = key
if result_season is None:
    print("Такого месяца не существует!")
else:
    print(f'Сезон: {result_season}.')
