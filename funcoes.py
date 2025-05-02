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

def remover_dado(dados_rolados, dados_guardados, dado_p_remover):
    dados_rolados.append(dados_guardados[dado_p_remover])
    novos_dados_guardados = []
    i = 0
    while i < len(dados_guardados):
        if i != dado_p_remover:
            novos_dados_guardados.append(dados_guardados[i])
        i += 1
    return [dados_rolados, novos_dados_guardados]

def calcula_pontos_regra_simples(dados_rolados):
    dicionario = {}
    for i in range(len(dados_rolados)):
        A = dados_rolados.count(1)
        B = dados_rolados.count(2)
        C = dados_rolados.count(3)
        D = dados_rolados.count(4)
        E = dados_rolados.count(5)
        F = dados_rolados.count(6)
        dicionario[1] = A
        dicionario[2] = B*2
        dicionario[3] = C*3
        dicionario[4] = D*4
        dicionario[5] = E*5
        dicionario[6] = F*6
    return dicionario

def calcula_pontos_soma(dados_rolados):
    X = 0
    for i in range(len(dados_rolados)):
        X += dados_rolados[i]
    return X

def calcula_pontos_sequencia_baixa(dados_rolados):
    A = dados_rolados.count(1)
    B = dados_rolados.count(2)
    C = dados_rolados.count(3)
    D = dados_rolados.count(4)
    E = dados_rolados.count(5)
    F = dados_rolados.count(6)
    if A > 1 and B > 1 and C > 1 and D > 1:
        return 15
    if E > 1 and B > 1 and C > 1 and D > 1:
        return 15
    if E > 1 and F > 1 and C > 1 and D > 1:
        return 15
    else: 
        return 0
