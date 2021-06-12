from .humano import AgentePrepostoESHumano
from .auto_bfs import AgenteAutomaticoBfs
from .auto_dfs import AgenteAutomaticoDfs
from .a_star import AgenteAEstrela
from .auto_gbfs import AgenteAutomaticoGbfs
from .tipos import TiposAgentes

def construir_agente(*args, **kwargs):
    """ Método factory para uma instância Agente arbitrária, de acordo com os
    paraâmetros. Pode-se mudar à vontade a assinatura do método.
    """
    tipo_agente = args[0]
    if tipo_agente == TiposAgentes.PREPOSTO_HUMANO:
        return AgentePrepostoESHumano()
    if tipo_agente == TiposAgentes.AUTO_BFS:
        return AgenteAutomaticoBfs()
    if tipo_agente == TiposAgentes.AUTO_DFS:
        return AgenteAutomaticoDfs()
    if tipo_agente == TiposAgentes.A_Star:
        return AgenteAEstrela()
    if tipo_agente == TiposAgentes.auto_gbfs:
        return AgenteAutomaticoGbfs()
    
    raise ValueError("Não foi escolhido nenhum tipo de agente válido.")