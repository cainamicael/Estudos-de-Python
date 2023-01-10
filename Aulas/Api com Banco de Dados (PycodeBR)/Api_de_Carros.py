from flask import Flask, make_response , jsonify, request
#from bd_fake import carros #Para usar o banco de dados fake 

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False #Para não deixar em ordem alfabética

#Consultar carros
@app.route('/carros',methods=['GET'])
def get_carros():
    return make_response( #Para construir uma resposta
        jsonify(
            mensagem = 'Lista de Carros',
            dado = carros
        )
    )

@app.route('/carros',methods=['POST'])
def create_carro():
    novo_carro = request.get_json()
    carros.append(novo_carro)
    return make_response(
        jsonify(
            mensagem = 'Carro cadastrado com sucesso!',
            dado = carros
        )
        )

app.run()