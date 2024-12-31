import datetime as dt
def normalize_date(date_str):
    return date_str.replace(".", "-").replace("/", "-")

issue_date_str = normalize_date(input('Введите дату истечения заметки в формате "день-месяц-год" "xx-xx-xxxx": '))
create_date = dt.datetime.now().strftime("%d-%m-%Y")
create_date = dt.datetime.strptime(create_date, "%d-%m-%Y")
issue_date  = dt.datetime.strptime(issue_date_str, "%d-%m-%Y")
if issue_date >= create_date:
    print(f"Внимание! Дедлайн истёк {issue_date - create_date} дня назад.")
else:
    print(f"До дедлайна осталось {create_date - issue_date} дня.")