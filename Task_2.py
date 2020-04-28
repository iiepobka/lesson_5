# Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить
# подсчет количества строк, количества слов в каждой строке.

with open('Task_2.txt', 'r', encoding='utf-8') as open_file:
    count_lines = open_file.readlines()
    print('Кол-во строк в файле Task_2.txt: ', len(count_lines))

    for item in range(len(count_lines)):
        count_words = count_lines[item].split()
        print('Кол-во слов в', item + 1, '-й строке файла Task_2.txt: ', len(count_words))
