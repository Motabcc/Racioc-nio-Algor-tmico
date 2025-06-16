import random
import time
import os

TAMANHO = 10
NAVIOS = {
    'Encouraçado': 5,
    'Porta-aviões': 4,
    'Contratorpedeiro1': 3,
    'Contratorpedeiro2': 3,
    'Submarino1': 2,
    'Submarino2': 2
}

class Cores:
    RESET = '\033[0m'
    AZUL = '\033[34m'
    VERMELHO = '\033[91m'
    AMARELO = '\033[93m'
    VERDE = '\033[92m'
    BRANCO = '\033[97m'
    CIANO = '\033[96m'

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_inicial():
    limpar_tela()
    print(Cores.CIANO + "=====================" + Cores.RESET)
    print(Cores.CIANO + "=== BATALHA NAVAL ===" + Cores.RESET)
    print(Cores.CIANO + "=====================" + Cores.RESET)

    print(f"Tamanho do Tabuleiro: {TAMANHO}x{TAMANHO}")
    print("\nEscolha o modo de jogo:")
    print("1 - Jogador vs Jogador")
    print("2 - Jogador vs IA")

    modo_valido = False
    modo_escolhido = ''
    while not modo_valido:
        modo_escolhido = input(Cores.BRANCO + "Modo: " + Cores.RESET)
        if modo_escolhido in ['1', '2']:
            modo_valido = True
        else:
            print(Cores.AMARELO + "Opção inválida. Digite apenas 1 ou 2." + Cores.RESET)
    return int(modo_escolhido)

def configurar_tabuleiro():
    return [['~' for _ in range(TAMANHO)] for _ in range(TAMANHO)]

def mostrar_tabuleiro(tabuleiro, mostrar_navios=False):
    cabecalho_colunas = Cores.BRANCO + '   ' + '  '.join(chr(65 + i) for i in range(TAMANHO)) + Cores.RESET
    print(cabecalho_colunas)
    print(Cores.BRANCO + '  +' + '---' * TAMANHO + '-+' + Cores.RESET)

    for i, linha_dados in enumerate(tabuleiro):
        linha_formatada = Cores.BRANCO + f"{i+1:2}| " + Cores.RESET
        for celula in linha_dados:
            simbolo_final = ''
            cor_aplicada = ''

            if celula == '~':
                simbolo_final = '≈'
                cor_aplicada = Cores.AZUL
            elif celula == 'N':
                if mostrar_navios:
                    simbolo_final = '■'
                    cor_aplicada = Cores.VERDE
                else:
                    simbolo_final = '≈'
                    cor_aplicada = Cores.AZUL
            elif celula == 'X':
                simbolo_final = '🔥' 
                cor_aplicada = Cores.VERMELHO
            elif celula == 'O':
                simbolo_final = '●'
                cor_aplicada = Cores.AMARELO
            else:
                simbolo_final = celula
                cor_aplicada = Cores.RESET

            linha_formatada += cor_aplicada + simbolo_final + Cores.RESET + '  '
        linha_formatada = linha_formatada.rstrip()
        linha_formatada += ' ' + Cores.BRANCO + "|" + Cores.RESET
        print(linha_formatada)
    print(Cores.BRANCO + '  +' + '---' * TAMANHO + '-+' + Cores.RESET)
    print()

def inicializar_lista_navios():
    lista_de_navios = []
    for nome_navio, tamanho_navio in NAVIOS.items():
        lista_de_navios.append({
            'nome': nome_navio,
            'tamanho': tamanho_navio,
            'coords': [], 
            'hits': set(), 
            'afundado': False
        })
    return lista_de_navios

