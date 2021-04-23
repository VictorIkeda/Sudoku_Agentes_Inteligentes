import time


def mundo():
    sudoku = [[0, 6, 0, 0, 0, 3, 8, 7, 2], [1, 0, 2, 0, 7, 0, 5, 3, 6], [0, 0, 0, 2, 6, 5, 4, 0, 1], [7, 3, 1, 5, 0, 0, 9, 0, 8], [0, 5, 0, 0, 8, 0, 0, 4, 3], [6, 8, 0, 3, 0, 9, 0, 5, 0], [5, 2, 0, 0, 0, 0, 0, 8, 0], [0, 1, 0, 8, 9, 7, 6, 2, 0], [8, 0, 0, 6, 0, 0, 0, 1, 4]]
    return(sudoku)


def iniciar_jogo():
    print("Tabuleiro do sudoku \n")
    sudoku = mundo()
    for x in range(len(sudoku)):
        if x % 3 == 0 and x != 0:
            print("")
        for y in range(len(sudoku[0])):
            if y % 3 == 0 and y != 0:
                print(" ", end="")
            if y == 8:
                print(sudoku[x][y])
            else:
                print(str(sudoku[x][y]) + " ", end="")

def humano():
    print("Digite linha por linha da tabela do sudoku resolvida, para ser verificado.")
    sudoku_aux = []
    for i in range(1,10):
        sudoku_aux.append(list(map(int,input().strip().split())))
    return(sudoku_aux)

def bfs():
    print("Busca por largura")

def dfs():
    print("Busca por profundidade")

def selecaoAgente():
    print("1- Agente Humando")
    print("2- BFS")
    print("3- DFS")
    escolha = int(input())
    if escolha == 1:
        humano()
    elif escolha == 2:
        bfs()
    elif escolha == 3:
        dfs()


if __name__ == '__main__':
    iniciar_jogo()
    print("")
    selecaoAgente()
