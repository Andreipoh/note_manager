import json

def save_notes_json(notes, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        j_file = json.dump(notes, file, indent=4, ensure_ascii=False)


notes = [
    {"username": "Алексей", "title": "Список покупок", "content": "Купить продукты", "status": "новая", "created_date": "27-11-2024", "issue_date": "30-11-2024"},
    {'username': 'Мария', 'title': 'Учеба', 'content': 'Подготовиться к экзамену', 'status': 'в процессе',
     'created_date': '25.11.2024', 'issue_date': '01.12.2024'}
]
save_notes_json(notes, 'json_file.json')
