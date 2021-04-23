
class acao():
    def comando(self):
        # print("Digite linha por linha da tabela do sudoku resolvida, para ser verificado.")
        # sudoku_aux = []
        # for i in range(1,10):
        #     sudoku_aux.append(list(map(int,input().strip().split())))
        # return(sudoku_aux)
        print("digite a cordenada que deseja motificar")
        print("cordenada x")
        x = input()
        if(int(x) > 9):
            print("comando invalido")
        else:
            print("cordenada y")
            y = input()
            if(int(y) > 9):
                print("comando invalido")
            else:
                print("valor que deseja adicionar")
                valor = input()
                if (int(valor) > 9):
                    print("valor invalido")
                else:
                    return x,y,valor