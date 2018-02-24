from tkinter import *
from datetime import datetime

root = Tk()
root['bg'] = "black"
root.title('NERD_SCRIPT *** Projeto ARC')

open("menu.txt","a")

def salve():
    file = open("menu.txt","a")
    x = str(nota.get())
    file.write("\n" + x)
    y = texto.get(1.0, END)
    open(x,'w')
    ark = open(x,'w')
    ark.write(y)
    ark.close()
    file.close()

def ler():
    x = str(nota.get())
    open(x,'r')
    ark = open(x,'r')
    y = ark.read()
    texto.delete(1.0,END)
    texto.insert(INSERT,y)
    ark.close()

def limp():
    texto.delete(1.0,END)

def data():
    hj = datetime.now()
    x = ("*", hj.day, hj.month, hj.year,"as", hj.hour,":",hj.minute,"*")
    texto.insert(INSERT,x)
    
def menu():
    texto.delete(1.0,END)
    open("menu.txt","r")
    x = open("menu.txt","r")
    y = x.read()
    texto.insert(INSERT,y)
    x.close()
    
    
texto = Text(root, height = 30, width = 40,font=("Helvetica",11), bg = "#E0FFFF", fg = "black")
texto.insert(INSERT,">>>")
texto.place(x = 10, y = 38)

nota = Entry(root, width = 53, bg = "#E0FFFF", fg = "black")
nota.place(x = 10, y = 10)



but = Button(root, text = "SALVAR", bg = "black", fg = "cyan", command = salve)
but.place(x = 10, y = 553)

but1 = Button(root, text = "Ler", bg = "black", fg = "cyan", command = ler)
but1.place(x = 70, y = 553)

but2 = Button(root, text = "Limpar", bg = "black", fg = "cyan", command = limp)
but2.place(x = 100, y = 553)

but3 = Button(root, text = "Data", bg = "black", fg = "cyan", command = data)
but3.place(x = 150, y = 553)

but4 = Button(root, text = "Menu", bg = "black", fg = "cyan", command = menu)
but4.place(x = 200, y = 553)

root.geometry("350x600")
root.mainloop()
