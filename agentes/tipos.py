from jogo import atualizarMundo, mostrarMundo
import acao

class tipos():
    def selecaoAgente(self):
        print("1- Agente Humando")
        print("2- BFS")
        print("3- DFS")
        escolha = int(input())
        if escolha == 1:
            self.humano()
        elif escolha == 2:
            self.bfs()
        elif escolha == 3:
            self.dfs()
            
    def humano(self):
        try:
            x,y,v = acao.acao().comando()
            atualizarMundo(x,y,v)
        except:
            self.selecaoAgente()

    def bfs(self):
        print("Busca por largura")

    def dfs(self):
        print("Busca por profundidade")

