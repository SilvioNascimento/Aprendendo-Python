"""João tem uma bicicletaria e gostaria de registrar as vendas das suas bicicletas. Crie um programa onde João
informe: cor, modelo, ano e valor da bicicleta vendida. Uma bicicleta pode: buzinar, parar e correr. Adicione esses
comportamentos."""


class Bicicleta:

    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("Ponk, pooonk!")

    def parar(self):
        print("Tieeeeerrrr!")
        print("Bicicleta parada")

    def correr(self):
        print("Vruuuuuum!")

    def get_cor(self):
        return self.cor

    def get_modelo(self):
        return self.modelo

    def get_ano(self):
        return self.ano

    def get_valor(self):
        return self.valor



    # def __str__(self):  # É o mesmo que o toString de Java, mostra os conteúdos do objeto em String
    #     return f"Cor: {self.cor}\tModelo: {self.modelo}\tAno: {self.ano}\tValor: R${self.valor:.2f}"

    def __str__(self):  # Mostra o nome da classe
                                            # Irá criar um dicionário com a chave (nome de cada atributo) e seus
                                            # valores (valor de cada atributo) e inserí-los em uma lista
        return f"{self.__class__.__name__}: {', '.join(f'{chave}={valor}' for chave, valor in self.__dict__.items())}"


bicicleta_1 = Bicicleta("Preto", "Mountain Bike", 2020, 1200.50)
bicicleta_2 = Bicicleta("Vermelho", "Cross-Country", 2019, 1135.90)

bicicleta_1.buzinar()
bicicleta_2.parar()
bicicleta_1.correr()

print(bicicleta_1.get_cor(), bicicleta_1.get_modelo(), bicicleta_1.get_ano(), bicicleta_1.get_valor())

print(bicicleta_1.__str__())
