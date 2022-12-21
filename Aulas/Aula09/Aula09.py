carros = ['Hrv','Golf','Argo','Focus']

carros.append('Fit')#add
carros.append('Fusion')
carros.append('Polo')

carros.remove('Fusion')
carros.pop()#Remove o último
del carros[2]#remover pelo índice

carros2 = list(carros)#copiar a lista

carros3 = ['Fusca','147','uno']

carros4 = carros+carros23

print(len(carros))
print(carros)
print(carros[0])
print(carros[-1])#O último elemento
print(carros[-2])#O penúltimo elemento