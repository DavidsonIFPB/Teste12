JOGADAS = 1
QUANT_BRANCAS = 12
QUANT_PRETAS = 12
VAZIO = "      "
BRANCA = "BRANCA"
PRETA = "PRETA "
DAMA_BRANCA = "DAMA-B"
DAMA_PRETA = "DAMA-P"

peca_branca=[DAMA_BRANCA,BRANCA]
def imprimir_tabuleiro ():
    for i in tabuleiro:
        for t in i:
            print(t, end=' | ')
        print("\n")


def  mov_das_pecas  (destino_linha, destino_coluna, inicio_linha, inicio_coluna):

    """ESSA FUNÇÃO ANALISA SE O MOVIMENTO DE UMA PEÇA(SEJA ELA BRANCA OU PRETA) É VALIDO."""

    global JOGADAS

    # CONDIÇÕES PARA AS PEÇAS BRANCA SEREM MOVIMENTADAS
    if JOGADAS % 2 != 0:     #JOGADOR 1 É AS BRANCAS
        if destino_linha > inicio_linha and destino_linha - inicio_linha==1 and (destino_coluna - inicio_coluna==-1 or destino_coluna-inicio_coluna==1) and destino_linha != inicio_linha and destino_coluna != inicio_coluna and \
                        tabuleiro[destino_linha][destino_coluna]==VAZIO and tabuleiro[inicio_linha][inicio_coluna]==BRANCA:
            tabuleiro[inicio_linha][inicio_coluna] = VAZIO
            tabuleiro[destino_linha][destino_coluna] = BRANCA
            # CONDIÇÃO PARA UMA PEÇA SE TORNAR UMA DAMA BRANCA
            if destino_linha == 8:
                tabuleiro[destino_linha][destino_coluna] = DAMA_BRANCA
        else:
            JOGADAS-=1      #DIMINUI 1 NO NÚMERO DE JOGADAS PARA RETORNAR A JOGADA PARA O JOGADOR QUE TENTOU MOVIMENTAR AS PEÇAS DE FORMA ERRADA.
            print("É A VEZ DE VOCÊ  MOVIMENTAR AS PEÇAS BRANCAS E VOCÊ MOVIMENTOU ELAS DE FORMA ERRADA.JOGUE NOVAMENTE!""\n")     #MENSAGEM DE ERRO CASO A PEÇA NÃO POSSA SER MOVIMENTADA.

    # CONDIÇÕES PARA A PEÇA PRETA SER MOVIMENTADA
    elif JOGADAS % 2 == 0:#JOGADOR 2 É AS PRETAS
        if destino_linha < inicio_linha and inicio_linha - destino_linha == 1 and((destino_coluna - inicio_coluna==-1) or (destino_coluna-inicio_coluna==1))  and destino_linha != inicio_linha \
                and destino_coluna != inicio_coluna and tabuleiro[destino_linha][destino_coluna] == VAZIO and tabuleiro[inicio_linha][inicio_coluna]==PRETA:
            tabuleiro[inicio_linha][inicio_coluna] = VAZIO
            tabuleiro[destino_linha][destino_coluna] = PRETA
            # CONDIÇÃO PARA PEÇA SE TORNAR UMA DAMA PRETA
            if destino_linha == 1:
                tabuleiro[destino_linha][destino_coluna] = DAMA_PRETA
        else:
            JOGADAS -= 1  #DIMINUI 1 NO NÚMERO DE JOGADAS PARA RETORNAR A JOGADA PARA O JOGADOR QUE TENTOU MOVIMENTAR AS PEÇAS DE FORMA ERRADA
            print("É A VEZ DE VOCÊ  MOVIMENTAR AS PEÇAS PRETAS E VOCÊ MOVIMENTOU ELAS DE FORMA ERRADA.JOGUE NOVAMENTE!""\n")  #MENSAGEM DE ERRO CASO A PEÇA NÃO POSSA SER MOVIMENTADA.


