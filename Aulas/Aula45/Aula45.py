import re
f = open('C:/Users/cmcai/Documents/GitHub/Estudos de Python/Estudos-de-Python/Aulas/Aula45/teste.txt', 'rt')

res = re.sub(' ','-', f.readline())

f.close()


print(res)