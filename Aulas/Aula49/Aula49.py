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

nome = input('Nome: ')
telefone = input('Telefone: ')
email = input('Email: ')

vsql = f"INSERT INTO tb_contatos (T_NOMECONTATO, T_TELEFONECONTATO, T_EMAILCONTATO) VALUES('{nome}', '{telefone}', '{email}')" #O tipo de aspas tem q ser diferente dentro do comando


def inserir(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit() #É para manter o registro na tabela 
        print('Registro inserido')
    except Error as ex:
        print(ex)

inserir(vcon, vsql)

