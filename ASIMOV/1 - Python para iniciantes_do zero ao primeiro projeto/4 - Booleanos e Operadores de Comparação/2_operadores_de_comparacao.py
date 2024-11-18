# Este código é responsável por utilizar os operadores de comparação

perg1 = 3 > 2       # 3 é maior que 2? True
perg2 = 3 < 2       # 3 é menor que 2? False
perg3 = 2 >= 2      # 2 é maior ou igual a 2? True
perg4 = 2 <= 2      # 2 é menor ou igual a 2? True
perg5 = 2 != 2      # 2 é diferente de 2? False

print(f"3 é maior que 2? {perg1}")
print(f"3 é menor que 2? {perg2}")
print(f"2 é maior ou igual a 2? {perg3}")
print(f"2 é menor ou igual a 2? {perg4}")
print(f"2 é diferente de 2? {perg5}\n")


# and (e) / or (ou)
eTrue = (3 > 2) and (2 > 1)         # Retorna 'True'
eFalse1 = (3 > 2) and (2 < 1)       # Retorna 'False'
eFalse2 = (3 < 2) and (2 > 1)       # Retorna 'False'
eFalse3 = (3 < 2) and (2 < 1)       # Retorna 'False'

print(f"(3 > 2) and (2 > 1): {eTrue}")
print(f"(3 > 2) and (2 < 1): {eFalse1}")
print(f"(3 < 2) and (2 > 1): {eFalse2}")
print(f"(3 < 2) and (2 < 1): {eFalse3}\n")


ouTrue1 = (2 <= 2) or (2 >= 2)      # Retorna 'True'
ouTrue2 = (2 < 2) or (2 >= 2)       # Retorna 'True'
ouTrue3 = (2 <= 2) or (2 > 2)       # Retorna 'True'
ouFalse = (2 < 2) or (2 > 2)        # Retorna 'False'

print(f"(2 <= 2) or (2 >= 2): {ouTrue1}")
print(f"(2 < 2) or (2 >= 2): {ouTrue2}")
print(f"(2 <= 2) or (2 > 2): {ouTrue3}")
print(f"(2 < 2) or (2 > 2): {ouFalse}")
