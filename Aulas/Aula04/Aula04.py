x = 1
n1=5;n2=2;x=complex(n1,n2)
x = ['carro','moto','avião','navio', False, 1.15] #list / Array
x = ('carro','moto','avião','navio', False, 1.15) #tupla
x = range(0, 100, 1) #list
x = {
    'canal':'cfb cursos',
    'curso':'Python'
}#Dict
x = {5,7,4,5,7,4,8} #Não repete os valores
x = frozenset({5,7,4,5,7,4,8}) #congela o set

print('Valor' + str(x))
print('Tipo: ' + str(type(x)))

print(x, "é o valor")