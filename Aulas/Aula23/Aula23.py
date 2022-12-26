class Carro:
    velMax = 0
    ligado = False
    cor = ''

c1 = Carro()
c2 = Carro()
c3 = Carro()

c1.velMax = 200
c1.cor = 'Preto'
c1.ligado = False

print(f'A velodidade máxima de c1 é {c1.velMax} km/h')
print(f'A velodidade cor de c1 é {c1.cor}!')
print(f'C1 está {c1.ligado}!')
