import re
texto = 'Curso de Python do CFB Cursos, canal do Youtube'
res = re.sub(',','.',texto)# quero substituir toda vírgula por ponto
print(res)