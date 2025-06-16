from random import randint
# Importar biblioteca para randomizar a escolha da máquina/ criar condição para o while
continuar = "s"
while continuar == 's':
    maquina_Ou_Humano = int(input("Se quiser jogar com máquina digite 1, se quiser jogar com seu amigo digite 2: "))
    # Caso o usuário erre, fique em looping até digitar o valor certo
    while maquina_Ou_Humano not in [1, 2]:
        try:
            maquina_Ou_Humano = int(input("Escolha somente 1 ou 2: "))
        except ValueError:
            print("Escolha 1 ou 2: ")
    # Após a condição ser verificada
    try:
        while 2 >= maquina_Ou_Humano >= 1:
            nomes = []
            if maquina_Ou_Humano == 2: nomeUm = input("Insira o nome do jogador 1: "); nomes.append(nomeUm); nomeDois = input("Insira o nome do jogador 2: "); nomes.append(nomeDois)
            else: nomeUm = input("Insira o nome do jogador 1: "); nomeDois = "Máquina"; nomes.append(nomeUm); nomes.append(nomeDois)
            # Condição para o looping e adicionar o vencedor de cada partida a uma lista
            historico = []
            while continuar == "s":
                jogada0 = int(input(f"{nomes[0]} escolha [0] para pedra, [1] para papel, e [2] para tesoura: "))
                # Para o outro jogador não ver a resposta anterior
                print(f"{'='} \n" * 30)
                if maquina_Ou_Humano == 2: jogada1 = int(input(f"{nomes[1]} escolha [0] para pedra, [1] para papel, e [2] para tesoura: "))
                # Randomizar escolha
                else: jogada1 = randint(0, 2)
                while jogada0 not in [0, 1, 2] or jogada1 not in [0, 1, 2]:
                    try:
                        jogada0 = int(input(f"{nomes[0]} escolha [0] para pedra, [1] para papel, e [2] para tesoura: "))
                        if nomes[1] == "Máquina": jogada1 = randint(0, 2)
                        else: jogada1 = int(input(f"{nomes[1]} escolha [0] para pedra, [1] para papel, e [2] para tesoura: "))
                    except ValueError:
                        print(" ")
                # Condições para ganhar/perder/empatar
                if jogada0 == jogada1: print(f"{nomes[0]} e {nomes[1]} empataram!"); historico.append('empate')
                elif (jogada0 == 0 and jogada1 == 2) or (jogada0 == 1 and jogada1 == 0) or (jogada0 == 2 and jogada1 == 1): print(f"\033[1;32m{nomes[0]}\033[m ganhou de \033[1;31m{nomes[1]}!\033[m "); historico.append(f'vitória de {nomes[0]}')
                else: print(f"\033[1;32m{nomes[1]}\033[m ganhou de \033[1;31m{nomes[0]}!\033[m "); historico.append(f'vitória de {nomes[1]}')
                continuar = input("Insira S/N para continuar ou parar: ").strip().lower()
            print(f"Histórico de partidas: {historico}")
            # Caso o usuário digite "n", interrompe o jogo completamente
            if continuar == "n": break
    # Caso o usuário digite uma string!
    except ValueError:
        print('Opção inválida. Digite um número inteiro!')