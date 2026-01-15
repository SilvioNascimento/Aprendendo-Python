# TODO: Crie uma classe UsuarioTelefone.  
# TODO: Defina um método especial `__init__`, que é o construtor da classe.
# O método `__init__`, irá inicializar os atributos da classe: `nome`, `numero` e `plano`.
class UsuarioTelefone:
    def __init__(self, nome, numero_telefone, plano):
        self._nome = nome
        self._numero_telefone = numero_telefone
        self._plano = plano

    @property
    def nome(self):
        return self._nome

    @property
    def numero_telefone(self):
        return self._numero_telefone

    @property
    def plano(self):
        return self._plano

        # TODO: Aplique o conceito de encapsulamento, onde os atributos serão encapsulados dentro da classe.
        # A classe `UsuarioTelefone` define um método especial `__str__`, que retorna uma representação em string do objeto.

    def __str__(self):
        return f"Usuário {self.nome} criado com sucesso."


# Entrada:
nome = input()
numero = input()
plano = input()

usuario = UsuarioTelefone(nome, numero, plano)
# TODO: Crie um novo objeto `UsuarioTelefone` com os dados fornecidos:

print(usuario.__str__)