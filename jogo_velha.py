import time
import os
def main():
    imprimeMenuPrincipal()
    

def leiaCoordenadaLinha():
    aux = []
    for i in range(len(jogo)):
        aux.append(i)
    return aux
    
def leiaCoordenadaColuna():
    aux = []
    for i in range(len(jogo)):
        aux.append(i)
    return aux

    
def imprimirTabuleiro():
    linha = leiaCoordenadaLinha()
    coluna = leiaCoordenadaColuna()
    print(f'{linha[0]} {jogo[0][0]} | {jogo[0][1]} | {jogo[0][2]}')
    print('  ---------')
    print(f'{linha[1]} {jogo[1][0]} | {jogo[1][1]} | {jogo[1][2]}')
    print('  ---------')
    print(f'{linha[2]} {jogo[2][0]} | {jogo[2][1]} | {jogo[2][2]}')
    print(f'  {coluna[0]}   {coluna[1]}   {coluna[2]}')

def imprimeMenuPrincipal():
    os.system('cls') 
    print('\tMenu principal\n')
    print('1 - J x J \n2 - J x Bot (Modo Fácil) \n3 - J x Bot (Modo difícil)\n0 - Sair')
    escolha = int(input('Escolha a opção: '))
    time.sleep(2)
    match escolha:
        case 1:
            modoJogador()
        case 2:
            print('2')
        case 3:
            print('3')
        case 0:
            print('0')
        case _:
            print('\n\tOpção inválida\n')
            time.sleep(2)
            imprimeMenuPrincipal()
    
def modoJogador():
    os.system('cls')
    aux = 1  
    jogador = 1
    linha = 0
    coluna = 0
    while aux <=9:
        imprimirTabuleiro()
        if aux % 2 == 0: #Verifica qual jogador irá jogar, ou seja, em numeros pares será o jogador 2 que joga
            jogador = 2
        else:
            jogador = 1 # E impar é o jogador 1 que joga
        linha= int(input(f'Jogador {jogador}: Escolha a linha: '))
        coluna= int(input(f'Jogador {jogador}: Escolha a coluna: '))
        if posicaoValida(linha, coluna):
            if jogador == 1:
                jogada = 'X'
                jogo[linha][coluna] = 'X'
            else:
                jogada = 'O'
                jogo[linha][coluna] = 'O'
            
            if validaColuna(jogada) or validaLinha(jogada) or validaVertical(jogada):
                print(f'Jogador {jogador} vitórioso')
                time.sleep(2)
                os.system('cls')
                escolha = input('Deseja continuar?')
                if escolha== 'Sim' or escolha == 'sim':
                    imprimeMenuPrincipal()
                else:
                    os.system('cls')
                    time.sleep(2)
                    print('Adeus')
                    break

        else:
            print('\n\tPosição inválida')
            aux =-1
        aux += 1


def posicaoValida(linha,coluna):
    if jogo[linha][coluna] == ' ':
        return True
    else:
        return False


def verificaVencedor(jogador):
    jogada = ''
    if jogador == 1:
        jogada = 'X'
    else:
        jogada = 'O'
    
def validaLinha(jogada):
    for i in range(len(jogo)):
        if jogo[i][0] == jogada and jogo[i][1] == jogada and jogo[i][2] == jogada:
            return True
    return False    

def validaColuna(jogada):
    for i in range(len(jogo)):
        if jogo[0][i] == jogada and jogo[1][i] == jogada and jogo[2][i] == jogada:
            return True
    return False    

def validaVertical(jogada):
    if jogo[0][0] == jogada and jogo[1][1] == jogada and jogo[2][2] == jogada:
        return True
    elif jogo[0][2] == jogada and jogo[1][1] == jogada and jogo[2][0] == jogada:
        return True
    else:
        return False



jogo = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

main()
