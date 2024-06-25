"""
Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário.
Calcule o total em segundos
"""

dias = int(input("Digite um valor em dias: "))
horas = int(input("Digite um valor em horas: "))
minutos = int(input("Digite um valor em minutos: "))
segundos = int(input("Digite um valor em segundos: "))

converter_dias_em_segundos = ((dias * 24) * 60) * 60
converter_horas_em_segundos = (horas * 60) * 60
converter_minutos_em_segundos = minutos * 60
total_de_segundos = converter_dias_em_segundos + converter_horas_em_segundos + converter_minutos_em_segundos + segundos

print(f"Total de segundos: {total_de_segundos}")
