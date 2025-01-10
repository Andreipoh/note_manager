# Функция поиска заметок     Grade 1. Этап 3: Задание 4

# Определение функции поиска заметок
def search_notes(notes, keyword=None, status=None):
    if len(notes) == 0:
        print("\nСписок заметок пуст.\nПоиск невозможен.")
        return
# выполняется условие при отсутствии Ключевого слова и Статуса
    if keyword is None and status is None:
        print("\nКлючевое слово и/или Статус не введены.\nПоиск завершен.")
# выполняется поиск при наличии Ключевого слова и отсутствии Статуса
    elif keyword != None and status is None:
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
    elif keyword is None and status != None:
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

# Исходный список заметок:
notes = [
    {'username': 'Алексей', 'title': 'Список покупок', 'content': 'Купить продукты на неделю', 'status': 'новая',
         'created_date': '27-11-2024', 'issue_date': '30-11-2024'},
        {'username': 'Мария', 'title': 'Учеба', 'content': 'Подготовиться к экзамену', 'status': 'в процессе',
         'created_date': '25-11-2024', 'issue_date': '01-12-2024'},
        {'username': 'Иван', 'title': 'План работы', 'content': 'Завершить проект', 'status': 'выполнено',
         'created_date': '20-11-2024', 'issue_date': '26-11-2024'}
]

search_notes(notes, keyword='покупок')
print()
search_notes(notes, status='в процессе')
print()
search_notes(notes, keyword='работы', status='выполнено')
print()