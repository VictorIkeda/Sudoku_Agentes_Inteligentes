from agentes import auto_gbfs
from enum import Enum

class TiposAgentes(Enum):
    PREPOSTO_HUMANO = 'Preposto humano'
    AUTO_BFS = 'Automático BFS'
    AUTO_DFS = 'Automático DFS'
    A_Star = 'A estrela'
    auto_gbfs = 'Automatico gulosa'