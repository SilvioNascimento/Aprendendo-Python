from time import sleep


class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print(f"Ligando o motor de {self.__class__.__name__}...")
        sleep(2)
        print("Motor ligado")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


class Motocicleta(Veiculo):
    pass


class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado):
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado

    def estah_carregado(self):
        print(f"{'Sim,' if self.carregado else 'Não'} estou carregado")


class Carro(Veiculo):
    pass


moto = Motocicleta("Vermelho", "MLF-1608", 2)
moto.ligar_motor()
print(moto)

carro = Carro("Preto", "OXR-7951", 4)
carro.ligar_motor()
print(carro)

caminhao = Caminhao("Marrom", "AXS-0923", 6, False)
caminhao.ligar_motor()
caminhao.estah_carregado()
print(caminhao)
