from tkinter import *
from tkinter import messagebox

app = Tk()
app.title('CFB Cursos')
app.geometry('500x300')

def mostrarMsg(tipomsg, msg):
    if tipomsg == '1':
        messagebox.showinfo(title='CFB Cursos', message=msg)
    elif tipomsg == '2':
        messagebox.showwarning(title='CFB Cursos', message=msg)
    elif tipomsg == '3':
        messagebox.showerror(title='CFB Cursos', message=msg)

def resetarTB():
    res = messagebox.askyesno('Resetar','Confirma reset do TextBox?')
    """
    askyesno/askquestion - Sim ou Não (True of False)
    askokcancel - Ok e Cancelar " "
    askretrycancel - Repetir e Cancelar " "
    askyesnocancel - Sim, Não, Cancelar (True, False or None)
    """
    if res == True:
        tb_num.delete(0, END)
        tb_num.insert(0, '1')

vmsg = 'Curso de Python/Tkinter'
vnum_texto = StringVar()
vnum_texto.set('1')#Valor Padrão


Label(app, text='Tipo de cx(1, 2 ou 3').pack()
tb_num = Entry(app, textvariable= vnum_texto)
tb_num.pack()

btn_msg =Button(app, text='Mostrar Mensagem', command= lambda:mostrarMsg(vnum_texto.get(), vmsg))#Para chamar função com argumentos chama como lambda
btn_msg.pack()

btn_reset =Button(app, text='Reset', command=resetarTB)
btn_reset.pack()

app.mainloop()