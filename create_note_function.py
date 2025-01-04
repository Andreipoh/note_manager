from datetime import date
def create_note():
    a = input('Введите имя пользователя: ')
    b = input('Введите заголовок заметки: ')
    c = input('Введите описание заметки: ')
    d = input('Введите статус заметки (новая, в процессе, выполнено): ')
    e = date.today()
    f = input('Введите дедлайн (день-месяц-год): ')
    print( { 'username': a, 'title': b, 'content': c, 'status': d, 'created_date ': e, 'issue_date': f })
create_note()
print()