duration = int(input("Введите промежуток времени, в секундах"))
days = duration // 24 // 3600
hours = (duration - days * 24 * 60 * 60) // 3600
minutes = (duration - (days * 86400) + (hours * 3600)) //60
seconds = duration - ((days * 86400) + (hours * 60 * 60) + (minutes * 60))

if seconds > 0 and minutes == 0:
    print(f"Продолжительность времени {seconds} секунд")
elif minutes > 0 and hours == 0:
    print(f"Продолжительность времени {minutes} минут и {seconds} секунд")
elif hours > 0 and days == 0:
    print(f"Продолжительность времени {hours} часов , {minutes} минут и {seconds} секунд")
else:
    print(f"Продолжительность времени {days} дней {hours} часов {minutes} минут {seconds} секунд")