def posicionar_navios(tabuleiro, nome_jogador="Jogador", lista_navios_do_jogador=None):
    limpar_tela()
    print(Cores.CIANO + f"--- {nome_jogador.upper()}: POSICIONE SEUS NAVIOS ---" + Cores.RESET)
    
    for navio_dict in lista_navios_do_jogador:
        navio_nome = navio_dict['nome']
        tam = navio_dict['tamanho']
        colocado = False
        
        navio_dict['coords'] = [] 
        navio_dict['hits'] = set()
        navio_dict['afundado'] = False

        while not colocado:
            print(Cores.BRANCO + f"\nPosicionando {navio_nome} (tamanho {tam})" + Cores.RESET)
            mostrar_tabuleiro(tabuleiro, mostrar_navios=True)
            try:
                linha_input = input(f"Linha inicial para {navio_nome} (1-{TAMANHO}): ")
                coluna_input = input(f"Coluna inicial para {navio_nome} (A-{chr(65 + TAMANHO - 1)}): ").upper()
                orientacao = input("Orientação (H para horizontal, V para vertical): ").upper()

                if not linha_input.isdigit():
                    print(Cores.AMARELO + "Linha inválida. Deve ser um número." + Cores.RESET)
                    continue
                linha = int(linha_input) - 1

                if not (len(coluna_input) == 1 and 'A' <= coluna_input <= chr(65 + TAMANHO - 1)):
                    print(Cores.AMARELO + "Coluna inválida." + Cores.RESET)
                    continue
                coluna = ord(coluna_input) - 65

                if orientacao not in ['H', 'V']:
                    print(Cores.AMARELO + "Orientação inválida. Digite H ou V." + Cores.RESET)
                    continue
            except ValueError:
                print(Cores.AMARELO + "Entrada de coordenadas inválida." + Cores.RESET)
                continue
            except Exception as e:
                print(Cores.AMARELO + f"Ocorreu um erro: {e}" + Cores.RESET)
                continue

            if validar_posicao(tabuleiro, linha, coluna, tam, orientacao):
                for i in range(tam):
                    coord_atual = None
                    if orientacao == 'H':
                        tabuleiro[linha][coluna + i] = 'N'
                        coord_atual = (linha, coluna + i)
                    else:  # 'V'
                        tabuleiro[linha + i][coluna] = 'N'
                        coord_atual = (linha + i, coluna)
                    navio_dict['coords'].append(coord_atual)
                
                colocado = True
                limpar_tela()
                print(Cores.CIANO + f"--- {nome_jogador.upper()}: POSICIONE SEUS NAVIOS ---" + Cores.RESET)
                print(Cores.VERDE + f"{navio_nome} posicionado!" + Cores.RESET)
            else:
                print(Cores.AMARELO + "Posição inválida (fora do tabuleiro ou sobreposição). Tente novamente." + Cores.RESET)
      

def validar_posicao(tabuleiro, linha, coluna, tam, orientacao):
    if orientacao == 'H':
        if not (0 <= linha < TAMANHO and 0 <= coluna < TAMANHO and coluna + tam <= TAMANHO):
            return False
        for i in range(tam):
            if tabuleiro[linha][coluna + i] != '~':
                return False
    else:  # 'V'
        if not (0 <= linha < TAMANHO and 0 <= coluna < TAMANHO and linha + tam <= TAMANHO):
            return False
        for i in range(tam):
            if tabuleiro[linha + i][coluna] != '~':
                return False
    return True

def posicionar_navios_automatico(tabuleiro, lista_navios_ia):
    for navio_dict in lista_navios_ia:
        tam = navio_dict['tamanho']
        colocado = False
        
        navio_dict['coords'] = []
        navio_dict['hits'] = set()
        navio_dict['afundado'] = False

        max_tentativas_pos = 100 
        tentativas_pos = 0
        while not colocado and tentativas_pos < max_tentativas_pos:
            orientacao = random.choice(['H', 'V'])
            linha = random.randint(0, TAMANHO - 1)
            coluna = random.randint(0, TAMANHO - 1)

            if validar_posicao(tabuleiro, linha, coluna, tam, orientacao):
                for i in range(tam):
                    coord_atual = None
                    if orientacao == 'H':
                        tabuleiro[linha][coluna + i] = 'N'
                        coord_atual = (linha, coluna + i)
                    else:  # 'V'
                        tabuleiro[linha + i][coluna] = 'N'
                        coord_atual = (linha + i, coluna)
                    navio_dict['coords'].append(coord_atual)
                colocado = True
            tentativas_pos += 1
        if not colocado:
         
            print(Cores.AMARELO + f"Atenção: IA teve dificuldade em posicionar {navio_dict['nome']}. Pode haver sobreposição ou falha." + Cores.RESET)


