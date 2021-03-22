# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

with open("Txt_python5_4.txt", "r", encoding="utf-8") as num_line:
    num_word = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
    num_string = []
    for line in num_line:
        line_list = line.split()
        line_list[0] = num_word[line_list[0]]
        num_string.append(" ".join(line_list))
        print(num_string)

with open("rus_num.txt", "w", encoding="utf-8") as rus_list:
    rus_list.write("\n".join(num_string))
