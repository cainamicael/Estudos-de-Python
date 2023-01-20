#Radio Button
from tkinter import *

def imprimirEsporte():
    ve = vesporte.get()
    if ve == 'Futebol':
        print('Esporte Futebol')
    elif ve == 'Vôlei':
        print('Esporte Vôlei')
    elif ve == 'Basquete':
        print('Esporte Basquete')
    else:
        print('Nenhum Esporte Selecionado!')

app = Tk()
app.title('CFB Cursos')
app.geometry('500x300')

listaEsportes = ['Futebol', 'Vôlei', 'Basquete']

vesporte = StringVar() #A variável que vai armazenar a opção que foi selecionada
vesporte.set(listaEsportes[0]) #Deixando o futebol como o padrão (default)

#Esportes
lb_esportes = Label(app, text='Esportes')
lb_esportes.pack()

op_esportes = OptionMenu(app, vesporte, *listaEsportes)#Forma mais fácil, cria cada opção com cada valor da lista
op_esportes.pack()

btn_esporte = Button(app, text='Esporte Selecionado', command=imprimirEsporte)
btn_esporte.pack()

app.mainloop()