# Функция создания заметки
from datetime import date
def create_note():
    a = input('Введите имя пользователя: ')
    b = input('Введите заголовок заметки: ')
    c = input('Введите описание заметки: ')
    d = input('Введите статус заметки (новая, в процессе, выполнено): ')
    e = date.today() # Получаем автоматически текущую дату и помещаем её в словарь note как дату создания заметки
    f = input('Введите дедлайн (день-месяц-год): ')
    note = { 'username': a, 'title': b, 'content': c, 'status': d, 'created_date ': f'{e.day}-{e.month}-{e.year}', 'issue_date': f } # Создаем словарь для заметки
    print(note)
create_note()
print()