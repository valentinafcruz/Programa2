import random
def rolar_dados(n):
    dados = []
    i = 0
    while i < n:
        dado = random.randint(1, 6)
        dados.append(dado)
        i += 1
    return dados

def guardar_dado(dados_rolados, dados_guardados, dado_p_guardar):
    novos_dados_rolados = []
    i = 0
    while i < len(dados_rolados):
        if i == dado_p_guardar:
            dados_guardados.append(dados_rolados[i])
        else:
            novos_dados_rolados.append(dados_rolados[i])
        i += 1
    return [novos_dados_rolados, dados_guardados]