def comer_peca_preta (destino_linha, destino_coluna, inicio_linha, inicio_coluna):

    """ESSA FUNÇÃO ANALISA SE A TENTATIVA DO JOGADOR 1 DE COMER UMA PEÇA PRETA DO JOGADOR 2 É VÁLIDA"""

    global JOGADAS
    global QUANT_PRETAS

    if JOGADAS % 2 != 0:  #VERIFICA SE A VEZ É REALMENTE DO JOGADOR 1 (PEÇAS BRANCAS)
        if inicio_coluna < destino_coluna and inicio_linha< destino_linha and tabuleiro[destino_linha][destino_coluna] ==VAZIO \
                and tabuleiro[inicio_linha + 1][inicio_coluna + 1] == PRETA \
                and destino_coluna-inicio_coluna==2 and destino_linha-inicio_linha==2:    #CONDIÇÕES PARA COMER UMA PEÇA PRETA PARA O LADO DIREITO
            tabuleiro[inicio_linha][inicio_coluna] = VAZIO
            tabuleiro[inicio_linha + 1][inicio_coluna + 1] = VAZIO
            tabuleiro[destino_linha][destino_coluna] = BRANCA
            QUANT_PRETAS-=1
            if destino_linha == 8:     #CONDIÇÃO PARA A PEÇA BRANCA VIRAR UMA DAMA-BRANCA NO MOMENTO QUE ESTIVER COMENDO UMA PEÇA PRETA PARA O LADO DIREITO
                tabuleiro[destino_linha][destino_coluna] = DAMA_BRANCA

        elif inicio_coluna > destino_coluna  and inicio_linha< destino_linha and tabuleiro[inicio_linha + 1][inicio_coluna - 1] == PRETA \
                and tabuleiro[destino_linha][destino_coluna]==VAZIO and inicio_coluna-destino_coluna==2 and destino_linha-inicio_linha==2: #CONDIÇÕES PARA COMER UMA PEÇA PRETA PARA O LADO ESQUERDO
            tabuleiro[inicio_linha][inicio_coluna] = VAZIO
            tabuleiro[inicio_linha + 1][inicio_coluna - 1] = VAZIO
            tabuleiro[destino_linha][destino_coluna] = BRANCA
            QUANT_PRETAS-=1
            if destino_linha == 8:  #CONDIÇÃO PARA A PEÇA BRANCA VIRAR UMA DAMA-BRANCA NO MOMENTO QUE ESTIVER COMENDO UMA PEÇA PRETA PARA O LADO ESQUERDO
                tabuleiro[destino_linha][destino_coluna] = DAMA_BRANCA
        else:
            JOGADAS-=1
            print("VOCÊ MOVIMENTOU A PEÇA BRANCA DE FORMA ERRADA. JOGUE NOVAMENTE!") #MENSAGEM DE ERRO, PARA SE CASO ELE MOVIMENTAR A PEÇA DELE PARA O LUGAR ERRADO
    else:
        JOGADAS -= 1
        print("VOCÊ MOVIMENTOU A PEÇA ERRADA. A VEZ DE JOGAR É DO JOGADOR 2, O JOGADOR DAS PEÇAS PRETAS!")  #MENSAGEM DE ERRO, PARA SE O JOGADOR FOR MEXER A PEÇA ERRADA

