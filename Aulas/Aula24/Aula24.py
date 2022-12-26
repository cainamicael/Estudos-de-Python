class Carro:
    velMax = 0
    ligado = False
    cor = ''

    def __init__(self, v, l, c):
        self.velMax = v
        self.ligado = l
        self.cor = c

    def mostar(self):
        print(f'A velodidade maxima eh {self.velMax} km/h!')
        print(f'A cor eh {self.cor}!')
        l = 'Ligado' if self.ligado else 'Desligado'
        print(f'O carro esta {l}!')
        print('\n')

    def ligar(self):
        self.ligado = True

    def desligar(self):
        self.ligado = False

    def andar(self):
        if(self.ligado):
            print('Andando')
        else:
            print('Carro desligado')

c1 = Carro(200, False, 'Preto')
c2 = Carro(120, False, 'Branco')
c3 = Carro(350, False, 'Vermelha')

c1.ligar()
c2.ligar()

c1.mostar()
c2.mostar()
c3.mostar()

c1.andar()
c2.andar()

