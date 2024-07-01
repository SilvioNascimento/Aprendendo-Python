import pytz
from datetime import datetime

timezone1 = "Asia/Tehran"
timezone2 = "America/Sao_Paulo"

d1 = datetime.now(pytz.timezone(timezone1))
print(f"Fuso horário de {timezone1.split('/')[1]}, {timezone1.split('/')[0]}: {d1}")

d2 = datetime.now(pytz.timezone(timezone2))
print(f"Fuso horário de {timezone2.split('/')[1]}, {timezone2.split('/')[0]}: {d2}")
