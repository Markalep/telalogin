from cProfile import label
from calendar import c
from tkinter import * 


root = Tk()

root.title('Login')

largura = 400
altura = 300

largura_screen = root.winfo_screenwidth()
altura_screen = root.winfo_screenheight()

posx = largura_screen/2 - largura/2
posy = altura_screen/2 - altura/2
              #Substitui os parâmetros de dimensão da tela
root.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))
                                            #Sticky funciona com a rosa dos ventos W E N S
Label(root, text = 'Usuario: ').grid(row = 0, sticky=W)
Label(root, text = 'Senha: ').grid(row = 1, sticky=W)

textbox1 = Entry(root).grid(row = 0, column=1)
textbox2 = Entry(root).grid(row = 1, column=1)

cmd = Button(root, text= 'Login').grid(row= 2, column= 1, sticky=E)

root.mainloop()