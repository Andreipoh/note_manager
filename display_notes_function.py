# Функция отображения заметок. Grade 1. Этап 3: Задание 3.
def display_notes(notes):
    if len(notes) ==0:
        print('У вас нет сохранённых заметок.')
    else:
        print('Список заметок:')
        for i in range(len(notes)):
            print('------------------------------')
            for key , value in notes[i].items():
                print(key, ':', value)

# Тестовый список заметок:
notes=[{'Имя': 'Алексей', 'Заголовок': 'Список покупок', 'Описание': 'Купить продукты на неделю', 'Статус': 'новая', 'Дата создания': '27-11-2024', 'Дедлайн': '30-11-2024'},
       {'Имя': 'Мария', 'Заголовок': 'Учеба', 'Описание': 'Подготовиться к экзамену', 'Статус': 'в процессе', 'Дата создания': '25-11-2024', 'Дедлайн': '01-12-2024'}]
display_notes(notes)
print()

