from datetime import datetime, timezone, timedelta

# Criando datetime com timezone
d = datetime.now(timezone(timedelta(hours=-3), "BRT"))

# Convertendo para outro timezone
d_utc = d.astimezone(timezone.utc)
print(d_utc)

data_tehran = datetime.now(timezone(timedelta(hours=3, minutes=30), "Tehran/Asia"))
data_sao_paulo = datetime.now(timezone(timedelta(hours=-3), "São Paulo/América"))

print(f"{data_tehran.tzname()}: {data_tehran}")
print(f"{data_sao_paulo.tzname()}: {data_sao_paulo}")
