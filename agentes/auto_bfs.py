from percepcoes import PercepcoesJogador
from agentes.abstrato import AgenteAbstrato
from acoes import AcaoJogador
from .problemas.sudoku import ProblemaSudoku
from .buscadores.busca import busca_arvore_bfs

class AgenteAutomaticoBfs(AgenteAbstrato):
    def __init__(self) -> None:
        super().__init__()

        self.problema: ProblemaSudoku = None
        self.solucao: list = None

    def adquirirPercepcao(self, percepcao_mundo: PercepcoesJogador):
        ''' Forma uma percepcao interna por meio de seus sensores, a partir das
        informacoes de um objeto de visao de mundo.
        '''
        AgenteAutomaticoBfs.desenhar_tabuleiro(percepcao_mundo)

        if not self.solucao:
            self.problema = ProblemaSudoku()

    def escolherProximaAcao(self):
        if not self.solucao:
            no_solucao = busca_arvore_bfs(self.problema)
            self.solucao = no_solucao.caminho_acoes()
            print(len(self.solucao), self.solucao)
            if not self.solucao:
                raise Exception("Agente BFS não encontrou solução.")
        
        acao = self.solucao.pop(0)
        print(f"Próxima ação é {acao}.")


        x, y, v = acao[1],acao[2],acao[0]
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