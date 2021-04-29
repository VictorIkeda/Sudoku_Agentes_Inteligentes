from queue import Queue

class No():
    def __init__(self, estado, acoes=None):
        self.estado = estado
        self.acoes = acoes

    def caminho_acoes(self, problema):
        return [self.criar_no_filho(problema, acoes)
                for acoes in problema.acoes(self.estado)]

    def criar_no_filho(self, problema, acoes):
        proximo = problema.resultado(self.estado, acoes)
        return No(proximo, acoes)

def busca_em_arvore(problema):
    folha = No(problema.tabela)
    if problema.teste_objetivo(folha.estado):
        return folha
    borda = Queue()
    borda.put(folha)
    while (borda.qsize() != 0):
        folha = borda.get()
        for filho in folha.caminho_acoes(problema):
            if problema.teste_objetivo(filho.estado):
                return filho
            borda.put(filho)
    return None

busca_arvore_bfs = busca_em_arvore
