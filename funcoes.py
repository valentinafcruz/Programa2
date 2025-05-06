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
    if A >= 1 and B >= 1 and C >= 1 and D >= 1:
        return 15
    if E >= 1 and B >= 1 and C >= 1 and D >= 1:
        return 15
    if E >= 1 and F >= 1 and C >= 1 and D >= 1:
        return 15
    else: 
        return 0

def calcula_pontos_sequencia_alta(dados_rolados):
    A = dados_rolados.count(1)
    B = dados_rolados.count(2)
    C = dados_rolados.count(3)
    D = dados_rolados.count(4)
    E = dados_rolados.count(5)
    F = dados_rolados.count(6)
    if A >= 1 and B >= 1 and C >= 1 and D >= 1 and E >= 1:
        return 30
    if E >= 1 and F >= 1 and C >= 1 and D >= 1 and B >= 1:
        return 30
    else: 
        return 0

def calcula_pontos_full_house(dados_rolados):
    A = dados_rolados.count(1)
    B = dados_rolados.count(2)
    C = dados_rolados.count(3)
    D = dados_rolados.count(4)
    E = dados_rolados.count(5)
    F = dados_rolados.count(6)
    if A == 3 or B == 3 or C == 3 or D == 3 or E == 3 or F == 3:
        if A == 2 or B == 2 or C == 2 or D == 2 or E == 2 or F == 2:
            soma = 0
            for num in dados_rolados:
                soma += num
            return soma
    return 0

def calcula_pontos_quadra(dados_rolados):
    A = dados_rolados.count(1)
    B = dados_rolados.count(2)
    C = dados_rolados.count(3)
    D = dados_rolados.count(4)
    E = dados_rolados.count(5)
    F = dados_rolados.count(6)
    if A >= 4 or B >= 4 or C >= 4 or D >= 4 or E >= 4 or F >= 4:
            soma = 0
            for num in dados_rolados:
                soma += num
            return soma
    return 0

def calcula_pontos_quina(dados_rolados):
    A = dados_rolados.count(1)
    B = dados_rolados.count(2)
    C = dados_rolados.count(3)
    D = dados_rolados.count(4)
    E = dados_rolados.count(5)
    F = dados_rolados.count(6)
    if A >= 5 or B >= 5 or C >= 5 or D >= 5 or E >= 5 or F >= 5:
            return 50
    return 0

def calcula_pontos_regra_avancada(dados_rolados):
    dic = {
    'cinco_iguais': calcula_pontos_quina(dados_rolados),
    'full_house': calcula_pontos_full_house(dados_rolados),
    'quadra': calcula_pontos_quadra(dados_rolados),
    'sem_combinacao': calcula_pontos_soma(dados_rolados),
    'sequencia_alta': calcula_pontos_sequencia_alta(dados_rolados),
    'sequencia_baixa': calcula_pontos_sequencia_baixa(dados_rolados)
    }
    return dic

def faz_jogada(dados, categoria, cartela):
    simples = calcula_pontos_regra_simples(dados)
    avancada = calcula_pontos_regra_avancada(dados)
    if categoria in simples:
        categoriaint = int(categoria)
        cartela['regra_simples'][categoriaint] = simples[categoriaint]
    else:
        cartela['regra_avancada'][categoria] = avancada[categoria]
    return cartela

def imprime_cartela(cartela):
    print("Cartela de Pontos:")
    print("-"*25)    
    for i in range(1, 7):
        filler = " " * (15 - len(str(i)))
        if cartela['regra_simples'][i] != -1:
            print(f"| {i}: {filler}| {cartela['regra_simples'][i]:02} |")
        else:
            print(f"| {i}: {filler}|    |")
    for i in cartela['regra_avancada'].keys():
        filler = " " * (15 - len(str(i)))
        if cartela['regra_avancada'][i] != -1:
            print(f"| {i}: {filler}| {cartela['regra_avancada'][i]:02} |")
        else:
            print(f"| {i}: {filler}|    |")
    print("-"*25)