

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