import time
from regras_jogo.regras_sudoku import construir_jogo
from regras_jogo.personagens import Personagens
from agentes import construir_agente
from agentes.tipos import TiposAgentes


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
    agente_jogador = construir_agente(TiposAgentes.auto_gbfs, Personagens.JOGADOR_SUDOKU)
    
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
    
    #Mostra a tabuleiro final
    ambiente_perceptivel = jogo.gerarCampoVisao(personagem_jogador) 
    agente_jogador.adquirirPercepcao(ambiente_perceptivel)

if __name__ == '__main__':
    iniciar_jogo()

