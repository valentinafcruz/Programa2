import random
def rolar_dados(n):
    dados = []
    i = 0
    while i < n:
        dado = random.randint(1, 6)
        dados.append(dado)
        i += 1
    return dados