def calcular(operacao):
    def somar(a, b):
        return a + b

    def subtrair(a, b):
        return a - b

    def multiplicar(a, b):
        return a * b

    def dividir(a, b):
        return a / b

    def dividir_exato(a, b):
        return a // b

    match operacao:  # match: tem a mesma funcionalidade de um switch em Java
        case "+":
            return somar
        case "-":
            return subtrair
        case "*":
            return multiplicar
        case "/":
            return dividir
        case "//":
            return dividir_exato


resultado1 = calcular("+")(1, 3)
print(resultado1)
resultado2 = calcular("-")(1, 3)
print(resultado2)
resultado3 = calcular("*")(2, 3)
print(resultado3)
resultado4 = calcular("/")(1, 3)
print(resultado4)
resultado5 = calcular("//")(6, 3)
print(resultado5)
