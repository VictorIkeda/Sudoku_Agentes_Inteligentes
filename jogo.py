# from regras_jogo.regras_sudoku import regras
# from agentes import tipos
import time
from regras_jogo.regras_sudoku import construir_jogo
# from regras_jogo.regras_abstratas import construir_jogo
from regras_jogo.personagens import Personagens
from agentes.abstrato import construir_agente
from agentes.tipos import TiposAgentes

# tabela = regras().gerarMundo()

def ler_tempo(em_turnos=False):
    """ Se o jogo for em turnos, retorna a passada de 1 rodada.
    
    Se não for em turno, é continuo ou estratégico, retorna tempo
    preciso (ns) do relógio.
    """
    return 1 if em_turnos else time.time()

def iniciar_jogo():
    
    # Inicializar e configurar jogo
    jogo = construir_jogo()
    personagem_jogador = jogo.registrarAgentePersonagem(Personagens.JOGADOR_SUDOKU)
    agente_jogador = construir_agente(TiposAgentes.PREPOSTO_HUMANO, Personagens.JOGADOR_SUDOKU)
    
    tempo_de_jogo = 0
    while not jogo.isFim():
        
        # Mostrar mundo ao jogador
        ambiente_perceptivel = jogo.gerarCampoVisao(personagem_jogador)
        agente_jogador.adquirirPercepcao(ambiente_perceptivel)
        
        # Decidir jogada e apresentar ao jogo
        acao = agente_jogador.escolherProximaAcao()
        jogo.registrarProximaAcao(personagem_jogador, acao)
        
        # Atualizar jogo
        # tempo_corrente = ler_tempo()
        jogo.atualizarEstado(1)
        tempo_de_jogo += 1

# def iniciar_jogo():
#     print("Tabuleiro do sudoku \n")
#     global tabela
#     mostrarMundo(tabela)

# def atualizarMundo(x,y,v):
#     global tabela
#     aux = tabela
#     aux[int(x)][int(y)] = int(v)
#     print("")
#     mostrarMundo(aux)

    

# def mostrarMundo(sudoku):
#     for i in range(len(sudoku)):
#         if i % 3 == 0 and i != 0:
#             print("")
#         for j in range(len(sudoku[0])):
#             if j % 3 == 0 and j != 0:
#                 print(" ", end="")
#             if j == 8:
#                 print(sudoku[i][j])
#             else:
#                 print(str(sudoku[i][j]) + " ", end="")


if __name__ == '__main__':
    iniciar_jogo()
    # print("")
    # tipos.tipos().selecaoAgente()
    
