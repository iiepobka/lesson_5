# Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить
# ее на экран.

with open('Task_5.txt', 'w+', encoding='utf-8') as f:
    wtite_f = f.write('1 1 2 3 5 28 16 45 85 100 11 2 0 -1 -2')
    f.seek(0)
    read_f = f.readlines()
    read_f = read_f[0].split()
    for i in range(len(read_f)):
        read_f[i] = int(read_f[i])
    print(f'Сумма чисел, записанныхь в файл: {sum(read_f)}')


