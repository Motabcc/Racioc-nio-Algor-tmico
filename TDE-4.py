import random

# 1
def tabela_de_multiplicacao_2_lacos():
    print("--- Exercício 1: Tabela de Multiplicação (2 Laços) ---")
    for i in range(1, 11):
        for j in range(1, 11):
            print(f"{i} x {j} = {i*j}")
        print("-" * 15)

# 2
def tabela_de_multiplicacao_1_laco():
    print("\n--- Exercício 2: Tabela de Multiplicação (1 Laço) ---")
    for i in range(1, 101):
        for j in range(1, 11):
            if i % j == 0 and i // j <= 10:
                print(f"{i//j} x {j} = {i}")

# 3
def verificar_soma():
    print("\n--- Exercício 3: Verificar Soma ---")
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))
    n3 = int(input("Digite o terceiro número: "))

    if n1 > n2 + n3:
        print("O primeiro número é maior que a soma dos outros dois.")
    else:
        print("O primeiro número não é maior que a soma dos outros dois.")

# 4
def operacoes_reais():
    print("\n--- Exercício 4: Operações com Números Reais ---")
    v1 = float(input("Digite o primeiro valor: "))
    v2 = float(input("Digite o segundo valor: "))

    print(f"Soma: {v1 + v2}")
    print(f"Produto: {v1 * v2}")
    if v2 != 0:
        print(f"Quociente: {v1 / v2}")
    else:
        print("Não é possível dividir por zero.")

# 5
def soma_pares():
    print("\n--- Exercício 5: Soma de Números Pares ---")
    soma = 0
    for i in range(4):
        num = int(input(f"Digite o {i+1}º número inteiro: "))
        if num % 2 == 0:
            soma += num
    print(f"A soma dos números pares é: {soma}")

# 6
def verificar_triangular():
    print("\n--- Exercício 6: Verificar Número Triangular ---")
    n = int(input("Digite um número inteiro não-negativo: "))
    i = 1
    while i * (i + 1) * (i + 2) < n:
        i += 1

    if i * (i + 1) * (i + 2) == n:
        print(f"{n} é triangular, pois {i} * {i+1} * {i+2} = {n}")
    else:
        print(f"{n} não é triangular.")

# 7
def amplitude_amostral():
    print("\n--- Exercício 7: Amplitude Amostral ---")
    vetor = []
    for i in range(10):
        vetor.append(int(input(f"Digite o {i+1}º número: ")))

    maximo = max(vetor)
    minimo = min(vetor)
    amplitude = maximo - minimo

    print(f"Valor máximo: {maximo}")
    print(f"Valor mínimo: {minimo}")
    print(f"Amplitude amostral: {amplitude}")

# 8
def pesquisar_vetor():
    print("\n--- Exercício 8: Pesquisar no Vetor ---")
    vetor = []
    for i in range(10):
        vetor.append(int(input(f"Digite o {i+1}º número: ")))

    pesquisa = int(input("Digite o número a ser pesquisado: "))
    posicoes = [i for i, x in enumerate(vetor) if x == pesquisa]
    ocorrencias = len(posicoes)

    if ocorrencias > 0:
        print(f"O número {pesquisa} foi encontrado na(s) posição(ões): {posicoes}")
        print(f"Foram detectadas {ocorrencias} ocorrência(s).")
    else:
        print(f"O número {pesquisa} não foi encontrado no vetor.")

# 9
def separar_pares_impares():
    print("\n--- Exercício 9: Separar Pares e Ímpares ---")
    vLido = []
    for i in range(10):
        vLido.append(int(input(f"Digite o {i+1}º número: ")))

    vPares = [x for x in vLido if x % 2 == 0]
    vImpares = [x for x in vLido if x % 2 != 0]

    print(f"Vetor lido: {vLido}")
    print(f"Vetor de pares: {vPares}")
    print(f"Vetor de ímpares: {vImpares}")

# 10
def ordenar_por_paridade():
    print("\n--- Exercício 10: Ordenar por Paridade ---")
    vetor = []
    while len(vetor) < 10:
        num = int(input(f"Digite o {len(vetor)+1}º número positivo: "))
        if num > 0:
            vetor.append(num)

    print(f"Vetor antes da modificação: {vetor}")
    vetor_modificado = sorted(vetor, key=lambda x: x % 2)
    print(f"Vetor depois da modificação: {vetor_modificado}")

# 11
def aposta_mega_sena():
    print("\n--- Exercício 11: Aposta na Mega-Sena ---")
    gabarito = random.sample(range(1, 61), 6)
    aposta = []
    while len(aposta) < 6:
        num = int(input(f"Digite o {len(aposta)+1}º número da sua aposta (1 a 60): "))
        if 1 <= num <= 60 and num not in aposta:
            aposta.append(num)

    acertos = len(set(gabarito) & set(aposta))
    print(f"Os números sorteados foram: {sorted(gabarito)}")
    print(f"Sua aposta foi: {sorted(aposta)}")
    print(f"Você teve {acertos} acerto(s).")

# 12
def ordenacao_selecao_direta():
    print("\n--- Exercício 12: Ordenação por Seleção Direta ---")
    vetor = []
    for i in range(20):
        vetor.append(int(input(f"Digite o {i+1}º número: ")))

    for i in range(len(vetor)):
        menor_idx = i
        for j in range(i + 1, len(vetor)):
            if vetor[j] < vetor[menor_idx]:
                menor_idx = j
        vetor[i], vetor[menor_idx] = vetor[menor_idx], vetor[i]

    print(f"Vetor ordenado: {vetor}")

