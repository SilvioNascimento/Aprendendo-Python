from datetime import date


class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self._nome = nome
        self._ano_nascimento = ano_nascimento

    @property
    def nome(self):
        return self._nome

    @property
    def ano_nascimento(self):
        return self._ano_nascimento

    @property
    def idade(self):
        _ano_atual = date.today().year
        return _ano_atual - self._ano_nascimento

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    @ano_nascimento.setter
    def ano_nascimento(self, novo_ano_nascimento):
        self._ano_nascimento = novo_ano_nascimento


pessoa1 = Pessoa("Silvio Nascimento Ribeiro", 2002)
print(f"Nome completo: {pessoa1.nome}", end="\t\t")
print(f"Ano de nascimento: {pessoa1.ano_nascimento}", end="\t\t")
print(f"Idade: {pessoa1.idade}")
pessoa1.nome = "Arthur Sagaz"
print(f"Nome completo: {pessoa1.nome}", end="\t\t")
pessoa1.ano_nascimento = 1994
print(f"Ano de nascimento: {pessoa1.ano_nascimento}", end="\t\t")
print(f"Idade: {pessoa1.idade}")
