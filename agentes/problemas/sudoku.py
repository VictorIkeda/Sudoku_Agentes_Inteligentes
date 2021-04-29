import copy

class ProblemaSudoku(object):
    
    def __init__(self, tabela):
        self.tabela = tabela
        self.tamanho = len(tabela) 
        self.altura = int(self.tamanho/3) 


    def valores_nao_utilizado(self, valor, valor2):
        return [i for i in valor if i not in valor2]

    def vazio(self, tabela, estado):
        for x in range(tabela):
            for y in range(tabela):
                if estado[x][y] == 0:
                    return x, y   

    def estado_inicial():
        sudoku_completo = [[0, 6, 0, 0, 4, 3, 8, 7, 2], [1, 0, 2, 0, 7, 0, 5, 3, 6], [0, 0, 0, 2, 6, 5, 4, 0, 1], [7, 3, 1, 5, 0, 4, 9, 0, 8], [0, 5, 0, 0, 8, 0, 0, 4, 3], [6, 8, 0, 3, 0, 9, 2, 5, 0], [5, 2, 6, 0, 0, 0, 0, 8, 0], [0, 1, 0, 8, 9, 7, 6, 2, 0], [8, 0, 0, 6, 0, 0, 0, 1, 4]]
        return sudoku_completo

    def acoes(self, estado):
        valor = range(1, self.tamanho+1) 
        coluna = [] 
        aux = [] 

        x,y = self.vazio(self.tamanho, estado) 

        linha = [i for i in estado[x] if (i != 0)]
        valores = self.valores_nao_utilizado(valor, linha)

        for j in range(self.tamanho):
            if estado[j][y] != 0:
                coluna.append(estado[j][y])
        valores = self.valores_nao_utilizado(valores, coluna)

        linhaValida = int(x/self.altura)*self.altura
        colunaValida = int(y/3)*3
        
        for i in range(self.altura):
            for j in range(3):
                aux.append(estado[linhaValida + i][colunaValida + j])
        valores = self.valores_nao_utilizado(valores, aux)

        for i in valores:
            yield i, x, y

    def resultado(self, estado, acoes):
        novo_estado = copy.deepcopy(estado)
        novo_estado[acoes[1]][acoes[2]] = acoes[0]
        # print("X: ",acoes[1], " Y: ", acoes[2]," Valor: ", acoes[0])
        # print(novo_estado,"\n")
        # print novo_estado ira exibir o estado atual
        return novo_estado


    def teste_objetivo(self, estado):
        for x in range(len(estado)):
            for y in range(len(estado[0])):
                if estado[x][y] == 0:
                    return False
        for i in estado:
            if sorted(list(set(i))) != sorted(i):
                return False
        coluna = []
        for j in range(len(estado)):
            for i in estado:
                coluna += [i[j]]
            if sorted(list(set(coluna))) != sorted(coluna):
                return False
            coluna = []
        return True
    
    def custo(EstadoRestaUm, resultante):
        """Custo em quantidade de jogadas"""
        return 1