import random
import os

erros = 0
sorteado = random.randrange(0,100)
jogador = int(input('Digite seu numero: '))

while sorteado != jogador :
    os.system('cls')
    if sorteado > jogador :
        print('Erro, o número é maior')
    elif sorteado < jogador:
        print('Erro, o número é menor')
    erros += 1
    jogador = int(input('Digite seu numero: '))

print(f'Número: {str(jogador)} | Você acertou depois de {int(erros+1)} tentativas!')
