from percepcoes import PercepcoesJogador
from agentes.abstrato import AgenteAbstrato
from acoes import AcaoJogador
class AgentePrepostoESHumano(AgenteAbstrato):
    
    def adquirirPercepcao(self, percepcao_mundo: PercepcoesJogador):
        """ Inspeciona a disposicao dos elementos no objeto de visao e escreve
        na tela para o usuário saber o que seu agente está percebendo.
        """
        
        print("\n Sudoku")
        for i in range(len(percepcao_mundo)):
            if i % 3 == 0 and i != 0:
                print("")
            for j in range(len(percepcao_mundo[0])):
                if j % 3 == 0 and j != 0:
                    print(" ", end="")
                if j == 8:
                    print(str(percepcao_mundo[i][j]))
                else:
                    print(str(percepcao_mundo[i][j]) + " ", end="")
    
    def escolherProximaAcao(self):
        print("digite a cordenada que deseja motificar")
        print("cordenada x")
        x = int(input())
        if(x > 9):
            print("comando invalido")
        else:
            print("cordenada y")
            y = int(input())
            if(y > 9):
                print("comando invalido")
            else:
                print("valor que deseja adicionar")
                valor = int(input())
                if (valor > 9):
                    print("valor invalido")
                else:
                    return AcaoJogador.adicionar_valor(x,y,valor)
