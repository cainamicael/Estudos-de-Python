import sqlite3
from sqlite3 import Error


#Criar conexão
def conexaoBanco():
    caminho = 'C:\\Users\\cmcai\\Documents\\GitHub\\Estudos de Python\\Estudos-de-Python\\Aulas\\Banco\\agenda.db'
    con = None
    try:
        con = sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return con

vcon = conexaoBanco()

#criar tabela
vsql = """CREATE TABLE tb_contatos(
                N_IDCONTATO INTEGER PRIMARY KEY AUTOINCREMENT,
                T_NOMECONTATO VARCHAR(30),
                T_TELEFONECONTATO VARCHAR(14),
                T_EMAILCONTATO VARCHAR(30)
        );""" #As 3 aspas servem para poder dar enter

def criarTabela(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        print('Tabela Criada')
    except Error as ex:
        print(ex)

criarTabela(vcon, vsql)
vcon.close()