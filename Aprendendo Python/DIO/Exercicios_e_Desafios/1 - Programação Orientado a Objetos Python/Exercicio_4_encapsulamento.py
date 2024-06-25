class Conta:
    def __init__(self, numero_da_agencia, saldo=0):
        self.numero_da_agencia = numero_da_agencia
        self._saldo = saldo

    def mostrar_saldo(self):
        return self._saldo

    def depositar(self, valor):
        if valor < 0:
            print(f"Não é possível realizar um depósito com um valor negativo. Valor: {valor}")
        elif valor == 0:
            print("Não é possível realizar um depósito com um valor igual a zero")
        else:
            self._saldo += valor

    def sacar(self, valor):
        if valor < 0:
            print(f"Não é possível realizar um saque com um valor negativo. Valor: {valor}")
        elif valor == 0:
            print("Não é possível realizar um saque com um valor igual a zero")
        else:
            self._saldo -= valor


conta = Conta("047", 100)
print(conta.numero_da_agencia)
print(conta.mostrar_saldo())

# Irão falhar
conta.depositar(-100)
conta.depositar(0)
print(conta.mostrar_saldo())
conta.sacar(-50)
conta.sacar(0)
print(conta.mostrar_saldo(), end='\n\n')


# Irão passar
conta.depositar(100)
print(conta.mostrar_saldo())
conta.sacar(50)
print(conta.mostrar_saldo())
