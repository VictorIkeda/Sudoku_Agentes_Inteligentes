from percepcoes import PercepcoesJogador
from agentes.abstrato import AgenteAbstrato
from acoes import AcaoJogador
from .Heuristica.heuristica_sudoku import heuristica
from .buscadores.busca import busca_arvore_gbfs
import time

class AgenteAutomaticoGbfs(AgenteAbstrato):
    def __init__(self) -> None:
        super().__init__()
        self.problema: heuristica = heuristica(heuristica.estado_inicial())
        self.no_solucao = busca_arvore_gbfs(self.problema)
        print(self.no_solucao)

    def adquirirPercepcao(self, percepcao_mundo: PercepcoesJogador):
        ''' Forma uma percepcao interna por meio de seus sensores, a partir das
        informacoes de um objeto de visao de mundo.
        '''
        AgenteAutomaticoGbfs.desenhar_tabuleiro(percepcao_mundo)


    def escolherProximaAcao(self):
        acao = self.no_solucao.pop(0)
        x, y, v = int(acao[0]), int(acao[1]), int(acao[2])
        print(f"\n A proxima acao sera em X: {x} Y: {y} colocando o valor {v} \n")
        time.sleep(1)
        return AcaoJogador.adicionar_valor(x, y, v)
    
    def desenhar_tabuleiro(percepcao_mundo: PercepcoesJogador):
        for i in range(len(percepcao_mundo)):
            if i % 3 == 0 and i != 0:
                print("")
            for j in range(len(percepcao_mundo[0])):
                if j % 3 == 0 and j != 0:
                    print(" ", end="")
                if j == 8:
                    print(str(percepcao_mundo[i][j]))
                else:
                    print(str(percepcao_mundo[i][j]) + " ", end="")