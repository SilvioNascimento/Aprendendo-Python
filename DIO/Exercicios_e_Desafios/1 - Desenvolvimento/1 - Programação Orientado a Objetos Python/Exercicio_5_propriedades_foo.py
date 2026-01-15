class Foo:
    def __init__(self, x=None):
        self._x = x

    @property   # Retorna o valor do atributo privado x
    def x(self):
        return self._x or 0

    @x.setter   # Possibilita alterar o valor do atributo privado x
    def x(self, valor):
        _x = self._x or 0
        _valor = valor or 0
        self._x = _x + _valor

    @x.deleter  # Possibilita de apagar o valor do atributo privado x ou alterar por um valor igual a zero
    def x(self):
        self._x = 0


foo = Foo(10)
print(foo.x)
foo.x = 11  # Somava o valor anterior com o novo informado e transformava o resultado no x do objeto Foo
print(foo.x)
del foo.x
print(foo.x)
