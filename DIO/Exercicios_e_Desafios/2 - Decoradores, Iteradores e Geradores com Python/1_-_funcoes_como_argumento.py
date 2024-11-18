# Método de passar função como parametro - parte 1
def dizer_oi(nome):
    return print(f"Oi {nome}")


def incentivar_aprender(nome):
    return print(f"Oi {nome}, vamos aprender Python juntos!")


def mensagem_para_guilherme(funcao_mensagem):
    return funcao_mensagem("Guilherme")


mensagem_para_guilherme(dizer_oi)
mensagem_para_guilherme(incentivar_aprender)


# Método de passar função como parametro - parte 2
def mensagem(nome):
    print("Executando mensagem")
    return f"oi {nome}"


def mensagem_longa(nome):
    print("Executando mensagem longa")
    return f"Olá tudo bem com você {nome}?"


def executar(funcao, nome):
    print("Executando executar")
    return funcao(nome)


print(executar(mensagem, "Silvio"))
print(executar(mensagem_longa, "Silvio"))
