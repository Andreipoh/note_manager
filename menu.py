from datetime import date

def create_note():
    n = 0
    a = input('Введите имя пользователя: ')
    b = input('Введите заголовок заметки: ')
    c = input('Введите описание заметки: ')
    d = input('Введите статус заметки (новая, в процессе, выполнено): ')
    e = date.today()
    f = input('Введите дедлайн (день-месяц-год): ')
    note = {f'{1+n}.' 'username': a, 'title': b, 'content': c, 'status': d, 'created_date ': f'{e.day}-{e.month}-{e.year}', 'issue_date': f }
    notes.append(note)
    n = n + 1

def display_notes(notes):
    for note in notes:
        print('------------------------------')
        for key in note:
            print(key, note[key])

def update_note(note):
    a = input('Какие данные вы хотите обновить? (username, title, content, status, issue_date): ')
    if note[a]:
        b = input(f'Введите новое значение для {a}: ')
        note[a] = b
    print(note)

def delete_note(notes):
    for note in notes:
        for key in note:
            print(key, note[key])
    a = input('Введите имя пользователя или заголовок для удаления заметки: ')
    for i in reversed(range(len(notes))):
        if (notes[i]['username'] == a) or (notes[i]['title'] == a):
            del notes[i]
    print('Успешно удалено. Остались следующие заметки:')
    for note in notes:
        for key in note:
            print(key, note[key])

def search_notes(notes, keyword=None, status=None):
    if len(notes) == 0:
        print("\nСписок заметок пуст.\nПоиск невозможен.")
        return
    if keyword is None and status is None:
        print("\nКлючевое слово и/или Статус не введены.\nПоиск завершен.")
    elif keyword != None and status is None:
        j = 0
        for i in range(len(notes)):
            cur_values = list(notes[i].values())
            for k in range(len(cur_values)):
                if keyword in cur_values[k]:
                    j += 1
                    if j == 1:
                        print(f"\nПо Ключевому слову - '{keyword}' найдены заметки:")
                        print(f"Заметка{j}.")
                    else:
                        print(f"Заметка{j}.")
                    for key, value in notes[i].items():
                        print(key, "-", value)
        if j == 0:
            print(f"\nКлючевого слова - '{keyword}' в заметках не существует."
                  "\nПоиск завершен.")

    elif keyword is None and status != None:
        j = 0
        for i in range(len(notes)):
            if status == notes[i].get('status'):
                j += 1
                if j == 1:
                    print(f"\nПо Статусу - '{status}' найдены заметки:")
                    print(f"Заметка{j}.")
                else:
                    print(f"Заметка{j}.")
                for key, value in notes[i].items():
                    print(key, "-", value)
        if j == 0:
            print(f"\nСтатуса - '{status}' в заметках не существует."
                  "\nПоиск завершен.")
    else:
        j = 0
        for i in range(len(notes)):
            cur_values = list(notes[i].values())
            for k in range(len(cur_values)):
                if keyword in cur_values[k] and status == notes[i].get('status'):
                    j += 1
                    if j == 1:
                        print(f"\nПо Ключевому слову - '{keyword}' и Статусу - '{status}' найдены заметки:")
                        print(f"Заметка{j}.")
                    else:
                        print(f"Заметка{j}.")
                    for key, value in notes[i].items():
                        print(key, "-", value)

        if j == 0:
            print(f"\nНе найдены заметки с одновременным наличием Ключевого слова - '{keyword}' и Статуса - '{status}'."
                  "\nПоиск завершен.")

notes = []

print('Меню действий:')
print('1. Создать новую заметку')
print('2. Показать все заметки')
print('3. Обновить заметку')
print('4. Удалить заметку')
print('5. Найти заметки')
print('6. Выйти из программы')

while True:
    x = input('Ваш выбор: ')
    if x == 1:
        create_note()
    elif x == 2:
        display_notes(notes)
    elif x == 3:
        update_note(notes)
    elif x == 4:
        delete_note(notes)
    elif x == 5:
        search_notes(notes, keyword=input('Введите ключевое слово: '), status=input('Введите статус: '))
    elif x == 6:
        print('Программа завершена. Спасибо за использование!')
        break
    else: print('Неверный выбор. Пожалуйста, выберите действие из списка.')