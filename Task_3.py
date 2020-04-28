# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и
# величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее
# 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода
# сотрудников.

with open('Task_3.txt', 'r', encoding='utf-8') as open_file:
    pay_summ = []
    list_lines = open_file.readlines()
    for item in range(len(list_lines)):
        list_line = list_lines[item].split()
        pay_summ.append(float(list_line[1]))
        if float(list_line[1]) < 20000:
            print(f'Фамилия сотрудника с окладлм меньше 20 тыс.: {list_line[0]}')
    print(f'Средняя величина дохода сотрудников: {round(sum(pay_summ) / len(list_lines), 2)}')
