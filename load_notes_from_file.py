notes = []
def load_notes_from_file():
    file = open('Notes Manager.txt', encoding= 'utf-8')
    file.seek(0)
    temp_str = file.readline()
    temp_str = temp_str.replace('Имя', 'username')
    temp_str = temp_str.replace('Заголовок', 'title')
    temp_str = temp_str.replace('Описание', 'content')
    temp_str = temp_str.replace('Статус', 'status')
    temp_str = temp_str.replace('Дата создания', 'created_date')
    temp_str = temp_str.replace('Дедлайн', 'issue_date')
    j = 0  # счетчик считанных заметок
    while "Заметка" in temp_str:
        i = 0  # счетчик строк в заметке
        list_key = ['username', 'title', 'content', 'status', 'created_date', 'issue_date']
        note = {}  # создание словаря для заметок
        while i < 6:
            temp_str = file.readline()  # считываем текущую строку
            temp_str = temp_str.split(': ')  # делим строку по признаку - ': ', строки заносим в список
            temp_str = temp_str[1].split('\n')  # вторую строку списка делим строку по признаку - '\n '
            note[list_key[i]] = temp_str[0]
            i += 1
        else:
            notes.append(note)  # Добавление словаря с новой заметкой в список заметок
            j += 1
            temp_str = file.readline()  # считываем завершающую строку ("------------")
            temp_str = file.readline()  # считываем следующую строку
    print(notes)

    file.close()

load_notes_from_file()
