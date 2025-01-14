titles = []
while True:
    title = input('Введите заголовок (или оставьте пустым для завершения): ')
    titles.append(title)
    if title == 'стоп':
        break
    if title == '':
        break

print(titles)

