import sqlite3
from sqlite3 import Error

vcon = sqlite3.connect('C:\\Users\\cmcai\\Documents\\GitHub\\Estudos de Python\\Estudos-de-Python\\Aulas\\Banco\\agenda.db')

def dql(query): #select
    c = vcon.cursor()
    c.execute(query)
    res = c.fetchall()
    vcon.close()
    return res

def dml(query): #inset, update, delete
    c = vcon.cursor()
    c.execute(query)
    vcon.commit()
    vcon.close()


