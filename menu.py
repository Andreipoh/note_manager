# Создание меню действий
from datetime import date
from datetime import datetime
# Определение функции "Создание заметки"
def create_note():
    n = 0
    username = input('Введите имя пользователя: ')
    title = input('Введите заголовок заметки: ')
    content = input('Введите описание заметки: ')
    status = input('Введите статус заметки (новая, в процессе, выполнено): ')
    created_date = date.today()
    issue_date = input('Введите дедлайн (день-месяц-год): ')
    note = {f'Заметка № {1+n}.' 'username': username, 'title': title, 'content': content, 'status': status, 'created_date': f'{created_date.day}-{created_date.month}-{created_date.year}', 'issue_date': issue_date } # Создаем словарь для заметки
    notes.append(note) # Добавление словаря с новой заметкой в список заметок
    n = n + 1
    for key in note:
        print(key, note[key])
    print("-------------------------------------")

# Определение функции "Вывод заметок на экран"
def display_notes(notes):
    if len(notes) ==0:
        print('У вас нет сохранённых заметок.')
    else:
        print('Список заметок:\n------------------------------')
        for i in range(len(notes)):
            for key , value in notes[i].items():
                print(key, ':', value)
            print("-------------------------------------")

# Определение функции "Обновление заметок"
def update_note(note):
    print(f'Текущие данные заметки: {note}')
    while True:
        a = input('Какие данные вы хотите обновить? (username, title, content, status, issue_date): ')
        if a == 'username':
            note['username'] = input(f"Введите новое значение для поля 'username': ")
            print(f"Заметка обновлена:\n{note}")
        elif a == 'title':
            note['title'] = input(f"Введите новое значение для поля 'title': ")
            print(f"Заметка обновлена:\n{note}")
        elif a == 'title':
            note['content'] = input(f"Введите новое значение для поля 'content': ")
            print(f"Заметка обновлена:\n{note}")
        elif a == 'title':
            note['status'] = input(f"Введите новое значение для поля 'status' (новая, в процессе, выполнена): ")
            statuses = ['выполнено', 'в процессе', 'отложено']
            while True:
                if note['status'] in statuses:
                    break
                else:
                    note['status'] = input('Такого статуса не существует, введите существующий статус заметки: ')
            print(f"Заметка обновлена:\n{note}")
        elif a == 'issue_date':
            while True:
                try:
                    note['issue_date'] = input(f"Введите новое значение для поля 'issue_date' в формате - день-месяц-год: ")
                    if datetime.strptime(note['issue_date'], "%d-%m-%Y"):
                        print(f"Заметка обновлена:\n{note}")
                        break
                except ValueError:  # обработка ошибки ввода формата
                    print("Формат даты некорректен. Необходимо вводить 'issue_date' в требуемом формате - 'день-месяц-год.'")

# Определение функции "Удаление заметок"
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

# Определение функции поиска заметок
def search_notes(notes, keyword=None, status=None):
    if len(notes) == 0:
        print("\nСписок заметок пуст.\nПоиск невозможен.")
        return
# выполняется условие при отсутствии Ключевого слова и Статуса
    if keyword is None and status is None:
        print("\nКлючевое слово и/или Статус не введены.\nПоиск завершен.")
# выполняется поиск при наличии Ключевого слова и отсутствии Статуса
    elif keyword != None and status is (None or ''):
        j = 0 # счетчик найденных заметок
        for i in range(len(notes)):
            cur_values = list(notes[i].values()) # значения словаря i заносим во временный список(cur_values)
            for k in range(len(cur_values)): # цикл проверки наличия Ключевого слова во временном списке
                if keyword in cur_values[k]:  # проверка наличия Ключевого слова в элементе 'к' временного списка
                    j += 1
                    if j == 1:
                        print(f"\nПо Ключевому слову - '{keyword}' найдены заметки:")
                        print(f"Заметка{j}.")
                    else:
                        print(f"Заметка{j}.")
                    for key, value in notes[i].items():
                        print(key, "-", value)
        if j == 0: # Вывод на экран сообщения об отсутствии в заметках введенного Ключевого слова
            print("Заметки, соответствующие запросу, не найдены.")
# выполняется поиск при отсутствии Ключевого слова и наличии Статуса
    elif keyword is (None or '') and status != None:
        j = 0 # счетчик найденных заметок
        for i in range(len(notes)):
            if status == notes[i].get('status'): # проверка Статуса во временном списке
                j += 1
                if j == 1:
                    print(f"\nПо Статусу - '{status}' найдены заметки:")
                    print(f"Заметка{j}.")
                else:
                    print(f"Заметка{j}.")
                for key, value in notes[i].items():
                    print(key, "-", value)
        if j == 0: # Вывод на экран сообщения об отсутствии в заметках введенного Статуса
            print("Заметки, соответствующие запросу, не найдены.")
# выполняется поиск при одновременном наличии Ключевого слова и Статуса
    else:
        j = 0 # счетчик найденных заметок
        for i in range(len(notes)):
            cur_values = list(notes[i].values()) # значения словаря i заносим во временный список - cur_values
            for k in range(len(cur_values)): # цикл проверки наличия Ключевого слова во временном списке
                if keyword in cur_values[k] and status == notes[i].get('status'): # проверка Ключевого слова в элементе 'к' временного списка и Статуса в словаре notes[i]
                    j += 1
                    if j == 1:
                        print(f"\nПо Ключевому слову - '{keyword}' и Статусу - '{status}' найдены заметки:")
                        print(f"Заметка{j}.")
                    else:
                        print(f"Заметка{j}.")
                    for key, value in notes[i].items():
                        print(key, "-", value)

        if j == 0:# Вывод на экран сообщения об отсутствии в заметках введенных Ключевого слова и Статуса
            print("Заметки, соответствующие запросу, не найдены.")

notes = []

# Программа Меню действий
while True:
    print('Меню действий:')
    print('1. Создать новую заметку')
    print('2. Показать все заметки')
    print('3. Обновить заметку')
    print('4. Удалить заметку')
    print('5. Найти заметки')
    print('6. Выйти из программы')
    x = input('Введите номер действия: ')
    if x == 1: # Создание заметки
        create_note()
    elif x == 2: # Вывод заметок на экран
        display_notes(notes)
    elif x == 3:  # Обновить заметку
        index_note = input("\nВведите номер обновляемой заметки (пустой ввод - окончание обновления): ")
        if index_note.strip() != "":
            update_note(notes[int(index_note.strip()) - 1])
        else:
            print("\nОбновление завершено.")
    elif x == 4: # Удаление заметок
        delete_note(notes)
    elif x == 5: # Поиск заметок
        search_notes(notes, keyword=input('Введите ключевое слово: '), status=input('Введите статус: '))
    elif x == 6:
        print('Программа завершена. Спасибо за использование!')
        break
    else: print('Неверный выбор. Пожалуйста, выберите действие из списка.')