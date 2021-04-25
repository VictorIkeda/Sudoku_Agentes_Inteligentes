# from jogo import atualizarMundo 
# import acoes
# from regras_jogo.regras_sudoku import regras
# class tipos():
#     def selecaoAgente(self):
#         print("1- Agente Humando")
#         print("2- BFS")
#         print("3- DFS")
#         escolha = int(input())
#         if escolha == 1:
#             self.humano()
#         elif escolha == 2:
#             self.bfs()
#         elif escolha == 3:
#             self.dfs()
            
#     def humano(self):
#         try:
#             x,y,v = acao.acao().comando()
#             atualizarMundo(x,y,v)
#         except:
#             self.selecaoAgente()

#     def bfs(self):
#         print("Busca por largura")

#     def dfs(self):
#         print("Busca por profundidade")

from enum import Enum

class TiposAgentes(Enum):
    PREPOSTO_HUMANO = 'Preposto humano'
    AUTO_BFS = 'Automático BFS'
    AUTO_DFS = 'Automático DFS'