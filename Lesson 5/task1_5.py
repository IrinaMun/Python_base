# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

with open("text_input5_1.txt", "w", encoding="utf-8") as word_string:
    while True:
        lines = input("Введите строку: ")
        if not lines:
            break
        word_string.write(lines + "\n")
