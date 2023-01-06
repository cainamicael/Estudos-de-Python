import os

nome = 'teste.txt'
caminho = 'C:/Users/cmcai/Documents/GitHub/Estudos de Python/Estudos-de-Python/Aulas/Aula46/'

if os.path.exists(caminho+nome):
    print('Arquivo existente')
else:
    f = open(caminho+nome,'x')
    f.close()
    print('Arquivo criado')

if os.path.exists(caminho+nome):
    os.remove(caminho+nome)
    print('Arquivo Removido')
else:
    print('Arquivo inexistente')