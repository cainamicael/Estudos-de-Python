#entrada de texto
from tkinter import *
import os 

#Salvando respostas em um arquivo
c = os.path.dirname(__file__)#Obter o diretório da aplicação
nomeArquivo = c+'\\nomes.txt'


def gravarDados():
    arquivo = open(nomeArquivo, 'at')
    arquivo.write('\nNome: %s' %vnome.get())
    arquivo.write('\nTelefone: %s' %vfone.get())
    arquivo.write('\nEmail: %s' %vemail.get())
    arquivo.write('\nObs: %s' %vobs.get('1.0', END))
    arquivo.write('\n\n')
    arquivo.close()
 
app = Tk()

app.title('CFB Cursos')
app.geometry('500x300')
app.configure(background='#dde')

#Anchor => N-Norte, S-SUl, E-Leste, W-Oeste, NE-Nordeste, SE-Sudeste, SO-Sudoeste, NO-Noroeste 
Label(app, text='Nome', bg='#dde', fg='#009', anchor=W).place(x=10, y=10, width=100, height=20)
vnome = Entry(app)#É usado para entrada de dados
vnome.place(x=10, y=30, width=200, height=20)

Label(app, text='Telefone', bg='#dde', fg='#009', anchor=W).place(x=10, y=60, width=100, height=20)
vfone = Entry(app)#É usado para entrada de dados
vfone.place(x=10, y=80, width=200, height=20)

Label(app, text='Email', bg='#dde', fg='#009', anchor=W).place(x=10, y=110, width=100, height=20)
vemail = Entry(app)#É usado para entrada de dadosha
vemail.place(x=10, y=130, width=300, height=20)

Label(app, text='Obs', bg='#dde', fg='#009', anchor=W).place(x=10, y=160, width=100, height=20)
vobs = Text(app)#É usado para entrada de dados - Componente de texto multi-linha
vobs.place(x=10, y=180, width=300, height=80)

btn = Button(app, text='Gravar', command=gravarDados)#Command chama a Função
btn.place(x=10, y=270, width=100, height=20)

app.mainloop()