# Variáveis globais
nu1=num2=res=0
canal = "CFB Cursos"

def cn():
    print(canal) #escopo global

cn()

def cs():
    curso = 'Python'
    print(curso)

cs()

#print(curso)#escopo local

def variavel():
    global vari
    vari = 1
    print(vari)

variavel()
print(vari)
