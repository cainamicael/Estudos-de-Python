matriz = [[0,0,0],[0,0,0],[0,0,0]]
for linha in range (0,3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f'Digite o valor da posição [{linha}][{coluna}]: '))

for linha in matriz:
    print(linha)