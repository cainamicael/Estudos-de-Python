carros = {
    'Carro1' : {
        'Fabricante' : 'honda',
        'Modelo' : 'hrv'
    },
    'Carro2' : {
        'Fabricante' : 'Volksvagen',
        'Modelo' : 'golf'
    },
    'Carro3' : {
        'Fabricante' : 'ford',
        'Modelo' : 'focus'
    }
}

print(carros['Carro1']['Fabricante']) #f1
print(carros.get('Carro2').get('Modelo')) #f2
