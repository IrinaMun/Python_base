# Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее
# сумме и после этого завершить программу.
# 1 2 3 4 5 6 7
def my_fan():
    total = 0

    while True:
        user_num = input("Ведите несколько чисел через пробел для прекращения работы программы, нажмите 'z': \n").split()
        for dig in user_num:
            if dig.isdigit():
                total += int(dig)
            elif dig == 'z':
                print(total)
                exit(0)
        print(total)

if __name__ == '__main__': my_fan()
