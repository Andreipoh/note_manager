statuses = ['1. выполнено', '2. в процессе', '3. отложено']
current_status = input("Введите текущий статус заметки: ")
print(f"Текущий статус заметки: {current_status}")
while True:
    print("\n Возможные статусы:")
    for status in statuses:
        print(f" {status}")
    new_status = int(input("Ваш выбор: "))
    if new_status == 1 :
        current_status = statuses[0]
        print(f"Статус заметки обновлён на: {current_status}")
        break
    if new_status == 2:
        current_status = statuses[1]
        print(f"Статус заметки обновлён на: {current_status}")
        break
    if new_status == 3:
        current_status = statuses[2]
        print(f"Статус заметки обновлён на: {current_status}")
        break
    else:
        print("Некорректный статус. Пожалуйста, выберите из предложенных.")
print(f"\nОбновлённый статус заметки: {current_status}")