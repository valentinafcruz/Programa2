import funcoes

cartela_de_pontos = {
    'regra_simples':  {
        1:-1,
        2:-1,
        3:-1,
        4:-1,
        5:-1,
        6:-1
    },
    'regra_avancada' : {
        'sem_combinacao':-1,
        'quadra': -1,
        'full_house': -1,
        'sequencia_baixa': -1,
        'sequencia_alta': -1,
        'cinco_iguais': -1
    }
}

funcoes.imprime_cartela(cartela_de_pontos)

for i in range(12):
    guardados =[]
    rerrolagens = 2
    dados_rolados = funcoes.rolar_dados(5)
    dados_guardados = funcoes.guardar_dado(dados_rolados, guardados,  )
