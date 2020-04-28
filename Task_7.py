# Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая
# строка должна содержать данные о фирме: название, форма собственности, выручка,
# издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также
# среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать .
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а
# также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в
# словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{ "firm_1" : 5000 , "firm_2" : 3000 , "firm_3" : 1000 }, { "average_profit" : 2000 }]
from json import dump

firm_dict = {}
av_prof_dict = {}
json_list = []
av_prof = 0

with open('Task_7.txt', 'r', encoding='utf-8') as f:
    len_f = len(f.readlines())
    f.seek(0)
    for i in range(len_f):
        read_f = f.readline()
        read_f = read_f.split()
        revenue = int(read_f[2]) - int(read_f[3])
        firm_dict[read_f[0]] = revenue
        if revenue > 0:
            av_prof += revenue

    av_prof_dict['average_profit'] = av_prof / len_f
    json_list.append(firm_dict)
    json_list.append(av_prof_dict)
    print(json_list)

with open('Task_7.json', 'w') as f:
    dump(json_list, f)
