class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print("Iniciando a instância...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self):
        print("Removendo a instância...")

    def falar(self):
        print("Auau")


c = Cachorro("Zeus", "Branco e preto", False)
print(c.nome)

c.falar()

print("Olá, pessoal")
del c
print("Olá, pessoal")
print("Olá, pessoal")
