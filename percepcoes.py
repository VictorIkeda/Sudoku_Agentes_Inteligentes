from dataclasses import dataclass
from typing import Optional, Tuple, Set
from typing import List
@dataclass
class PercepcoesJogador():
    '''Coloque aqui atributos que descrevam as percepções possíveis de
    mundo por parte do agente jogador
    
    Vide documentação sobre dataclasses em python.
    '''
    sudoku_valor: List[int]
        
    