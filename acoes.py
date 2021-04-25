from enum import Enum
from dataclasses import dataclass

class AcoesJogador(Enum):
    ADICIONAR_VALOR = 'AdicionarValor'

@dataclass
class AcaoJogador():
    tipo: str
    parametros: tuple = tuple()

    @classmethod
    def adicionar_valor(cls, x:int, y:int, valor: int)-> 'AcaoJogador':
        return cls(AcoesJogador.ADICIONAR_VALOR,(x,y,valor))
    