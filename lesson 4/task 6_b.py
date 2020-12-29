# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.

from itertools import cycle

num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def cyclinator(iter_list):
    count = 0
    for item in cycle(iter_list):
        if count >= len(iter_list) * 2:
            break
        yield item
        count += 1


print([i for i in cyclinator(num_list)])