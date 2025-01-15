# Функция обновления заметки  Grade 1. Этап 3: Задание 2.
from datetime import date
from datetime import datetime
# Определение функции обновления заметок
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

e = date.today()
note = {'username': 'Алексей', 'title': 'Список покупок', 'content': 'Купить продукты на неделю', 'status': 'новая', 'created_date ': f'{e.day}-{e.month}-{e.year}', 'issue_date': '30-11-2024'}

update_note(note)
print()