def realizar_ataque(tabuleiro_alvo, registro_ataques, nome_atacante, navios_do_alvo_lista, nome_jogador_alvo):
    ataque_valido = False
    linha, coluna = -1, -1

    while not ataque_valido:
        try:
            print(Cores.BRANCO + f"\n{nome_atacante}, sua vez de atacar!" + Cores.RESET)
            linha_input = input(f"Linha para atacar (1-{TAMANHO}): ")
            coluna_input = input(f"Coluna para atacar (A-{chr(65 + TAMANHO - 1)}): ").upper()

            if not linha_input.isdigit():
                print(Cores.AMARELO + "Linha inválida. Deve ser um número." + Cores.RESET)
                continue
            linha = int(linha_input) - 1

            if not (len(coluna_input) == 1 and 'A' <= coluna_input <= chr(65 + TAMANHO - 1)):
                print(Cores.AMARELO + "Coluna inválida." + Cores.RESET)
                continue
            coluna = ord(coluna_input) - 65

            if not (0 <= linha < TAMANHO and 0 <= coluna < TAMANHO):
                print(Cores.AMARELO + "Coordenada fora do tabuleiro." + Cores.RESET)
                continue
            if registro_ataques[linha][coluna] in ['X', 'O']:
                print(Cores.AMARELO + "Você já atacou essa posição." + Cores.RESET)
                continue
            ataque_valido = True
        except ValueError:
            print(Cores.AMARELO + "Entrada de coordenadas inválida." + Cores.RESET)
        except Exception as e:
            print(Cores.AMARELO + f"Ocorreu um erro: {e}" + Cores.RESET)

    foi_acerto_em_navio = False
    nome_navio_afundado = None

    if tabuleiro_alvo[linha][coluna] == 'N':
        foi_acerto_em_navio = True
        tabuleiro_alvo[linha][coluna] = 'X'
        registro_ataques[linha][coluna] = 'X' 
        
        for navio_atingido in navios_do_alvo_lista:
            if (linha, coluna) in navio_atingido['coords']:
                navio_atingido['hits'].add((linha, coluna))
                if len(navio_atingido['hits']) == navio_atingido['tamanho'] and not navio_atingido['afundado']:
                    navio_atingido['afundado'] = True
                    nome_navio_afundado = navio_atingido['nome']
                    print(Cores.VERMELHO + f"\nBOOOM! {nome_atacante} AFUNDOU o {nome_navio_afundado} de {nome_jogador_alvo}!" + Cores.RESET)
                break 
        
        if not nome_navio_afundado:
             print(Cores.VERMELHO + f"\nBOOOM! {nome_atacante} ACERTOU um navio de {nome_jogador_alvo}!" + Cores.RESET)

    elif tabuleiro_alvo[linha][coluna] == '~':
        print(Cores.AMARELO + "\nSPLASH! Você ERROU!" + Cores.RESET)
        tabuleiro_alvo[linha][coluna] = 'O' 
        registro_ataques[linha][coluna] = 'O'
    else:
        print(Cores.AMARELO + "\nSPLASH! Você ERROU (posição já conhecida)!" + Cores.RESET)
        if registro_ataques[linha][coluna] == '~': 
            if tabuleiro_alvo[linha][coluna] == 'X':
                 registro_ataques[linha][coluna] = 'X'
            elif tabuleiro_alvo[linha][coluna] == 'O':
                 registro_ataques[linha][coluna] = 'O'

    time.sleep(2) 
    return foi_acerto_em_navio, nome_navio_afundado

