from dataclasses import dataclass
from typing import Optional, Tuple

@dataclass
class PercepcoesJogador():
    '''Coloque aqui atributos que descrevam as percepções possíveis de
    mundo por parte do agente jogador
    
    Vide documentação sobre dataclasses em python.
    '''

    sudoku: list(map(int,[]))
    