from regras_jogo.regras_sudoku import regras
from agentes import tipos

tabela = regras().gerarMundo()

def iniciar_jogo():
    print("Tabuleiro do sudoku \n")
    global tabela
    mostrarMundo(tabela)

def atualizarMundo(x,y,v):
    global tabela
    tabela[int(x)][int(y)] = int(v)
    print("")
    mostrarMundo(tabela)

def mostrarMundo(sudoku):
    for i in range(len(sudoku)):
        if i % 3 == 0 and i != 0:
            print("")
        for j in range(len(sudoku[0])):
            if j % 3 == 0 and j != 0:
                print("  ", end="")
            if j == 8:
                print(sudoku[i][j])
            else:
                print(str(sudoku[i][j]) + " ", end="")


if __name__ == '__main__':
    iniciar_jogo()
    print("")
    tipos.tipos().selecaoAgente()
    # mostrarMundo(tabela)
    
