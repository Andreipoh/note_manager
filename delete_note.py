notes=[{'Имя': 'Алексей', 'Заголовок': 'Список покупок', 'Описание': 'Купить продукты на неделю'}, {'Имя': 'Мария', 'Заголовок': 'Учеба', 'Описание': 'Подготовиться к экзамену'}]
for note in notes:
    for key in note:
        print(key,note[key])
a = input('Введите имя пользователя или заголовок для удаления заметки: ')
for i in reversed(range(len(notes))):
    if (notes[i]['Имя'] == a) or (notes[i]['Заголовок'] == a):
        del notes[i]

print('Успешно удалено. Остались следующие заметки:')
for note in notes:
    for key in note:
        print(key, note[key])
