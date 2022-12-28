import os
carros = []

class Carro:
    nome = ''
    pot = 0
    velMax = 0
    ligado = False

    def __init__ (self, nome, pot):
        self.nome = nome
        self.pot = pot
        self.velMax = int(pot*2)

    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print('Carro Ligado')
        else:
            print('O carro ja esta ligado!')

    def desligar(self):
        if self.ligado:
            self.ligado = False
            print('Carro desligado')
        else:
            print('O carro ja esta desligado!')
    
    def info(self):
        print(f'Nome.............: {self.nome}')
        print(f'Potencia.........: {self.pot}')
        print(f'Velocidade maxima: {self.velMax} km/h')
        print('Ligado............: {}'.format('Sim' if self.ligado else 'Não'))

def Menu():
    os.system('cls') or None
    print('1 - Novo Carro')
    print('2 - Informacoes do Carro')
    print('3 - Excluir Carro')
    print('4 - Ligar Carro')
    print('5 - Desligar Carro')
    print('6 - Listar Carros')
    print('7 - Sair')
    print(f'Quantidade de carros: {len(carros)}')
    opc = int(input('Digite uma opcao: '))
    return opc

def novoCarro():
    os.system('cls') or None
    n = input('Nome do carro: ')
    p = int(input('Potencia do carro'))
    carro = Carro(n, p)
    carros.append(carro)
    print('Novo carro criado')
    print('O número do seu carro é: {}'.format(len(carros) - 1))
    os.system('pause')

def Informacoes():
    os.system('cls') or None
    n = int(input('Informe o número do carro que você deseja ter informacoes: '))
    try:
        carros[n].info()
    except:
        print('Carro não existe na lista')
    os.system('pause')

def excluirCarro():
    os.system('cls') or None
    n = int(input('Informe o número do carro que você deseja excluir: '))
    try:
        del carros[n]
    except:
        print('Carro não existe na lista')
    os.system('pause')


def ligarCarro():
    os.system('cls') or None
    n = int(input('Informe o número do carro que você deseja ligar: '))
    try:
        carros[n].ligar()
    except:
        print('Carro não existe na lista')
    os.system('pause')

def  desligarCarro():
    os.system('cls') or None
    n = int(input('Informe o número do carro que você deseja desligar: '))
    try:
        carros[n].desligar()
    except:
        print('Carro não existe na lista')
    os.system('pause')

def  listarCarro():
    os.system('cls') or None
    p = 0
    for c in carros:
        print(f'Posicao: {p}')
        print(f'Nome...: {c.nome}')
        p += 1
    os.system('pause')

    







