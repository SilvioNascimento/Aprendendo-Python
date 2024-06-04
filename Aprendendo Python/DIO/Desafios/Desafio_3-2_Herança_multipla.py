class Animal:
    def __init__(self, numero_patas):
        self.numero_patas = numero_patas

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join(f'{chave}={valor}' for chave, valor in self.__dict__.items())}"


class Mamifero(Animal):
    def __init__(self, cor_do_pelo,
                 **kwargs):  # **kwargs = é usado para inserir atributos da classe Pai na classe filho
        super().__init__(**kwargs)
        self.cor_do_pelo = cor_do_pelo


class Ave(Animal):
    def __init__(self, cor_do_bico, **kwargs):
        super().__init__(**kwargs)
        self.cor_do_bico = cor_do_bico


class Gato(Mamifero):
    def __init__(self, numero_patas, cor_do_pelo):
        super().__init__(numero_patas=numero_patas, cor_do_pelo=cor_do_pelo)


class Cachorro(Mamifero):
    pass


class Leao(Mamifero):
    pass


class Falar:
    def falar(self):
        return f"{self.__class__.__name__}: Oi, estou falando por aqui!"


class Ornitorrinco(Ave, Mamifero, Falar):
    def __init__(self, numero_patas, cor_do_pelo, cor_do_bico):
        # print(Ornitorrinco.__mro__) -> responsável por ver as classes que estão acima da classe Ornitorrinco
        super().__init__(numero_patas=numero_patas, cor_do_pelo=cor_do_pelo, cor_do_bico=cor_do_bico)


gato = Gato(4, "Branco")
print(gato)

ornitorrinco = Ornitorrinco(2, "Vermelho", "Laranja")
print(ornitorrinco)
print(ornitorrinco.falar())
