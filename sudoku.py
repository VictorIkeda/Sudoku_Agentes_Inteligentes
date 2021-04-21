def humano():
    print("agente humano")

def bfs():
    print("Busca por largura")

def dfs():
    print("Busca por profundidade")

if __name__ == '__main__':
    while(True):
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