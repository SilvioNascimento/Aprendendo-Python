from datetime import timedelta, datetime, date, time

tipo_carro = "P"
tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60
data_atual = datetime.now()
print(data_atual)

# tipo_carro = input("Qual é o tamanho do carro que quer pegar? [P/M/G] ").upper()    # P, M, G

if tipo_carro == "P":
    data_estimada = data_atual + timedelta(days=tempo_pequeno)
elif tipo_carro == "M":
    data_estimada = data_atual + timedelta(days=tempo_medio)
else:
    data_estimada = data_atual + timedelta(days=tempo_grande)

print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}")

print(date.today() - timedelta(weeks=1))

resultado = datetime.today() - timedelta(hours=2)
print(resultado)

print(datetime.now().date())
print(datetime.now().time())
