#entrada de texto
from tkinter import *

def semComando():
    print('')

def novoContato():
    exec(open('C:\\Users\\cmcai\\Documents\\GitHub\\Estudos de Python\\Estudos-de-Python\\Aulas\\Aula60\\Aula60.py').read(),{'x':10})
    #Quando clicar em Novo, vai abrir o formulario que está neste arquivo
    #Possoapassar parâmetros depois do read


app = Tk()

app.title('CFB Cursos')
app.geometry('500x300')
app.configure(background='#dde')

barraDeMenus = Menu(app)
menuContatos = Menu(barraDeMenus,tearoff=0) #pra tirar os ---------

#submenus

menuContatos.add_command(label='Novo',command=novoContato)
menuContatos.add_command(label='Pesquisar',command=semComando)
menuContatos.add_command(label='Deletar',command=semComando)
menuContatos.add_separator()#Barra separadora
menuContatos.add_command(label='Fechar',command=app.quit)
barraDeMenus.add_cascade(label='Contatos',menu=menuContatos)#menu é de onde vem os itens - Add cascade é menu cascata

menuManutencao = Menu(barraDeMenus, tearoff=0)
menuManutencao.add_command(label='Banco de Dados',command=semComando)
barraDeMenus.add_cascade(label='Manutenção',menu=menuManutencao)#menu é de onde vem os itens - Add cascade é menu cascata

menuSobre = Menu(barraDeMenus, tearoff=0)
menuSobre.add_command(label='CFB Cursos',command=semComando)
barraDeMenus.add_cascade(label='Sobre',menu=menuSobre)#menu é de onde vem os itens - Add cascade é menu cascata


app.config(menu=barraDeMenus) #Para o menu aparecer na janela
app.mainloop()