import re
texto = 'Curso de Python do CFB Cursos, canal do Youtube'
res = re.split(' ',texto) #no lugar do espaço pode ser \s
print(res)
print(f'O texto tem {len(res)} palavras')