def comer_peca_branca(destino_linha, destino_coluna, inicio_linha, inicio_coluna):
    """ESSA FUNÇÃO ANALISA SE A TENTATIVA DO JOGADOR 2 DE COMER UMA PEÇA BRANCA DO JOGADOR 1 É VÁLIDA"""

    global JOGADAS
    global QUANT_BRANCAS
    if JOGADAS%2==0:  #VERIFICA SE A VEZ É REALMENTE DO JOGADOR 2 (PEÇAS PRETAS)
        if inicio_linha>destino_linha and inicio_coluna<destino_coluna and (tabuleiro[inicio_linha-1][inicio_coluna+1]== BRANCA) \
                and tabuleiro[destino_linha][destino_coluna]==VAZIO and destino_coluna-inicio_coluna==2 and inicio_linha-destino_linha==2: #CONDIÇÕES PARA COMER UMA PEÇA BRANCA PARA O LADO DIREITO

            tabuleiro[inicio_linha][inicio_coluna] = VAZIO
            tabuleiro[inicio_linha - 1][inicio_coluna + 1] = VAZIO
            tabuleiro[destino_linha][destino_coluna] = PRETA
            QUANT_BRANCAS-=1
            if destino_linha == 1: #CONDIÇÃO PARA A PEÇA PRETA VIRAR UMA DAMA-PRETA NO MOMENTO QUE ESTIVER COMENDO UMA PEÇA BRANCA PARA O LADO DIREITO
                tabuleiro[destino_linha][destino_coluna] = DAMA_PRETA



        elif inicio_linha > destino_linha and inicio_coluna > destino_coluna and tabuleiro[inicio_linha - 1][inicio_coluna - 1]== BRANCA \
                and tabuleiro[destino_linha][destino_coluna]==VAZIO and inicio_coluna-destino_coluna==2 and inicio_linha-destino_linha==2: #CONDIÇÕES PARA COMER UMA PEÇA BRANCA PARA O LADO ESQUERDO
            tabuleiro[inicio_linha][inicio_coluna] = VAZIO
            tabuleiro[inicio_linha-1][inicio_coluna-1]=VAZIO
            tabuleiro[destino_linha][destino_coluna] = PRETA
            QUANT_BRANCAS-=1
            if destino_linha == 1:  #CONDIÇÃO PARA A PEÇA PRETA VIRAR UMA DAMA-PRETA NO MOMENTO QUE ESTIVER COMENDO UMA PEÇA BRANCA PARA O LADO ESQUERDO
                tabuleiro[destino_linha][destino_coluna] = DAMA_PRETA
        else:
            JOGADAS-=1
            print("VOCÊ MOVIMENTOU A PEÇA PRETA DE FORMA ERRADA. JOGUE NOVAMENTE!") #MENSAGEM DE ERRO, PARA SE CASO ELE MOVIMENTAR A PEÇA DELE PARA O LUGAR ERRADO
    else:
        JOGADAS -= 1
        print("VOCÊ MOVIMENTOU A PEÇA ERRADA. A VEZ DE JOGAR É DO JOGADOR 1, O JOGADOR DAS PEÇAS BRANCAS!") #MENSAGEM DE ERRO, PARA SE O JOGADOR FOR MEXER A PEÇA ERRADA

#A DAMA NÃO ESTAR CORRENDO A DIAGONAL TODA, ELA SÓ ANDA E COME PARA FRENTE E PARA ATRÁS PULANDO DE UMA EM UMA CASA
def mover_dama_branca(destino_linha, destino_coluna, inicio_linha, inicio_coluna):
    '''
    coluna=0
    for x in range(1,9):
        coluna+=1        
        if(tabuleiro[x][coluna]==VAZIO or tabuleiro[x][coluna]==PRETA):
            tabuleiro[inicio_linha][inicio_coluna] = VAZIO
            tabuleiro[destino_linha][destino_coluna] = DAMA_BRANCA
            break
     '''       
           
    if  tabuleiro[destino_linha][destino_coluna] == VAZIO and destino_linha != inicio_linha and destino_coluna != inicio_coluna and ((inicio_linha - destino_linha == 1) or (inicio_linha - destino_linha == -1)):
            tabuleiro[inicio_linha][inicio_coluna] = VAZIO
            tabuleiro[destino_linha][destino_coluna] = DAMA_BRANCA
    
    else:
        print("VOCÊ MOVIMENTOU A DAMA BRANCA DE FORMA ERRADA. JOGUE NOVAMENTE!")

def mover_dama_preta(destino_linha, destino_coluna, inicio_linha, inicio_coluna):
    if tabuleiro[destino_linha][destino_coluna] == VAZIO and destino_coluna!=inicio_coluna and destino_linha!=inicio_linha and ((inicio_linha-destino_linha==1) or (inicio_linha-destino_linha == -1)):
        tabuleiro[inicio_linha][inicio_coluna]= VAZIO
        tabuleiro[destino_linha][destino_coluna]= DAMA_PRETA
    else:
        print("VOCÊ MOVIMENTOU A DAMA PRETA DE FORMA ERRADA. JOGUE NOVAMENTE!")

