def save_notes_to_file():
    try:
        with open('Notes Manager.txt', 'w', encoding='utf-8') as file:
            for i in range(len(notes)):
                file.write(f'Заметка №{i+1}.\n')
                for key , value in notes[i].items():
                    file.write(f'{key} : {value}\n')
                file.write("-------------------------------------\n")

    except FileNotFoundError:
        print("Файл 'Notes Manager.txt не найден'.")
        with open('Notes Manager.txt', 'w', encoding='utf-8') as file:
            print('Создан новый файл. "Notes Manager.txt"')

notes = [
    {'Имя': 'Иван', 'Заголовок': 'План работы', 'Описание': 'Завершить проект', 'Статус': 'выполнена',
     'Дата создания': '20.11.2024', 'Дедлайн': '26.11.2024'},
    {'Имя': 'Мария', 'Заголовок': 'Учеба', 'Описание': 'Подготовиться к экзамену', 'Статус': 'в процессе',
     'Дата создания': '25.11.2024', 'Дедлайн': '01.12.2024'}
]

save_notes_to_file()