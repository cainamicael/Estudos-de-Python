import sqlite3
from sqlite3 import Error

def conexao_banco(caminho):
    try:
        conexao = sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return conexao
    
vcon = conexao_banco('C:\\Users\\cmcai\\Documents\\GitHub\\Estudos de Python\\Estudos-de-Python\\Aulas\\Banco\\agenda.db')

def consulta(conexao, sql):
    cursor = conexao.cursor()
    cursor.execute(sql) #Na Consulta não precisa de commit
    resultado = cursor.fetchall() #Resulta em uma nova tabela com os registros que foram encontrados
    return resultado 

vsql = "SELECT * FROM tb_contatos WHERE T_NOMECONTATO LIKE 'B%'" #TODOS OS REGISTROS QUE COMEÇAM COM B

resultado = consulta(vcon, vsql)

#print(resultado) - retorna cada consulta em uma lista

for r in resultado:
    print(r)
