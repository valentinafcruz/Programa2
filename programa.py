
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
    dados_guardados = funcoes.guardar_dado(dados_rolados, dados_guardados, dado_p_guardar)
 
    print(f"Dados rolados: {dados_rolados}")
    print(f"Dados guardados: {dados_guardados}")
    pergunta1 = int(input("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:"))

    if pergunta1 == 1:
        pp1 = input("Digite o índice do dado a ser guardado (0 a 4):")
        dados_guardados.append(dados_rolados[pp1])
        continue
        
    if pergunta1 == 2:
        
        continue
    if pergunta1 == 3:
        
        continue
    if pergunta1 == 4:

        continue
    if pergunta1 == 0:

        continue 
