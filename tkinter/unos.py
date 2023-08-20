from tkinter import * 
from turtle import *
def kvadrat():
    for i in range(4):
        fd(int(unos.get()))
        lt(90) 

prozor = Tk()  
prozor.title('Python')
prozor.geometry('230x150')
prozor.config(bg='gold')


gumb = Button(prozor,text='Kvadrat',bg='cyan',command=kvadrat)
gumb.place(x=75,y=50,width=60,height=30)

tk1=Label(prozor,text='CRTANJE KVADRATA',bg='yellow',fg='red',font=('Arial',11,'italic'))
tk1.place(x=50,y=10)

tk2=Label(prozor,text='Unesite duljinu stranice:',bg='yellow',fg='red',font=('Arial',11,'italic'))
tk2.place(x=5,y=100)

unos=Entry(prozor,width=8)
unos.place(x=170,y=100)

prozor.mainloop()