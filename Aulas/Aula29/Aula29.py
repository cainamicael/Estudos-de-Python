carros = ['Hrv', 'Polo', 'Jetta', 'Cruze', 'Fusion', 'Golf', 'Focus', 'Onix', 'Fit']

itCarros = iter(carros) # __iter__ __next__

while itCarros:
    try:
        print(next(itCarros))
    except StopIteration:
        print('Fim da Lista')
        break
