class Estudante:
    escola = "DIO"

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self) -> str:
        return f"{self.nome} - {self.matricula} - {self.escola}"


def mostrar_valores(*objs):
    for obj in objs:
        print(obj)


estudante1 = Estudante("Guilherme", 1)
estudante2 = Estudante("Giovanna", 2)

mostrar_valores(estudante1, estudante2)

Estudante.escola = "UFPB"
estudante3 = Estudante("Arthur", 3)
mostrar_valores(estudante1, estudante2, estudante3)
