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

def atualizar(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
    except Error as ex:
        print(ex)
    finally:
        print('Registro Atualizado')

vsql = "UPDATE tb_contatos SET T_NOMECONTATO = 'Bruno', T_TELEFONECONTATO = '81988888888', T_EMAILCONTATO = 'CM@GMAIL.COM' WHERE N_IDCONTATO = 1"

atualizar(vcon, vsql)
