curso = ' Curso de Python '

print(curso.strip())

print(curso[0:4])
print(curso.lower().strip())
print(curso.upper())
print('Tamanho' , len(curso))
print(curso.replace('Python', 'Java'))
a = curso.split(' ')
print(type(a))

res = 'Python' not in curso
print(res)

canal = 'CFB Cursos'
res = curso + " do canal " + canal
print(res)

cidade = 'Recife'
dia = 16
mes = 'Novembro'
ano = 2022
data = '{}, {} de {} de \n{}'
print(data.format(cidade, dia, mes, ano))