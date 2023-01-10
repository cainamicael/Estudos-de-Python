import sqlite3
from sqlite3 import Error
import os

def conexao(caminho):
    try:
        con = sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return con

conexao = conexao('C:\\Users\\cmcai\\Documents\\GitHub\\Estudos de Python\\Estudos-de-Python\\Aulas\\Banco\\bd_carros.db')

def query(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
        print('Operação realizada')
    except Error as ex:
        print(ex)

def consultar(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        r = c.fetchall()
    except Error as ex:
        print(ex)
    for x in r:
        print(x)

def inserir():
    os.system('cls')
    marca = input('Digite a marca do carro: ')
    modelo = input('Digite o modelo do carro: ')
    ano = int(input('Digite o ano do carro: '))
    sql = f"INSERT INTO carros (marca, modelo, ano) VALUES ('{marca}', '{modelo}', {ano})"
    query(conexao, sql)

consultar(conexao, f"SELECT * FROM carros")






conexao.close()
