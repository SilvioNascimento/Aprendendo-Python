"""
Excreva um programa que converta uma temperatura digitada em 'C' (Celsius) em 'F' (Fahrenheit).
A fórmula para essa conversão é:

    F = ((9 * C)/5) + 32
"""

celsius = float(input("Digite a temperatura em Celsius: "))

converter_para_fahrenheit = ((9 * celsius)/5) + 32

print(f"\nCelsius: \t\t{celsius:.1f}ºC\nFahrenheit: \t{converter_para_fahrenheit:.1f}ºF")
