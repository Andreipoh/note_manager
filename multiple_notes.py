# Запрашиваем и вводим данные по заметкам
print('Добро пожаловать в "Менеджер заметок"! Вы можете добавить новую заметку.')
notes = [] # создаем список для заметок
n = 0

while True:
    username = input('Введите имя пользователя: ')
    title = input('Введите заголовок заметки: ')
    content = input('Введите описание заметки: ')
    status = input('Введите статус заметки (новая, в процессе, выполнено): ')
    created_date = input('Введите дату создания (день-месяц-год): ')
    issue_date = input('Введите дедлайн (день-месяц-год): ')
    note = {f'Заметка № {1+n}.' 'Имя': username, 'Заголовок': title, 'Описание': content, 'Статус': status, 'Дата создания': created_date, 'Дедлайн': issue_date } # создаем словарь для ввода заметки
    notes.append(note) #добавляем заметку в список
    n = n + 1
    i = input('Хотите добавить ещё одну заметку? (да/нет): ')
    if i == 'нет':
        break # выход из цикла
# Вывод введенных заметок на экран
for note in notes:
    for key in note:
        print(key,note[key])
