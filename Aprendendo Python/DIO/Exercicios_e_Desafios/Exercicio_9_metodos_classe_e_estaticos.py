from datetime import date


class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade

    @classmethod    # Permite que este método crie uma instância da classe Pessoa, sem ser necessário chamá-lo novamente
    def criar_de_data_nascimento(cls, ano, mes, dia, nome):
        ano_atual = date.today().year
        idade = ano_atual - ano
        return cls(nome, idade)

    @staticmethod   # Permite que este método tratar os valores do atributo da classe Pessoa
    def eh_maior_de_idade(idade):
        return idade >= 18


p = Pessoa("Silvio", 22)
print(p.nome, p.idade)

p2 = Pessoa.criar_de_data_nascimento(1994, 3, 21, "Guilherme")  # Para usar o método de classe,
                                                                                    # deve-se colocar o nome da classe
                                                                                    # primeiro para depois chamar este
                                                                                    # método
print(p2.nome, p2.idade)

print(Pessoa.eh_maior_de_idade(p.idade))    # Para usar o método estático, deve-se colocar o nome da classe primeiro
                                            # para depois chamar este método
print(Pessoa.eh_maior_de_idade(p2.idade))
