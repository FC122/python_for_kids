from tkinter import * 
from turtle import *
def kvadrat():
    for i in range(4):
        fd(100)
        lt(90) 
def trokut():
    for i in range(3):
        fd(100)
        lt(120)

prozor = Tk()  
prozor.title('Python')
prozor.geometry('220x150')
prozor.config(bg='gold')

gumb = Button(prozor,text='Kvadrat',bg='cyan',command=kvadrat)
gumb.place(x=75,y=50,width=60,height=30)

gumb1 = Button(prozor,text='Trokut',command=trokut) 
gumb1.place(x=75,y=100,width=60,height=30)

prozor.mainloop()