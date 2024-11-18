import functools


def duplicar(func):
    @functools.wraps(func)
    def envelope(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)

    return envelope


@duplicar
def aprender(tecnologia):
    print(f"Estou apredendo {tecnologia}")


aprender("Python")
print(aprender.__name__)
