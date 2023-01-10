from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id' : 1,
        'Título' : 'Bíblia',
        'Autor' : 'Deus'
    },
    {
        'id' : 2,
        'Título' : 'O Peregrino',
        'Autor' : ' John Bunyan'
    },
    {
        'id' : 3,
        'Título' : 'Pai Rico, Pai Pobre',
        'Autor' : 'Robert Kiyosaki e Sharon Lechter'
    }
]

#consultar todos
@app.route('/livros',methods=['GET']) #Garanto que a requisição só funciona com o método GET
def obter_livros():
    return jsonify(livros)

#consultar por id
@app.route('/livros/<int:id>',methods=['GET'])#Faço a tipagem do id
def obter_livro_por_id(id):
    for livro in livros:
        if  livro.get('id') == id:
            return jsonify(livro)

#editar
@app.route('/livros/<int:id>',methods=['PUT'])
def editar_livro_por_id(id):
    livro_alterado = request.get_json()#Retorna as informações escritas pelo usuário para a api
    for indice,livro in enumerate(livros): #Para ter o indice do livro e para percorrer para conseguir o id
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])

#criar
@app.route('/livros',methods=['POST'])
def incluir_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(livros)

#excluir
@app.route('/livros/<int:id>',methods=['DELETE'])
def excluir_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
            
    return jsonify(livros)


app.run(port=5000, host='localhost',debug=True) #rodar a api