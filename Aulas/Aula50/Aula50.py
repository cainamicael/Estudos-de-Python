import sqlite3
from sqlite3 import Error

def conexaoBanco():
    caminho = 'C:\\Users\\cmcai\\Documents\\GitHub\\Estudos de Python\\Estudos-de-Python\\Aulas\\Banco\\agenda.db'
    try:
        con = sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return con

vcon = conexaoBanco()

#deletar
def deletar(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
    except Error as ex:
        print(ex)
    finally:
        print('Registro Removido')

vsql = "DELETE FROM tb_contatos WHERE N_IDCONTATO = 2"

deletar(vcon, vsql)