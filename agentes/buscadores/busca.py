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
    estados = []
    folha = No(problema.tabela)
    if problema.teste_objetivo(folha.estado):
        return folha
    borda = Queue()
    borda.put(folha)
    while (borda.qsize() != 0):
        folha = borda.get()
        for filho in folha.caminho_acoes(problema):
            estados.append([filho.acoes[1],filho.acoes[2],filho.acoes[0]])
            if problema.teste_objetivo(filho.estado):
                return estados
            borda.put(filho)
    return None

def busca_em_arvore_DFS(problema):
    estados = []
    folha = No(problema.tabela)
    if problema.teste_objetivo(folha.estado):
        return folha.estado
    pilha = []
    pilha.append(folha)
    while pilha:
        no = pilha.pop()
        if no.acoes != None:
            estados.append([no.acoes[1],no.acoes[2],no.acoes[0]])
        if problema.teste_objetivo(no.estado):
            return estados
        pilha.extend(no.caminho_acoes(problema)) 
    return None

busca_arvore_bfs = busca_em_arvore
busca_arvore_dfs = busca_em_arvore_DFS
