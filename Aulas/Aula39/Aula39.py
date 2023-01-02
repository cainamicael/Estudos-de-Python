import json 

with open('C:/Users/cmcai/Desktop/jogador.json') as f: #tem que substituir \ por /
    jogador = json.load(f) #indentado e load nao loads

#chaves
for x in jogador:
    print(x)

#itens
for x in jogador.items():
    print(x)

#valores
for x in jogador.values():
    print(x)

#nome do jogador
print(jogador['nome'])

#itens da mochila
for x in jogador['mochila']:
    print(x)

#imprimir aeronaves
for x in jogador['aeronaves']:
    print(str(x['tipo']) + ' : ' + str(x['habilidade']))
