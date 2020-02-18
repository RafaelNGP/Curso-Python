from datetime import date, time, datetime, timedelta

print(timedelta(days=365, hours=5, minutes=1))

now = datetime.now()
print(f"Today is {now}")

print(f"One year from now it will be: {str(now + timedelta(days=365))}")
print(f"in 2 days and 3 weeks it will be: {str(now + timedelta(days=2, weeks=3))}")

t = datetime.now() - timedelta(weeks=1)
s = t.strftime("%A %B %d, %Y")
print(print(f"One week ago it was {s}"))

today = date.today()
afd = date(today.year, 4, 1)

if afd < today:
    print("April Fool's day already went by %d days ago" % (today-afd).days)
    afd = afd.replace(year=today.year+1)
    time_to_afd = afd-today
    print(f"Its just {time_to_afd.days} days until aprils fools day")
elif afd > today:
    print("Ainda vai chegar o Primeiro de Abril")
