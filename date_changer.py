day,month,year = input('Введите дату создания заметки в формате "день-месяц-год" "xx-xx-xxxx": ').split('-')
created_date = (f'{day}-{month}-{year}')
day,month,year = input('Введите дату истечения заметки в формате "день-месяц-год" "xx-xx-xxxx": ').split('-')
issue_date = (f'{day}-{month}-{year}')
print(f'Дату создания заметки {day}-{month}')
print(f'Дату истечения заметки {day}-{month}')
