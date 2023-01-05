#findall - retorna uma lista de ocorrencias da palavra ou sílaba de uma string
import re #RegEx
texto = 'Curso de Python do CFB Cursos, canal do youtube'
pesq = input('Pesquisar: ')
res = re.findall(pesq, texto) # procura a sílaba 'so' em texto
print(res) # retorna ['so','so']
qtde = len(res)
print(f'Qtde: {qtde}')

