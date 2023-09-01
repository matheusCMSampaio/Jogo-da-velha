import time

import os

import random

def main():
    imprimeMenuPrincipal()

def imprimeMenuPrincipal():

    os.system('cls') 

    print('\tMenu principal\n')

    print('1 - J x J \n2 - J x Bot (Modo Fácil) \n0 - Sair')

    escolha = int(input('Escolha a opção: '))

    time.sleep(2)
    tabuleiro = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

    match escolha:

        case 1:

            
            modoJogador(tabuleiro)

        case 2:

            tabuleiro = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]


            modoFacil()

        case 0:

            print('0')

        case _:

            print('\n\tOpção inválida\n')

            time.sleep(2)

            imprimeMenuPrincipal()    


def leiaCoordenadaLinha(tabuleiro):

    aux = []
    for i in range(len(tabuleiro)):

        aux.append(i)

    return aux
    

def leiaCoordenadaColuna(tabuleiro):

    aux = []
    for i in range(len(tabuleiro)):

        aux.append(i)

    return aux

    

def imprimirTabuleiro(tabuleiro):

    linha = leiaCoordenadaLinha(tabuleiro)

    coluna = leiaCoordenadaColuna(tabuleiro)

    print(f'{linha[0]} {tabuleiro[0][0]} | {tabuleiro[0][1]} | {tabuleiro[0][2]}')

    print('  ---------')

    print(f'{linha[1]} {tabuleiro[1][0]} | {tabuleiro[1][1]} | {tabuleiro[1][2]}')

    print('  ---------')

    print(f'{linha[2]} {tabuleiro[2][0]} | {tabuleiro[2][1]} | {tabuleiro[2][2]}')

    print(f'  {coluna[0]}   {coluna[1]}   {coluna[2]}')



    

def modoJogador(tabuleiro):

    os.system('cls')

    cont = 1  

    jogador = 1

    linha = 0

    coluna = 0

    while cont <=9:

        imprimirTabuleiro(tabuleiro)

        if cont % 2 == 0: 

            jogador = 2
        else:

            jogador = 1 

        linha= int(input(f'Jogador {jogador}: Escolha a linha: '))

        coluna= int(input(f'Jogador {jogador}: Escolha a coluna: '))

        if jogar(linha,coluna,jogador,tabuleiro) == False:

            cont -=1

        if verificaVencedor('X' if jogador == 1 else 'O', jogador, tabuleiro):
            somaVencedor(jogador)
            imprimeMenuPrincipal()

        if verificaVelha(cont, tabuleiro):

            imprimeMenuPrincipal()

        cont += 1


def verificaVelha(cont, tabuleiro):

    if cont == 9:

        imprimirTabuleiro(tabuleiro)

        print('\tDeu velha!')

        return True

    return False



def jogar(linha,coluna,jogador,tabuleiro):

    if posicaoValida(linha, coluna, tabuleiro):

        if jogador == 1:

            jogada = 'X'

            tabuleiro[linha][coluna] = 'X'
        else:

            jogada = 'O'

            tabuleiro[linha][coluna] = 'O'
    else:

        print('\n\tPosição inválida')

        aux =-1

        return False

    return True


def verificaVencedor(jogada, jogador, tabuleiro):

    if validaColuna(jogada,tabuleiro) or validaLinha(jogada, tabuleiro) or validaVertical(jogada, tabuleiro):

        print(f'Jogador {jogador} vitórioso')

        imprimirTabuleiro(tabuleiro)

        time.sleep(2)

        return True

    return False
            

def somaVencedor(jogador):

    jogador += 1
    return jogador           


def imprimePontuacao(jogador1, jogador2):

    print(f'Pontuação \nJogador 1 - {jogador1} pontos\nJogador 2 - {jogador2} pontos')


def posicaoValida(linha,coluna,tabuleiro):

    if tabuleiro[linha][coluna] == ' ':

        return True
    else:

        return False


    

def validaLinha(jogada,tabuleiro):
    for i in range(len(tabuleiro)):

        if tabuleiro[i][0] == jogada and tabuleiro[i][1] == jogada and tabuleiro[i][2] == jogada:

            return True

    return False    


def validaColuna(jogada,tabuleiro):
    for i in range(len(tabuleiro)):

        if tabuleiro[0][i] == jogada and tabuleiro[1][i] == jogada and tabuleiro[2][i] == jogada:

            return True

    return False    


def validaVertical(jogada,tabuleiro):

    if tabuleiro[0][0] == jogada and tabuleiro[1][1] == jogada and tabuleiro[2][2] == jogada:

        return True

    elif tabuleiro[0][2] == jogada and tabuleiro[1][1] == jogada and tabuleiro[2][0] == jogada:

        return True
    else:

        return False


def modoFacil(tabuleiro):

    os.system('cls')

    cont = 1  

    jogador = 1

    linha = 0

    coluna = 0

    aux = 0

    while cont <=5:

        imprimirTabuleiro(tabuleiro)

        aux +=1

        linha= int(input(f'Jogador {jogador}: Escolha a linha: '))

        coluna= int(input(f'Jogador {jogador}: Escolha a coluna: '))

        if jogar(linha,coluna,1,tabuleiro) == False:

            cont -=1

            aux -= 1

        if verificaVencedor('X', jogador):
            somaVencedor(1)
            imprimeMenuPrincipal()

        aux+= 1

        while True:

            if jogar(random.randint(0,2), random.randint(0,2), 0):

                break

        if verificaVencedor('O', 'bot'):
            somaVencedor(2)
            imprimeMenuPrincipal()

        if verificaVelha(cont,tabuleiro):

            imprimeMenuPrincipal()

        cont += 1



main()

