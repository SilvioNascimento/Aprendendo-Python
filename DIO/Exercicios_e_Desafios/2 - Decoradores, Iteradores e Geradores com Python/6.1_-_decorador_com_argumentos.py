def duplicar(func):
    def envelope(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)

    return envelope


@duplicar
def aprender(tecnologia):
    print(f"Estou apredendo {tecnologia}")


aprender("Python")
