num = 'Bruno'

if not type(num) is int: #comparação de tipos
    raise Exception('Somente numeros permitidos') #cria a excessão
else:
    print(num)