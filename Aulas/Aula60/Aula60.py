#entrada de texto
from tkinter import *
import os
import banco

print(x)
def gravarDados():
    if tb_nome.get() != '':
        vnome = tb_nome.get()
        vfone = tb_fone.get()
        vemail = tb_email.get()
        vobs = tb_obs.get('1.0', END)
        query = f"INSERT INTO tb_contatos (t_nomecontato, t_telefonecontato, t_emailcontato, t_obs) VALUES ('{vnome}', '{vfone}', '{vemail}', '{vobs}')"
        banco.dml(query)

        #Limpando os campos do formulário

        tb_nome.delete(0, END)
        tb_fone.delete(0, END)
        tb_email.delete(0, END)
        tb_obs.delete('1.0', END)

        print('Dados Gravados')
    else:
        print('Erro')
 
app = Tk()

app.title('CFB Cursos')
app.geometry('500x300')
app.configure(background='#dde')

#Anchor => N-Norte, S-SUl, E-Leste, W-Oeste, NE-Nordeste, SE-Sudeste, SO-Sudoeste, NO-Noroeste 
Label(app, text='Nome', bg='#dde', fg='#009', anchor=W).place(x=10, y=10, width=100, height=20)
tb_nome = Entry(app)#É usado para entrada de dados
tb_nome.place(x=10, y=30, width=200, height=20)

Label(app, text='Telefone', bg='#dde', fg='#009', anchor=W).place(x=10, y=60, width=100, height=20)
tb_fone = Entry(app)#É usado para entrada de dados
tb_fone.place(x=10, y=80, width=200, height=20)

Label(app, text='Email', bg='#dde', fg='#009', anchor=W).place(x=10, y=110, width=100, height=20)
tb_email = Entry(app)#É usado para entrada de dadosha
tb_email.place(x=10, y=130, width=300, height=20)

Label(app, text='Obs', bg='#dde', fg='#009', anchor=W).place(x=10, y=160, width=100, height=20)
tb_obs = Text(app)#É usado para entrada de dados - Componente de texto multi-linha
tb_obs.place(x=10, y=180, width=300, height=80)

btn = Button(app, text='Gravar', command=gravarDados)#Command chama a Função
btn.place(x=10, y=270, width=100, height=20)

app.mainloop()