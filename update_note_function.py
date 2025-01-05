from datetime import date
def update_note():
    e = date.today()
    note = {'username': 'Алексей', 'title': 'Список покупок', 'content': 'Купить продукты на неделю', 'status': 'новая', 'created_date ': f'{e.day}-{e.month}-{e.year}', 'issue_date': '30-11-2024'}
    print(f'Текущие данные заметки: {note}')
    a = input('Какие данные вы хотите обновить? (username, title, content, status, issue_date): ')
    if note[a]:
        b = input(f'Введите новое значение для {a}: ')
        note[a] = b
    print(note)
update_note()
print()