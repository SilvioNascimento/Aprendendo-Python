"""
Escreva uma expressão que será utilizada para decidir se um aluno foi ou não aprovado. Para ser aprovado, todas as
médias do aluno devem ser maiores que 7. Considere que o aluno cursa apenas três matérias, e que a nota de cada uma
está armazenada nas seguintes variáveis: materia1, materia2 e materia3
"""

media = 7.0
materia1 = float(input("Digite a média da 1ª matéria do aluno: "))
materia2 = float(input("Digite a média da 2ª matéria do aluno: "))
materia3 = float(input("Digite a média da 3ª matéria do aluno: "))

if(materia1 > media) and (materia2 > media) and (materia3 > media):
    print("O aluno está APROVADO!")
else:
    print("O aluno está REPROVADO!")
