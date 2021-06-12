from queue import Queue
import heapq
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
        
def busca_em_arvore_BFS(problema):
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
                print("Resultado \n",filho.estado, "\n")
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
            print("Resultado \n", no.estado,"\n")
            return estados
        pilha.extend(no.caminho_acoes(problema)) 
    return None

def busca_em_A_estrela(problema):
    estado_atual = []
    folha = No(problema.tabela)
    novo_estado = Queue()
    novo_estado.put(folha)
    borda = []
    while (True):
        folha = novo_estado.get()
        for filho in folha.caminho_acoes(problema):
            estado_atual.append([filho.acoes[1],filho.acoes[2],filho.acoes[0]])
            if problema.isObjetivo(filho.estado):
                print("Resultado \n",filho.estado, "\n")
                return estado_atual
            else:
                novo_estado.put(filho)
                borda = problema.tabela
                heapq.heapify(borda)

def busca_em_arvore_GBFS(problema):
    estado_atual = []
    folha = No(problema.tabela)
    novo_estado = Queue()
    novo_estado.put(folha)
    borda = []
    while (True):
        folha = novo_estado.get()
        for filho in folha.caminho_acoes(problema):
            estado_atual.append([filho.acoes[1],filho.acoes[2],filho.acoes[0]])
            if problema.isObjetivo(filho.estado):
                print("Resultado \n",filho.estado, "\n")
                return estado_atual
            if problema.custo(borda) <= 1:
                novo_estado.put(filho)
                borda = problema.tabela
                heapq.heapify(borda)




busca_arvore_bfs = busca_em_arvore_BFS
busca_arvore_dfs = busca_em_arvore_DFS
A_estrela = busca_em_A_estrela
busca_arvore_gbfs = busca_em_arvore_GBFS
