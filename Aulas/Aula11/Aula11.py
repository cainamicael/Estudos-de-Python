clima = 'sol'
dinheiro = 650
lugar = ''

if clima=='sol' or (dinheiro>300 and dinheiro<= 500): #O dinheiro tem que estar nessa faixa
    lugar = 'clube'
else:
    lugar = 'cinema'

print(f'Vou ao {lugar}!')

"""
a = 10
b = 5
res = 0
op = '/'
if op == '-':
    res = a-b
elif op == '+':
    res = a+b

elif op == '*':
    res = a*b

elif op == '/':
    res = a/b

else:
    print("Digite um operador válido!")

print(f'Operação: {a} {op} {b} = {res}')
print("fim do programa")"""

print('fim')