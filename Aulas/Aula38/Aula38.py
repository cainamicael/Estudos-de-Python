import json

jogador_d = {
    "nome": "Bruno",
    "time": "aviadores",
    "vivo": "True",
    "energia": 100,
    "mochila": ["pederneira", "corda", "linha", "arame"],
    "aeronaves": [
        {"tipo": "transporte", "habilidade": 80},
        {"tipo": "ataque", "habilidade": 100},
        {"tipo": "reconhecimento", "habilidade": 50}
    ]
}

jogador_j = json.dumps(jogador_d)

jogador = json.loads(jogador_j)

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


