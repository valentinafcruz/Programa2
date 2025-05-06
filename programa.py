
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

soma=0
funcoes.imprime_cartela(cartela_de_pontos) #printa a cartela vazia no início do jogo

simples =['1', '2', '3', '4', '5', '6']
avancado = ['sem_combinacao', 'quadra', 'full_house', 'sequencia_baixa', 'sequencia_alta', 'cinco_iguais']

for i in range(12): #12 rodadas do jogo
    guardados =[]
    rerrolagens = 2
    dados_rolados = funcoes.rolar_dados(5)
 
    print(f"Dados rolados: {dados_rolados}")
    print(f"Dados guardados: {guardados}")
    print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
    pergunta = input('>')
    while pergunta != '0':
        if pergunta == '1':
            print("Digite o índice do dado a ser guardado (0 a 4):")
            p1 = int(input('>'))
            guardar_dado = funcoes.guardar_dado(dados_rolados, guardados, p1)
            dados_rolados = guardar_dado[0]
            guardados = guardar_dado[1]
            print(f"Dados rolados: {dados_rolados}")
            print(f"Dados guardados: {guardados}")
        elif pergunta == '2':
            print("Digite o índice do dado a ser removido (0 a 4):")
            p2 = int(input('>'))
            remover_dado = funcoes.remover_dado(dados_rolados, guardados, p2)
            dados_rolados = remover_dado[0]
            guardados = remover_dado[1]   
            print(f"Dados rolados: {dados_rolados}")
            print(f"Dados guardados: {guardados}") 
        elif pergunta == '3':
            if rerrolagens == 0:
                print("Você já usou todas as rerrolagens.")
            else:
                rerrolagens -= 1
                n = 0
                for dado in dados_rolados:
                    n += 1
                dados_rolados = funcoes.rolar_dados(n) 
            print(f"Dados rolados: {dados_rolados}")
            print(f"Dados guardados: {guardados}")  
        elif pergunta == '4':
            funcoes.imprime_cartela(cartela_de_pontos)
            print(f"Dados rolados: {dados_rolados}")
            print(f"Dados guardados: {guardados}")
        else:
            print("Opção inválida. Tente novamente.")
    if pergunta != '0':
        print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
        pergunta = input('>')
    else:
        categoria_valida = False
        while not categoria_valida:
            print("Digite a combinação desejada:")
            categoria = input('>')
            if categoria in ['1', '2', '3', '4', '5', '6']:
                if cartela_de_pontos['regra_simples'][int(categoria)] == -1:
                    funcoes.faz_jogada(guardados + dados_rolados, categoria, cartela_de_pontos)
                    categoria_valida = True
                else:
                    print("Essa combinação já foi utilizada.")
            if categoria in ['sem_combinacao', 'quadra', 'full_house', 'sequencia_baixa', 'sequencia_alta', 'cinco_iguais']:
                if cartela_de_pontos['regra_avancada'][categoria] == -1:
                    funcoes.faz_jogada(guardados + dados_rolados, categoria, cartela_de_pontos)
                    categoria_valida = True
                else:
                    print("Essa combinação já foi utilizada.")
            if categoria not in ['1', '2', '3', '4', '5', '6'] and categoria not in ['sem_combinacao', 'quadra', 'full_house', 'sequencia_baixa', 'sequencia_alta', 'cinco_iguais']:
                print("Combinação inválida. Tente novamente.")

for pontos in cartela_de_pontos['regra_simples'].values():
    soma += pontos
if soma >= 63:
    soma += 35
for pontos in cartela_de_pontos['regra_avancada'].values():
    soma += pontos

funcoes.imprime_cartela(cartela_de_pontos)
print(f"Pontuação total: {soma}")