def ataque_ia(tabuleiro_alvo_jogador, registro_ataques_ia, navios_do_jogador_lista):
    print(Cores.CIANO + "\nIA está escolhendo um alvo..." + Cores.RESET)
    time.sleep(random.uniform(1.5, 3.0)) 

    escolha_valida = False
    linha, coluna = -1, -1
    max_tentativas_ataque = TAMANHO * TAMANHO # se der merda
    tentativas_ataque = 0

    while not escolha_valida and tentativas_ataque < max_tentativas_ataque:
        linha = random.randint(0, TAMANHO - 1)
        coluna = random.randint(0, TAMANHO - 1)
        if registro_ataques_ia[linha][coluna] == '~':
            escolha_valida = True
        tentativas_ataque +=1
    
    if not escolha_valida: 
        print(Cores.AMARELO + "IA não encontrou novas posições para atacar em seu registro." + Cores.RESET)
        time.sleep(1.5)
        return False, None 

    print(Cores.BRANCO + f"IA atacou em {chr(65 + coluna)}{linha + 1}" + Cores.RESET)
    time.sleep(1)

    foi_acerto_em_navio = False
    nome_navio_afundado = None

    if tabuleiro_alvo_jogador[linha][coluna] == 'N':
        foi_acerto_em_navio = True
        tabuleiro_alvo_jogador[linha][coluna] = 'X'
        registro_ataques_ia[linha][coluna] = 'X'

        for navio_atingido in navios_do_jogador_lista:
            if (linha, coluna) in navio_atingido['coords']:
                navio_atingido['hits'].add((linha, coluna))
                if len(navio_atingido['hits']) == navio_atingido['tamanho'] and not navio_atingido['afundado']:
                    navio_atingido['afundado'] = True
                    nome_navio_afundado = navio_atingido['nome']
                    print(Cores.VERMELHO + f"IA AFUNDOU seu {nome_navio_afundado}!" + Cores.RESET)
                break
        
        if not nome_navio_afundado:
            print(Cores.VERMELHO + "IA acertou um dos seus navios!" + Cores.RESET)
            
    elif tabuleiro_alvo_jogador[linha][coluna] == '~':
        print(Cores.AMARELO + "IA errou o tiro!" + Cores.RESET)
        tabuleiro_alvo_jogador[linha][coluna] = 'O'
        registro_ataques_ia[linha][coluna] = 'O'
    else: 
        print(Cores.AMARELO + "IA atacou uma posição já revelada (sem efeito prático)." + Cores.RESET)
        if tabuleiro_alvo_jogador[linha][coluna] == 'X':
             registro_ataques_ia[linha][coluna] = 'X' 
        elif tabuleiro_alvo_jogador[linha][coluna] == 'O':
             registro_ataques_ia[linha][coluna] = 'O' 

    time.sleep(2) 
    return foi_acerto_em_navio, nome_navio_afundado

def verificar_vitoria(tabuleiro_oponente_com_navios):
    for linha_tab in tabuleiro_oponente_com_navios:
        if 'N' in linha_tab:
            return False 
    return True 

def registrar_partida(historico_msg):
    try:
        with open("historico_batalha_naval.txt", "a", encoding="utf-8") as f:
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"[{timestamp}] {historico_msg}\n")
    except IOError:
        print(Cores.AMARELO + "Não foi possível registrar a partida no arquivo." + Cores.RESET)

