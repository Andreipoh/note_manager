from datetime import date

day,month,year = input('Введите дату дедлайна (в формате день-месяц-год "xx-xx-xxxx"): ').split('-')
issue_date = (f'{day}-{month}-{year}')
year1, month1, day1= str(date.today()).split('-')
print(day1,month1,year1)
if ((int(day1) > int(day) and int(month1) == int(month) and int(year1) == int(year)) or
    (int(day1) == int(day) and int(month1) > int(month) and int(year1) == int(year)) or
    (int(day1) == int(day) and int(month1) == int(month) and int(year1) > int(year)) or
    (int(day1) > int(day) and int(month1) > int(month) and int(year1) == int(year)) or
    (int(day1) == int(day) and int(month1) > int(month) and int(year1) > int(year)) or
    (int(day1) > int(day) and int(month1) == int(month) and int(year1) > int(year)) or
    (int(day1) > int(day) and int(month1) > int(month) and int(year1) > int(year))
) :
    print(f"Внимание! Дедлайн истёк {(int(day1) - int(day))+((int(month1) - int(month))*30)+((int(year1) - int(year))*365)} дня назад.")
else:
    print(f"До дедлайна осталось {(int(day) - int(day1))+((int(month) - int(month1))*30)+((int(year)-int(year1))*365)} дня.")
