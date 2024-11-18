import datetime

d1 = datetime.datetime.now()

# Formatando data e hora
print(d1.strftime("%d/%m/%Y %H:%M"))

# Convertendo string para datetime
date_string = "20/07/2023 15:30"
d = datetime.datetime.strptime(date_string, "%d/%m/%Y %H:%M")
print(d)
