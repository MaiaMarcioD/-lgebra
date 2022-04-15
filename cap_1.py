
class Matriz:
    
    def __init__(self, m, n, elementos = [], aleatorio = True):

        self.linhas = m
        self.colunas = n
        self.elementos = elementos
        self.aleatorio = aleatorio

    def __add__(self, other):

        for ij in range(len(self.elementos)):
            self.elementos[ij] += other.elementos[ij]

        contador = 0
        contador1 = 0
        for i in range(len(self.elementos)):
            contador += 1 

            if contador == self.colunas:
                contador = 0
                contador1 += 1


                if contador1 * self.colunas == len(self.elementos):
                    print(self.elementos[-self.colunas:])

                if contador1 == 1:

                    print(self.elementos[0: i +1 ])

                if contador1 * self.colunas != len(self.elementos) and contador1 != 1:
                    
                    print(self.elementos[i-1: i+self.colunas - 1])