from datetime import  datetime

current_date = datetime.today()
print(f'Текущая дата: {current_date.strftime('%d-%m-%Y')}')

while True:
    issue_date = input('Введите дату дедлайна (в формате день-месяц-год "xx-xx-xxxx"): ')
    try:
        issue_date = datetime.strptime(issue_date,'%d-%m-%Y')
        break
    except ValueError:
        print('Неверный формат даты')
delta = issue_date - current_date
days_difference = delta.days*1
if delta == 1 :
    print("Дедлайн уже завтра!")
if 1 < days_difference < 5:
    print(f"До дедлайна осталось {days_difference} дня.")
if days_difference >= 5:
    print(f"До дедлайна осталось {days_difference} дней.")
if days_difference == -1:
    print(f"Внимание! Дедлайн истёк {-(days_difference)} день назад!")
if -1 > days_difference > -5:
    print(f"Внимание! Дедлайн истёк {-(days_difference)} дня назад!")
if days_difference <= -5:
    print(f"Внимание! Дедлайн истёк {-(days_difference)} дней назад!")
