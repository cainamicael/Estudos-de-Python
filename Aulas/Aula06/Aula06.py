curso = ' Curso de Python '

print(curso.strip())

print(curso[0:4])
print(curso.lower().strip())
print(curso.upper())
print('Tamanho' , len(curso))
print(curso.replace('Python', 'Java'))
a = curso.split(' ')
print(type(a))