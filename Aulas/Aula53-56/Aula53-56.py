import os
import sqlite3
from sqlite3 import Error

#conexão com banco
def conexaoBanco(caminho):
    con = None
    try:
        con = sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return con 

vcon = conexaoBanco('C:\\Users\\cmcai\\Documents\\GitHub\\Estudos de Python\\Estudos-de-Python\\Aulas\\Banco\\agenda.db')

def query(conexao, sql): #Serve para insert, update e delete
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
    except Error as ex:
        print(ex)
    finally:
        print('Operacao realizada com sucesso! ')

def consultar(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        res = c.fetchall()
    except Error as ex:
        print(ex)
    return res

def menuPrincipal():
    os.system('cls')
    print('\n1 - Inserir novo Registro........')
    print('2 - Deletar Registro pelo ID.....')
    print('3 - Atualizar Registro pelo ID...')
    print('4 - Consultar Registro...........')
    print('5 - Consultar Registro pelo Nome. ')
    print('6 - Sair.........................')

def menuInserir():
    os.system('cls')
    nome = input('Digite o Nome: ')
    telefone = input('Digite o Telefone: ')
    email = input('Digite o Email: ')
    vsql = f"INSERT INTO tb_contatos (T_NOMECONTATO, T_TELEFONECONTATO, T_EMAILCONTATO) VALUES ('{nome}', '{telefone}', '{email}')" #ou pode ser '"+nome"'
    query(vcon, vsql)

def menuDeletar():
    os.system('cls')
    id = int(input('Digite o id que voce deseja atualizar: '))
    vsql = f"DELETE FROM tb_contatos WHERE N_IDCONTATO = {id}"
    query(vcon, vsql)

def menuAtualisar():
    os.system('cls')
    id = int(input('Digite o id que voce deseja atualizar: '))
    r = consultar(vcon, f"SELECT * FROM tb_contatos WHERE N_IDCONTATO = {id}")

    rnome = r[0][1]
    rtelefone = r[0][2]
    remail = r[0][3]

    nome = input('Digite o Nome: ')
    telefone = input('Digite o Telefone: ')
    email = input('Digite o Email: ')

    if (len(nome) == 0):
        nome = rnome
    if (len(telefone) == 0):
        telefone = rtelefone
    if (len(email) == 0):
        email = remail

    vsql = f"UPDATE tb_contatos SET T_NOMECONTATO = '{nome}', T_TELEFONECONTATO = '{telefone}', T_EMAILCONTATO = '{email}' WHERE N_IDCONTATO = {id}"
    query(vcon, vsql)

def menuConsultar():
    os.system('cls')
    vsql = "SELECT * FROM tb_contatos"
    r = consultar(vcon, vsql)
    vlimite = 10
    vcont = 0
    try:
        for x in r:
            print(f'ID: {x[0]} NOME: {x[1]} TELEFONE: {x[2]}  EMAIL: {x[3]}')
            vcont += 1
            if(vcont >= vlimite):
                vcont = 0
                os.system('pause')
                os.system('cls')
        print('Fim da Lista')
        os.system('pause')
    except Error as ex:
        print(ex)


def menuConsultarNomes():
    os.system('cls')
    nome = input('Digite o nome: ')
    vsql = f"SELECT * FROM tb_contatos WHERE T_NOMECONTATO LIKE '%{nome}%'"
    r = consultar(vcon, vsql)
    vlimite = 10
    vcont = 0
    try:
        for x in r:
            print(f'ID: {x[0]} NOME: {x[1]} TELEFONE: {x[2]}  EMAIL: {x[3]}')
            vcont += 1
            if(vcont >= vlimite):
                vcont = 0
                os.system('pause')
                os.system('cls')
        print('Fim da Lista')
        os.system('pause')
    except Error as ex:
        print(ex)

opcao = 0
while (opcao != 6):

    menuPrincipal()

    opcao = int(input('Digite uma opcao: '))

    if opcao == 1:
        menuInserir()
    elif opcao == 2:
        menuDeletar()
    elif opcao == 3:
        menuAtualisar()
    elif opcao == 4:
        menuConsultar()    
    elif opcao == 5:
        menuConsultarNomes()
    elif opcao == 6:
        os.system('cls')
        print('Programa Finalizado!')
    else:
        os.system('cls')
        print('Opção Invalida!')
        os.system('pause')

vcon.close()
os.system('pause')    
