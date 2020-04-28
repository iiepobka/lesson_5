# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно
# данные. При этом английские числительные должны заменяться на русские. Новый блок строк
# должен записываться в новый текстовый файл.

with open('Task_4.txt', 'r', encoding='utf-8') as f:
    read_lines = f.readlines()
    my_list = ['Один', 'Два', 'Три', 'Четыре']
    new_lines = []
    for i in range(len(read_lines)):
        line = read_lines[i].split()
        line.insert(0, my_list[i])
        del line[1]
        line = ' '.join(line[:])
        line = line + '\n'
        new_lines.append(line)


with open('Task_4_1.txt', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

# другой вариант

with open('Task_4.txt', 'r', encoding='utf-8') as f:
    my_list = ['Один', 'Два', 'Три', 'Четыре']
    new_lines = []
    for i in range(len(read_lines)):
        read_lines = f.readline()
        line = read_lines.split()
        line.insert(0, my_list[i])
        del line[1]
        line = ' '.join(line[:])
        line = line + '\n'
        new_lines.append(line)

with open('Task_4_1.txt', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)


