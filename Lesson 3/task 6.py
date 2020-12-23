# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной
# первой буквой.
# Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием.
# В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно
# начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().

user_text = ''.join(filter(str.isascii, input('Введите несколько слов на английском: \n'))).split()
# введенные юзером слова проверяются фильтром при помощи метода .isascii на наличие отличных от английских букв, после
# проверки преобразует в строку при помощи метода .join, преобразует в список по пробелам при помощи метода .split()


def int_func(text: str):
    """
    Переводит первый символ строки в верхний регистр, а все остальные в нижний
    :param text: принимается строка
    :return: возвращает строку, где первый символ заглавный, а остальные прописные
    """
    return text.capitalize()


result_text = list(map(int_func, user_text))
print(' '.join(result_text))