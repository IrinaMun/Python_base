# 1 2 3 4 5 6 7

def my_fan():
    total = 0

    while True:
        user_num = input(
            "Ведите несколько чисел через пробел для прекращения работы программы, нажмите 'z': \n").split()
        for dig in user_num:
            if dig.isdigit():
                total += int(dig)
            elif dig == 'z':
                print(f'Сумма всех введенных чисел: {total}')
                exit(0)
        print(f'Сумма всех введенных чисел: {total}')


if __name__ == '__main__': my_fan()