def comer_com_dama_branca(destino_linha, destino_coluna, inicio_linha, inicio_coluna):
    # COMENDO PARA DIREITA E PARA CIMA
    if inicio_coluna < destino_coluna and inicio_linha > destino_linha:
        tabuleiro[inicio_linha][inicio_coluna] = VAZIO
        tabuleiro[destino_linha][destino_coluna] = DAMA_BRANCA

    # COMENDO PARA DIREITA E PARA BAIXO
    elif inicio_coluna < destino_coluna and inicio_linha < destino_linha:
        tabuleiro[inicio_linha][inicio_coluna] = VAZIO
        tabuleiro[destino_linha][destino_coluna] = DAMA_BRANCA

    # COMENDO PARA ESQUERDA E PARA CIMA
    elif inicio_coluna > destino_coluna and inicio_linha > destino_linha:
        tabuleiro[inicio_linha][inicio_coluna] = VAZIO
        tabuleiro[destino_linha][destino_coluna] = DAMA_BRANCA

    # COMENDO PARA ESQUERDA E PARA BAIXO
    elif inicio_coluna > destino_coluna and inicio_linha < destino_linha:
        tabuleiro[inicio_linha][inicio_coluna] = VAZIO
        tabuleiro[destino_linha][destino_coluna] = DAMA_BRANCA

def comer_com_dama_preta(destino_linha, destino_coluna, inicio_linha, inicio_coluna):
    # PARA DIREITA E PARA CIMA
    if inicio_coluna < destino_coluna and inicio_linha < destino_linha:
        tabuleiro[inicio_linha][inicio_coluna] = VAZIO
        tabuleiro[destino_linha][destino_coluna] = DAMA_PRETA

    # PARA DIREITA E PARA BAIXO
    elif inicio_coluna < destino_coluna and inicio_linha > destino_linha:
        tabuleiro[inicio_linha][inicio_coluna] = VAZIO
        tabuleiro[destino_linha][destino_coluna] = DAMA_PRETA


    # PARA ESQUERDA E PARA CIMA
    elif inicio_coluna > destino_coluna and inicio_linha < destino_linha:
        tabuleiro[inicio_linha][inicio_coluna] = VAZIO
        tabuleiro[destino_linha][destino_coluna] = DAMA_PRETA


    # ESQUERDA E PARA BAIXO
    elif inicio_coluna > destino_coluna and inicio_linha > destino_linha:
        tabuleiro[inicio_linha][inicio_coluna] = VAZIO
        tabuleiro[destino_linha][destino_coluna] = DAMA_PRETA

print("                       SEJA BEM VINDO AO JOGO DE DAMAS!!\n\n"
      "O JOGADOR 1 MOVERÁ APENAS AS PEÇAS BRANCAS E O JOGADOR 2 MOVERÁ AS PEÇAS PRETAS.\n"
      "PARA JOGAR PRIMEIRO VOCÊ DEVE DIGITAR O NÚMERO DA LINHA E EM SEGUIDA O NÚMERO DA COLUNA.\n"
      "EXEMPLO: 31(NESSE CASO VOCÊ VAI ESTAR INFORMANDO QUE A PEÇA ESTÁ NA LINHA 3, COLUNA 1.\n\n")

tabuleiro = [['   ', '   1  ', '   2  ', '   3  ', '  4   ', '   5  ', '   6  ', '   7  ', '   8  '],
            ['1  ', BRANCA, VAZIO, BRANCA, VAZIO, BRANCA, VAZIO, BRANCA, VAZIO],
            ['2  ', VAZIO, BRANCA, VAZIO, BRANCA, VAZIO, BRANCA, VAZIO, BRANCA],
            ['3  ', BRANCA, VAZIO, DAMA_BRANCA, VAZIO, BRANCA, VAZIO, BRANCA, VAZIO],
            ['4  ', VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO],
            ['5  ', VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO, VAZIO],
            ['6  ', VAZIO, PRETA, VAZIO, PRETA, VAZIO, PRETA, VAZIO, PRETA],
            ['7  ', PRETA, VAZIO, PRETA, VAZIO, PRETA, VAZIO, PRETA, VAZIO],
            ['8  ', VAZIO, PRETA, VAZIO, PRETA, VAZIO, PRETA, VAZIO, PRETA]]

imprimir_tabuleiro()

