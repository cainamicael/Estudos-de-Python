
from tkinter import *
from tkinter import messagebox

app = Tk()
app.title('CFB Cursos')
app.geometry('500x300')

def mostrarMsg():
    messagebox.showinfo(title='CFB Cursos', message='CFB Cursos, Curso de Python/Tkinter')

vnum_texto = StringVar()

fr_quadro1 = Frame(app, borderwidth=1, relief='solid')
"""
relief (flat, reised, sunken, solid)
"""
fr_quadro1.place(x=10, y=10, width=300, height=100)

Label(app, text='Tipo de cx(1, 2 ou 3').pack()
tb_num = Entry(app, textvariable= vnum_texto)
tb_num.pack()

btn_msg =Button(app, text='Mostrar Mensagem', command= lambda:mostrarMsg(vnum_texto.get(), vmsg))#Para chamar função com argumentos chama como lambda
btn_msg.pack()

app.mainloop()