class Npc: #pai/super
    def __init__(self, nome, time, forca, municao):
        self.nome = nome
        self.time = time
        self.forca = forca
        self.municao = municao
        self.vivo = True
        self.energia = 100

    def info(self):
        print(f'Nome...: {self.nome}')
        print(f'Time...: {self.time}')
        print(f'Forca..: {self.forca}')
        print(f'Municao: {self.municao}')
        print('Vivo: {}'.format('Sim' if self.vivo else 'Nao'))
        print(f'Energia: {self.energia}')
        print('\n')

class Soldado(Npc):
    def __init__(self, nome, time):#Vai sobrescrever o construtor da classe pai
        self.forca = 200
        self.municao = 200
        super().__init__(nome, time, self.forca, self.municao)#Passa as informações para a superclasse. O super disponibiliza tudo da classe pai

class Guarda(Npc):
    def __init__(self, nome, time):
        self.forca = 100
        self.municao = 20
        super().__init__(nome, time, self.forca, self.municao)

class Elite(Npc):
    def __init__(self, nome, time):
        self.forca = 400
        self.municao = 500
        super().__init__(nome, time, self.forca, self.municao)
    def inf(self):
        super().info()

s1 = Guarda('Olho Vivo', 1)
s2 = Soldado('Bala na Agulha', 1)
s3 = Elite('Ninja', 1)
s4 = Guarda('Super Atento', 2)
s5 = Soldado('Tiro Certo', 2)
s6 = Elite('Samurai', 2)

s1.vivo = False
s6.vivo = False

s1.info()
s2.info()
s3.info()
s4.info()
s5.info()
s6.inf()