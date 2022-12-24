valores = [1, 2, 3, 4, 5]
def somar (lista):
    s = 0
    for numero in lista:
        s += numero
    return s 

resultado = somar(valores)
print(resultado)