# Функция обновления заметки  Grade 1. Этап 3: Задание 2.
from datetime import date
# Определение функции обновления заметок
def update_note(note):
    a = input('Какие данные вы хотите обновить? (username, title, content, status, issue_date): ')
    if note[a]:
        b = input(f'Введите новое значение для {a}: ') #запрвшиваем новое значение
        note[a] = b
    print(note)

e = date.today()
note = {'username': 'Алексей', 'title': 'Список покупок', 'content': 'Купить продукты на неделю', 'status': 'новая', 'created_date ': f'{e.day}-{e.month}-{e.year}', 'issue_date': '30-11-2024'}
print(f'Текущие данные заметки: {note}')
update_note(note)
print()