while True:
    coluna=0
    for x in range(1,9):
        coluna+=1        
        if(tabuleiro[x][coluna]==VAZIO):
            print("yes")            
            break
        

    if QUANT_BRANCAS>0 and QUANT_PRETAS>0:
        if JOGADAS%2!=0:
            print("JOGADOR 1 - PEÇAS BRANCAS\n")
        elif JOGADAS%2==0:
            print("JOGADOR 2 - PEÇAS PRETAS\n")

        posicao_atual = input("DIGITE A POSIÇÃO ATUAL DA PEÇA: ")
        if  len(posicao_atual)!=2 or  posicao_atual.isdigit() == False: #VERIFICA SE TEM APENAS DOIS DIGITOS E SE REALMENTE SÃO DIGITOS
            print("VOCÊ DIGITOU A POSIÇÃO ATUAL DE FORMA ERRADA.DIGITE NOVAMENTE!")
            continue
        posicao_destino = input("DIGITE A POSIÇÃO DESTINO DA PEÇA: ")
        if len(posicao_destino) != 2 or posicao_destino.isdigit() == False: #VERIFICA SE TEM APENAS DOIS DIGITOS E SE REALMENTE SÃO DIGITOS
            print("VOCÊ DIGITOU A POSIÇÃO DESTINO DE FORMA ERRADA.DIGITE NOVAMENTE!")
            continue

        inicio_linha = int(posicao_atual[0:1])
        inicio_coluna = int(posicao_atual[1:])
        destino_linha = int(posicao_destino[0:1])
        destino_coluna = int(posicao_destino[1:])

        if destino_linha>8 or destino_linha <1 or destino_coluna>8 or destino_coluna<1 \
                or inicio_linha>8 or inicio_coluna<1 or inicio_coluna>8 or inicio_coluna<1: #VBRIFICA SE DIGITOU DE 1 ATÉ 8
            print("A POSIÇÃO ATUAL E A POSIÇÃO DESTINO DA LINHA É DE 1 ATÉ 8, VOCÊ NÃO OBEDECEU A ESSE PADRÃO. DIGITE NOVAMENTE!")
            continue


        if tabuleiro[inicio_linha][inicio_coluna]== DAMA_BRANCA:
             mover_dama_branca(destino_linha, destino_coluna, inicio_linha, inicio_coluna)
             comer_com_dama_branca(destino_linha, destino_coluna, inicio_linha, inicio_coluna)
             imprimir_tabuleiro()

        elif tabuleiro[inicio_linha][inicio_coluna] == DAMA_PRETA:
             mover_dama_preta(destino_linha, destino_coluna, inicio_linha, inicio_coluna)
             comer_com_dama_preta(destino_linha, destino_coluna, inicio_linha, inicio_coluna)
             imprimir_tabuleiro()

        elif inicio_linha - destino_linha == 1 or destino_linha - inicio_linha ==1 and (destino_coluna - inicio_coluna==-1 or destino_coluna-inicio_coluna==1):
            mov_das_pecas(destino_linha, destino_coluna, inicio_linha, inicio_coluna)
            imprimir_tabuleiro()

        elif (tabuleiro[inicio_linha + 1][inicio_coluna - 1] == PRETA or tabuleiro[inicio_linha + 1][inicio_coluna + 1] == PRETA) \
                and tabuleiro[destino_linha][destino_coluna]==VAZIO and destino_linha-inicio_linha==2 and (inicio_coluna-destino_coluna==2 or  destino_coluna-inicio_coluna==2):
            comer_peca_preta(destino_linha, destino_coluna, inicio_linha, inicio_coluna)
            imprimir_tabuleiro()
        elif (tabuleiro[inicio_linha-1][inicio_coluna+1]== BRANCA or tabuleiro[inicio_linha - 1][inicio_coluna - 1]== BRANCA) and inicio_linha > destino_linha \
                and tabuleiro[destino_linha][destino_coluna]==VAZIO:
            comer_peca_branca(destino_linha, destino_coluna, inicio_linha, inicio_coluna)
            imprimir_tabuleiro()
        else:
            JOGADAS -= 1
            imprimir_tabuleiro()
            print("JOGADA INVÁLIDA. JOGUE NOVAMENTE!")
        JOGADAS += 1
    else:
        if QUANT_BRANCAS > 0 and QUANT_PRETAS == 0:
             print("O JOGADOR DAS PEÇAS BRANCAS VENCEU!!")
             break
        elif QUANT_BRANCAS == 0 and QUANT_PRETAS > 0:
             print("O JOGADOR DAS PEÇAS PRETAS VENCEU!!")
             break
        elif QUANT_BRANCAS == 1 and QUANT_PRETAS == 1:
             print("O JOGO DEU EMPATE!!")
             break




