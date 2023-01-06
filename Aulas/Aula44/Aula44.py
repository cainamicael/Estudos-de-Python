nome = 'teste.txt'
f = open('C:/Users/cmcai/Documents/GitHub/Estudos de Python/Estudos-de-Python/Aulas/Aula44/'+nome, 'at') #(t é text, posso omitir)No segundo parâmetro posso passar:
"""
r - read (leitura)
a - append (anexar ao final)
w - write (escrita) - se não existir, ele cria e já abre para a escrita. Ele sobrescreve o que ja existia
x - create (criar)
t - text (texto) - já é o padrão
b - bynary (binário)
"""
txt = input('Digite um texto: ')
f.write(txt + '\n') # escrevendo dentro do arquivo
f.close()#Lembrar de fechar no final