import re
texto = 'Curso de Python do CFB Cursos, canal do Youtube'
res = re.search('Carro',texto)#Retorna a posição da primeira ocorrencia que a gente encontrar. Podemos dizer se queremos inicial ou final
if (res != None):
    pi = res.start()
    pf = res.end()
    tam = pf-pi
    print(res.start())#método para a posição inicial
    print(res.end())#método para a posição final
    print(tam)
else:
    print('Não encontrado')