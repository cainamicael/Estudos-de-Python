from tkinter import *

app = Tk()

#Configurações da janela
app.title('CFB Cursos')#Título
app.geometry('500x300')#Tamanho
app.configure(background='#008')#COr de fundo padrão RGB

#Inserindo elementos na janela - Widgets
txt1 = Label(app, text='Curso de Python', background='#008', foreground='#fff')#app é o elemento pai - Criando em sí
txt1.place(x=10, y=10, width=100, height=20)#Tem que ter o place para aparecer na tela

#Atribuindo parâmetros com variáveis
vtxt = 'Modulo Tkinter'
vbg = '#ff0'
vfg = '#000'
txt2 = Label(app, text = vtxt, bg = vbg, fg = vfg)
txt2.pack(ipadx = 20, ipady = 20, padx = 5, pady = 5, side = 'top', fill = X, expand = True) #Ipad é o espaçamento interno e pad é o espaçamento externo
#Pack é adequado para usar com container


app.mainloop()#Para executar o programa