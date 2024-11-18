class UsuarioTelefone:
    # Planos disponíveis
    PLANOS = ["Plano Essencial Fibra", "Plano Prata Fibra", "Plano Premium Fibra"]

    def __init__(self, nome, numero_telefone, plano):
        self._nome = nome
        self._numero_telefone = numero_telefone
        self._plano = plano if plano in UsuarioTelefone.PLANOS else "Plano Essencial Fibra"

    # Métodos getters
    @property
    def nome(self):
        return self._nome

    @property
    def numero_telefone(self):
        return self._numero_telefone

    @property
    def plano(self):
        return self._plano

    # Métodos setters
    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @numero_telefone.setter
    def numero_telefone(self, numero_telefone):
        self._numero_telefone = numero_telefone

    @plano.setter
    def plano(self, plano):
        if plano in UsuarioTelefone.PLANOS:
            self._plano = plano
        else:
            raise ValueError(f"Plano inválido. Planos disponíveis: {', '.join(UsuarioTelefone.PLANOS)}")

    def __str__(self):
        return f"Usuário {self.nome} criado com sucesso."


# Exemplo de uso
nome = input()
numero = input()
plano = input()

usuario = UsuarioTelefone(nome, numero, plano)
print(usuario)

"""
Desafio
Vamos criar uma classe chamada UsuarioTelefone para representar um usuário de telefone. Você pode definir um método especial e depois aplicar conceitos de encapsulamento nos atributos dentro da classe. Lembre-se que, cada usuário terá um nome, um número de telefone e um plano associado, neste desafio, simulamos três planos, sendo: Plano Essencial Fibra, Plano Prata Fibra e Plano Premium Fibra.

Entrada
Nome do usuário, número de telefone e plano.

Saída
Mensagem indicando que o usuário foi criado com sucesso.
"""
