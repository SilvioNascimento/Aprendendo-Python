from abc import ABC, abstractmethod
from time import sleep


class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):    # Método abstrato
        pass

    @abstractmethod
    def desligar(self): # Método abstrato
        pass

    @property
    @abstractmethod
    def marca(self):
        pass


class ControleTV(ControleRemoto):
    def ligar(self):    # Método abstrato
        print("Ligando a TV...")
        sleep(1)
        print("Ligada!")

    def desligar(self): # Método abstrato
        print("Desligando a TV...")
        sleep(1)
        print("Desligada!")

    @property
    def marca(self):
        return "LG"


class ControleArCondicionado(ControleRemoto):
    def ligar(self):    # Método abstrato
        print("Ligando o Ar Condicionado...")
        sleep(1)
        print("Ligado!")

    def desligar(self): # Método abstrato
        print("Desligando o Ar Condicionado...")
        sleep(1)
        print("Desligado!")

    @property
    def marca(self):
        return "Samsung"


controle1 = ControleTV()
controle1.ligar()
controle1.desligar()
print(f"Marca do controle de TV: {controle1.marca}")

controle2 = ControleArCondicionado()
controle2.ligar()
controle2.desligar()
print(f"Marca do controle de Ar Condicionado: {controle2.marca}")
