def my_fun(n_1, n_2):
    """
    Выполняет деление, при делении на ноль выводит ошибку и завершает программу
    :param n_1: первое число
    :param n_2: второе число
    :return: деление первого числа на второе
    """
    try:
        div = n_1 / n_2
    except ZeroDivisionError as err:
        print(err)
        exit(0)
    else:
        print(f"{n_1} / {n_2} = {div:.2f}")


my_fun(float(input("Введите первое число: ")), float(input("Введите второе число: ")))
