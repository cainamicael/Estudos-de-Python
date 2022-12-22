t_carros = ('hrv','golf','argo')
l_carros = list(t_carros)
l_carros[2] = 'focus'
t_carros = tuple(l_carros)

for carro in t_carros:
    print(carro)