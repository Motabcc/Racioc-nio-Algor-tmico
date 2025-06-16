import random

def analisar_matriz_quadrada():
    DIMENSAO = 4
    matriz = [[random.randint(1, 50) for _ in range(DIMENSAO)] for _ in range(DIMENSAO)]
    maiores_valores = [0] * DIMENSAO

    for j in range(DIMENSAO):
        maior_da_coluna = matriz[0][j]
        for i in range(1, DIMENSAO):
            if matriz[i][j] > maior_da_coluna:
                maior_da_coluna = matriz[i][j]
        maiores_valores[j] = maior_da_coluna

    media = sum(maiores_valores) / DIMENSAO

    print("Matriz:")
    for linha in matriz:
        print(linha)

    print("\nMaiores valores de cada coluna:")
    print(maiores_valores)

    print(f"\nMédia: {media}")

def multiplicar_matriz_por_numero():
    LINHAS = 3
    COLUNAS = 3
    matriz = []

    print("Vamos criar sua matriz 3x3. Por favor, insira os números.")
    for i in range(LINHAS):
        linha_atual = []
        for j in range(COLUNAS):
            while True:
                try:
                    elemento = int(input(f"Digite o número para a posição ({i+1}, {j+1}): "))
                    linha_atual.append(elemento)
                    break
                except ValueError:
                    print("Isso não é um número. Tente novamente.")
        matriz.append(linha_atual)

    while True:
        try:
            numero_multiplicador = int(input("\nPor Qual número você gostaria de multiplicar  "))
            break
        except ValueError:
            print("Por favor, digite um número válido.")

    matriz_resultado = [[0 for _ in range(COLUNAS)] for _ in range(LINHAS)]

    for i in range(LINHAS):
        for j in range(COLUNAS):
            matriz_resultado[i][j] = matriz[i][j] * numero_multiplicador

    print("\nMatriz original:")
    for linha in matriz:
        print(linha)

    print("\nResultado da mult:")
    for linha in matriz_resultado:
        print(linha)


def analisar_matriz_unica_humanizado():
    DIMENSAO = 4
    QUANTIDADE_NUMEROS = DIMENSAO * DIMENSAO
    
    print("Matriz 4x4 :")
    
    numeros_possiveis = range(100, 1000)
    numeros_sorteados = random.sample(numeros_possiveis, QUANTIDADE_NUMEROS)
    
    matriz = []
    for i in range(DIMENSAO):
        linha = numeros_sorteados[i*DIMENSAO : (i+1)*DIMENSAO]
        matriz.append(linha)
        
    maior_elemento = -1
    linha_do_maior = -1
    
    for i in range(DIMENSAO):
        for j in range(DIMENSAO):
            if matriz[i][j] > maior_elemento:
                maior_elemento = matriz[i][j]
                linha_do_maior = i
                
    menor_da_linha = min(matriz[linha_do_maior])
    
    print("\nM:")
    for linha in matriz:
        for numero in linha:
            print(f"{numero:^5}", end="")
        print()


    print(f"\nO maior número é o {maior_elemento}.\nNa mesma linha dele, o menor número que encontrei foi o {menor_da_linha}.")

import random

def analisar_figura_cruz():#primeira fig
    DIMENSAO = 5
    matriz = [[random.randint(10, 99) for _ in range(DIMENSAO)] for _ in range(DIMENSAO)]

    print("--- Matriz Original (5x5) ---")
    for linha in matriz:
        for numero in linha:
            print(f"{numero:^5}", end="")
        print()

    print("\n--- Analisando a Figura em formato de Cruz ---")
    soma_hachurada = 0
    for i in range(DIMENSAO):
        for j in range(DIMENSAO):
            if i == 2 or j == 2:#so alterar aqui
                print(f"{matriz[i][j]:^5}", end="")
                soma_hachurada += matriz[i][j]
            else:
                print(f"{' ':^5}", end="")
        print()

    print(f"\nA soma dos números na área destacada é: {soma_hachurada}")



def ordenar_matriz_por_paridade():
    LINHAS = 15
    COLUNAS = 7
    
    matriz = [[random.randint(10, 99) for _ in range(COLUNAS)] for _ in range(LINHAS)]

    print("--- Matriz Original (15x7) ---")
    for linha in matriz:
        for numero in linha:
            print(f"{numero:^5}", end="")
        print()


    numeros_pares = []
    numeros_impares = []

    for linha in matriz:
        for numero in linha:
            if numero % 2 == 0:
                numeros_pares.append(numero)
            else:
                numeros_impares.append(numero)

    numeros_ordenados = numeros_pares + numeros_impares

    matriz_modificada = []
    contador = 0
    for i in range(LINHAS):
        nova_linha = []
        for j in range(COLUNAS):
            nova_linha.append(numeros_ordenados[contador])
            contador += 1
        matriz_modificada.append(nova_linha)

    print("\n--- Matriz Modificada (Pares primeiro, depois Ímpares) ---")
    for linha in matriz_modificada:
        for numero in linha:
            print(f"{numero:^5}", end="")
        print()

def calcular_tempo_viagem():
    cidades = {
        "Curitiba": 0,
        "Florianopolis": 1,
        "Porto Alegre": 2,
        "Sao Paulo": 3,
        "Rio de Janeiro": 4
    }
    distancias = [
        [0, 310, 716, 408, 852],
        [310, 0, 470, 705, 1144],
        [716, 470, 0, 1119, 1553],
        [408, 705, 1119, 0, 429],
        [852, 1144, 1553, 429, 0]
    ]


    print("Cidades disponíveis:", ", ".join(cidades.keys()))
    cidade_origem = input("Digite a cidade de origem: ")
    cidade_destino = input("Digite a cidade de destino: ")
    velocidade_media = float(input("Digite a velocidade média em km/h: "))

    # Cálculo e exibição do resultado
    idx_origem = cidades[cidade_origem]
    idx_destino = cidades[cidade_destino]
    distancia = distancias[idx_origem][idx_destino]
    tempo_horas = distancia / velocidade_media

    print(f"O tempo de viagem entre {cidade_origem} e {cidade_destino} é de aproximadamente {tempo_horas:.2f} horas.")