def main():
    jogando = True
    while jogando:  #jogar de novo
        modo = menu_inicial()

        j1_lista_de_navios = inicializar_lista_navios()
        j2_lista_de_navios = inicializar_lista_navios()

        tabuleiro_j1 = configurar_tabuleiro()
        tabuleiro_j2 = configurar_tabuleiro()

        registro_j1_ataques_em_j2 = configurar_tabuleiro()
        registro_j2_ou_ia_ataques_em_j1 = configurar_tabuleiro()

        
        tiros_j1 = 0
        acertos_j1 = 0
        navios_afundados_j1 = 0 

        tiros_j2_ou_ia = 0
        acertos_j2_ou_ia = 0
        navios_afundados_j2_ou_ia = 0

        posicionar_navios(tabuleiro_j1, "Jogador 1", j1_lista_de_navios)
        input(Cores.BRANCO + "Jogador 1, seus navios estão posicionados. Pressione Enter para continuar..." + Cores.RESET)

        if modo == 1: 
            posicionar_navios(tabuleiro_j2, "Jogador 2", j2_lista_de_navios)
            input(Cores.BRANCO + "Jogador 2, seus navios estão posicionados. Pressione Enter para começar o jogo..." + Cores.RESET)
        else: 
            limpar_tela()
            print(Cores.CIANO + "IA está posicionando os navios dela..." + Cores.RESET)
            posicionar_navios_automatico(tabuleiro_j2, j2_lista_de_navios)
            time.sleep(1.5)
            print(Cores.VERDE + "IA terminou de posicionar os navios. Boa sorte!" + Cores.RESET)
            input(Cores.BRANCO + "Pressione Enter para começar o jogo..." + Cores.RESET)

        turno_jogador = 1
        historico_final = ""
        fim_de_jogo = False

        while not fim_de_jogo:
            limpar_tela()
            nome_jogador_vez = ""
            nome_oponente = ""
            
            acerto_neste_turno = False
            navio_afundado_neste_turno_nome = None

            if turno_jogador == 1:
                nome_jogador_vez = "Jogador 1"
                nome_oponente = "Jogador 2" if modo == 1 else "IA"
                print(Cores.CIANO + f"--- TURNO DO {nome_jogador_vez.upper()} ---" + Cores.RESET)
                print(Cores.BRANCO + "Seu tabuleiro (navios e danos recebidos):" + Cores.RESET)
                mostrar_tabuleiro(tabuleiro_j1, mostrar_navios=True)
                print(Cores.BRANCO + f"Seu registro de ataques em {nome_oponente}:" + Cores.RESET)
                mostrar_tabuleiro(registro_j1_ataques_em_j2, mostrar_navios=False) # Mostrar sem navios do oponente
                
                acerto_neste_turno, navio_afundado_neste_turno_nome = realizar_ataque(
                    tabuleiro_j2, registro_j1_ataques_em_j2, nome_jogador_vez, 
                    j2_lista_de_navios, nome_oponente
                )
                tiros_j1 += 1
                if acerto_neste_turno:
                    acertos_j1 += 1
                if navio_afundado_neste_turno_nome:
                    navios_afundados_j1 += 1

                if verificar_vitoria(tabuleiro_j2):
                    limpar_tela()
                    print(Cores.VERDE + f"🎉 PARABÉNS, {nome_jogador_vez.upper()}! VOCÊ AFUNDOU TODOS OS NAVIOS DE {nome_oponente.upper()}! 🎉" + Cores.RESET)
                    print(Cores.BRANCO + f"\nTabuleiro final de {nome_oponente}:" + Cores.RESET)
                    mostrar_tabuleiro(tabuleiro_j2, mostrar_navios=True)
                    historico_final = f"{nome_jogador_vez} venceu {nome_oponente}."
                    fim_de_jogo = True
                else:
                    turno_jogador = 2
            else: # jogador 2 ou IA
                nome_oponente = "Jogador 1"
                if modo == 1: 
                    nome_jogador_vez = "Jogador 2"
                    print(Cores.CIANO + f"--- TURNO DO {nome_jogador_vez.upper()} ---" + Cores.RESET)
                    print(Cores.BRANCO + "Seu tabuleiro (navios e danos recebidos):" + Cores.RESET)
                    mostrar_tabuleiro(tabuleiro_j2, mostrar_navios=True)
                    print(Cores.BRANCO + f"Seu registro de ataques em {nome_oponente}:" + Cores.RESET)
                    mostrar_tabuleiro(registro_j2_ou_ia_ataques_em_j1, mostrar_navios=False)
                    
                    acerto_neste_turno, navio_afundado_neste_turno_nome = realizar_ataque(
                        tabuleiro_j1, registro_j2_ou_ia_ataques_em_j1, nome_jogador_vez, 
                        j1_lista_de_navios, nome_oponente
                    )
                    tiros_j2_ou_ia += 1
                    if acerto_neste_turno:
                        acertos_j2_ou_ia += 1
                    if navio_afundado_neste_turno_nome:
                        navios_afundados_j2_ou_ia += 1
                else: # IA
                    nome_jogador_vez = "IA"
                    print(Cores.CIANO + f"--- TURNO DA {nome_jogador_vez.upper()} ---" + Cores.RESET)
                    
                    acerto_neste_turno, navio_afundado_neste_turno_nome = ataque_ia(
                        tabuleiro_j1, registro_j2_ou_ia_ataques_em_j1, 
                        j1_lista_de_navios
                    )
                    tiros_j2_ou_ia += 1
                    if acerto_neste_turno:
                        acertos_j2_ou_ia += 1
                    if navio_afundado_neste_turno_nome:
                        navios_afundados_j2_ou_ia += 1
                    
                    print(Cores.BRANCO + f"\nSeu tabuleiro ({nome_oponente}) após o ataque da IA:" + Cores.RESET)
                    mostrar_tabuleiro(tabuleiro_j1, mostrar_navios=True)
                
                if verificar_vitoria(tabuleiro_j1):
                    limpar_tela()
                    print(Cores.VERDE + f"🎉 {nome_jogador_vez.upper()} AFUNDOU TODOS OS NAVIOS DE {nome_oponente.upper()}! 🎉" + Cores.RESET)
                    print(Cores.BRANCO + f"\nTabuleiro final de {nome_oponente}:" + Cores.RESET)
                    mostrar_tabuleiro(tabuleiro_j1, mostrar_navios=True)
                    historico_final = f"{nome_jogador_vez} venceu {nome_oponente}."
                    fim_de_jogo = True
                else:
                    turno_jogador = 1

            if not fim_de_jogo:
                input(Cores.BRANCO + "\nPressione Enter para o próximo turno..." + Cores.RESET)

        # fim do jogo
        print(Cores.CIANO + "\n--- ESTATÍSTICAS DO JOGO ---" + Cores.RESET)
        print(Cores.BRANCO + f"Jogador 1:" + Cores.RESET)
        print(Cores.VERDE + f"  Tiros realizados: {tiros_j1}" + Cores.RESET)
        print(Cores.VERDE + f"  Tiros certeiros (em partes de navios): {acertos_j1}" + Cores.RESET)
        print(Cores.VERDE + f"  Navios inimigos afundados: {navios_afundados_j1}" + Cores.RESET)

        nome_adversario_final = "Jogador 2" if modo == 1 else "IA"
        print(Cores.BRANCO + f"\n{nome_adversario_final}:" + Cores.RESET)
        print(Cores.VERDE + f"  Tiros realizados: {tiros_j2_ou_ia}" + Cores.RESET)
        print(Cores.VERDE + f"  Tiros certeiros (em partes de navios): {acertos_j2_ou_ia}" + Cores.RESET)
        print(Cores.VERDE + f"  Navios inimigos afundados: {navios_afundados_j2_ou_ia}" + Cores.RESET)

        print(Cores.CIANO + "\n--- FIM DE JOGO ---" + Cores.RESET)
        registrar_partida(historico_final)
        if historico_final: # se tiver vencedor
             print(Cores.BRANCO + f"Partida: {historico_final}" + Cores.RESET)
        print(Cores.BRANCO + f"Histórico da partida salvo em 'historico_batalha_naval.txt'." + Cores.RESET)
        
        jogar_novamente_input = input(Cores.BRANCO + "\nDeseja jogar novamente? (S/N): " + Cores.RESET).upper()
        if jogar_novamente_input != 'S':
            jogando = False

    limpar_tela()
    print(Cores.CIANO + "Obrigado por jogar Batalha Naval!" + Cores.RESET)
    input(Cores.BRANCO + "\nPressione Enter para sair." + Cores.RESET)
    limpar_tela()

if __name__ == "__main__":
    main()