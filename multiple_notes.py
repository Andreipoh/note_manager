print('Добро пожаловать в "Менеджер заметок"! Вы можете добавить новую заметку.')
notes = []
a = input('Введите имя пользователя: ')
b = input('Введите заголовок заметки: ')
c = input('Введите описание заметки: ')
d = input('Введите статус заметки (новая, в процессе, выполнено): ')
e = input('Введите дату создания (день-месяц-год): ')
f = input('Введите дедлайн (день-месяц-год): ')
name = {'Имя': a}
title = {'Заголовок': b}
content = {'Описание':c}
status = {'Статус':d}
create_date = {'Дата создания':e}
deadline_date = {'Дедлайн: ':f}
notes.append(name)
notes.append(title)
notes.append(content)
notes.append(status)
notes.append(create_date)
notes.append(deadline_date)
while True:
    i = input('Хотите добавить ещё одну заметку? (да/нет): ')
    if i == 'нет':
        break
    notes.append({input('введите ключ словаря: '):input('ввидите значение словаря: ')})
print(notes, sep='\n')