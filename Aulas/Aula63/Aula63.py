#Radio Button
from tkinter import *

def imprimirEsporte():
    ve = vesporte.get()
    if ve == 'f':
        print('Esporte Futebol')
    elif ve == 'v':
        print('Esporte Vôlei')
    elif ve == 'b':
        print('Esporte Basquete')
    else:
        print('Nenhum Esporte Selecionado!')

app = Tk()
app.title('CFB Cursos')
app.geometry('500x300')

vesporte = StringVar() #A variável que vai armazenar a opção que foi selecionada
vcor = StringVar()

#Esportes
lb_esportes = Label(app, text='Esportes')
lb_esportes.pack()

rb_futebol = Radiobutton(app, text='Futebol', value='f', variable=vesporte)#Não pode esquecer o value
rb_futebol.pack()

rb_volei = Radiobutton(app, text='Vôlei', value='v', variable=vesporte)#Não pode esquecer o value
rb_volei.pack()

rb_basquete = Radiobutton(app, text='Basquete', value='b', variable=vesporte)#Não pode esquecer o value
rb_basquete.pack()


rb_verde = Radiobutton(app, text='Verde', value='#0f0', variable=vcor)#Vai separar dos esportes
rb_verde.pack()

rb_vermelho = Radiobutton(app, text='Vermelho', value='#f00', variable=vcor)#Não pode esquecer o value
rb_vermelho.pack()

btn_esporte = Button(app, text='Esporte Selecionado', command=imprimirEsporte)
btn_esporte.pack()


app.mainloop()