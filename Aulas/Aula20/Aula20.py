def somar(*num):
    soma = 0
    for n in num:
        soma += n
    print(soma)

def textos(*txt):
    for t in txt:
        print(t)

def carro(c = 'Golf'):
    print(f'O modelo do carro é: {c}')

somar(5, 7, 3, 2)
somar(2, 20, 80)
somar(1, 2)
textos('CFB cursos', 'Python', 'canal', 'curso', 'computador')
textos('CFB cursos', 'Python', 'canal')
textos('CFB cursos', 'Python')
textos('Aula')
carro('hrv')

