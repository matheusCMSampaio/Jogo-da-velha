import time
import os
def main():
    imprimeMenuPrincipal()
    

def leiaCoordenadaLinha():
    aux = []
    for i in range(len(jogo)):
        aux.append(i+1)
    return aux
    
def leiaCoordenadaColuna():
    aux = []
    for i in range(len(jogo)):
        aux.append(i+1)
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
    match escolha:
        case 1:
            imprimirTabuleiro()
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
    

jogo = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

main()
