import sqlite3
from flask import Flask, make_response , jsonify, request
from bd_fake import carros #Para usar o banco de dados fake 

conexao = sqlite3.connect('C:\\Users\\cmcai\\Documents\\GitHub\\Estudos de Python\\Estudos-de-Python\\Aulas\\Banco\\bd_carros.db', check_same_thread=False) #Esse segundo parâmetro é para não dar o erro de thread

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False #Para não deixar em ordem alfabética

#Consultar carros
@app.route('/carros', methods=['GET'])
def get_carros():
    c = conexao.cursor()
    c.execute("SELECT * FROM carros")
    meus_carros = c.fetchall()

    carros = list()
    for carro in meus_carros:
        carros.append({
            'id' : carro[0],
            'marca' : carro[1],
            'modelo' : carro[2],
            'ano' : carro[3]
        })

        return make_response(
        jsonify(
            mensagem = 'Lista de Carros',
            dado = carros
            )
        )

#Criar carro
@app.route('/carros', methods=['POST'])
def create_carro():
    carro = request.json

    c = conexao.cursor()
    c.execute(f"INSERT INTO carros (marca, modelo, ano) VALUES ('{carro.get('marca')}', '{carro.get('modelo')}', '{carro.get('ano')}')")
    conexao.commit()

    return make_response(
        jsonify(
            mensagem = 'Lista de Carros',
            dado = carros
            )
        )

app.run(port=5000, host='localhost',debug=True)
conexao.close()