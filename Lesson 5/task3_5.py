# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

with open("Txt_python5_3.txt", "r", encoding="utf-8") as salary_string:
    workers = {}
    for line in salary_string:
        line_list = line.split()
        workers[line_list[0]] = float(line_list[-1])
    for family, salary in workers.items():
        if salary <= 20000:
            print(family, salary)
    print("Средняя величина дохода сотрудников: ", sum(workers.values()) / len(workers.keys()))
