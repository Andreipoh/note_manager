from itertools import count


def append_notes_to_file(notes, filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            info = file.readlines()
            count = 0
            for line in info:
                if 'Заметка' in line:
                    count +=1
        pass
        with open(filename, 'a', encoding='utf-8') as file:
            for i in range(len(notes_add)):
                file.write(f'Заметка № {count+1+i}\n')
                for key , value in notes[i].items():
                    file.write(f'{key} : {value}\n')
                file.write("-------------------------------------\n")

    except FileNotFoundError:
        print("Файл 'Notes Manager.txt не найден'.")
        with open('Notes Manager.txt', 'x', encoding='utf-8') as file:
            print('Создан новый файл. "Notes Manager.txt"')


notes_add = [
    {'Имя': 'Антон', 'Заголовок': 'Диссертация', 'Описание': 'Глава 1', 'Статус': 'выполнена',
     'Дата создания': '20.11.2024', 'Дедлайн': '26.11.2024'},
    {'Имя': 'Мария', 'Заголовок': 'Учеба', 'Описание': 'Подготовиться к экзамену', 'Статус': 'в процессе',
     'Дата создания': '25.11.2024', 'Дедлайн': '01.12.2024'}
                ]

append_notes_to_file(notes_add, 'Notes Manager.txt')
