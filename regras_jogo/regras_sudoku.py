from .regras_abstratas import AbstractRegrasJogo
from .personagens import Personagens
from percepcoes import PercepcoesJogador
from acoes import AcoesJogador

class RegrasSudoku(AbstractRegrasJogo):
    def __init__(self) -> None:
        super().__init__()
        sudoku_completo = [[0, 6, 0, 0, 4, 3, 8, 7, 2], [1, 0, 2, 0, 7, 0, 5, 3, 6], [0, 0, 0, 2, 6, 5, 4, 0, 1], [7, 3, 1, 5, 0, 4, 9, 0, 8], [0, 5, 0, 0, 8, 0, 0, 4, 3], [6, 8, 0, 3, 0, 9, 2, 5, 0], [5, 2, 6, 0, 0, 0, 0, 8, 0], [0, 1, 0, 8, 9, 7, 6, 2, 0], [8, 0, 0, 6, 0, 0, 0, 1, 4]]
        self.tabuleiro = sudoku_completo
        self.original = sudoku_completo
        self.id_personagens = {Personagens.JOGADOR_SUDOKU: 0}
        self.acoes_personagens = {0: None}
        self.msg_jogador = None

    
    def registrarAgentePersonagem(self, personagem):
        """ Cria ou recupera id de um personagem agente.
        """
        return self.id_personagens[personagem]
    
    
    def isFim(self):
        """ Boolean indicando fim de jogo em True.
        """
        for x in range(len(self.tabuleiro)):
            for y in range(len(self.tabuleiro[0])):
                if self.tabuleiro[x][y] == 0:
                    return False
        for i in self.tabuleiro:
            if sorted(list(set(i))) != sorted(i):
                return False
        coluna = []
        for j in range(len(self.tabuleiro)):
            for i in self.tabuleiro:
                coluna += [i[j]]
            if sorted(list(set(coluna))) != sorted(coluna):
                return False
            coluna = []
        return True

    
    def gerarCampoVisao(self, id_agente):
        """ Retorna um EstadoJogoView para ser consumido por um agente
        específico. Objeto deve conter apenas descrição de elementos visíveis
        para este agente.

        EstadoJogoView é um objeto imutável ou uma cópia do jogo, de forma que
        sua manipulação direta não tem nenhum efeito no mundo de jogo real.
        """
        
        sudoku = self.tabuleiro
        percepcoes_jogador = PercepcoesJogador(
            sudoku_valor=list[self.tabuleiro]
        )
        return sudoku

    
    def registrarProximaAcao(self, id_agente, acao) -> None:
        """ Informa ao jogo qual a ação de um jogador especificamente.
        Neste momento, o jogo ainda não é transformado em seu próximo estado,
        isso é feito no método de atualização do mundo.
        """
        self.acoes_personagens[id_agente] = acao
    
    
    def atualizarEstado(self, diferencial_tempo):
        """ Apenas neste momento o jogo é atualizado para seu próximo estado
        de acordo com as ações de cada jogador registradas anteriormente.
        """
        acao_jogador = self.acoes_personagens[self.id_personagens[Personagens.JOGADOR_SUDOKU]]
        try:
            if acao_jogador.tipo == AcoesJogador.ADICIONAR_VALOR:
                x , y, valor = acao_jogador.parametros
                # if self.tabuleiro[x][y] == 0:
                self.tabuleiro[int(x)][int(y)] = int(valor)
                # else:
                    # print("\n ===== Só pode alterar os valores que estão vazios(Representado por 0) =====\n")
        except:
            print("Numeros acima de 9 ou letras nao sao permitidos")
    
    
    def terminarJogo(self):
        """ Faz procedimentos de fim de jogo, como mostrar placar final,
        gravar resultados, etc...
        """
        return

def construir_jogo(*args,**kwargs):
    """ Método factory para uma instância RegrasJogo arbitrária, de acordo com os
    parâmetros. Pode-se mudar à vontade a assinatura do método.
    """
    return RegrasSudoku()