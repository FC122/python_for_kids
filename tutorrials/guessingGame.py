from tkinter import *
from random import randint

randomValue = randint(1,100)
def hotCold():
    value = int(u1.get())
    
    if(value>randomValue):
        jaTxt.set("Hot")

    if(value<randomValue):
        jaTxt.set("Cold")
        
    if(value==randomValue):
        jaTxt.set("You guessed it")



w=Tk()
w.geometry('280x300')
w.config(bg='#57c5b6')
p= Frame(w, relief= 'sunken', bg= "#159895")
p.pack(fill= BOTH, expand= True, padx= 10, pady=10)

naslov=Label(p,text='Guess the number',font=('Arial',11,'bold'),bg='#159895',fg='white')
naslov.place(x=75,y=10)

u1=Entry(p,width=10)
u1.place(x=100,y=100)
jaTxt= StringVar()
racTxt=StringVar()
rjTxt=StringVar()

guess=Button(p,text='Guess',width=10,command=hotCold,bg='#002B5B',fg='white')
guess.place(x=90,y=250)

ja=Label(p,textvariable=jaTxt,width=25,bg='#1A5F7A',fg='white')
ja.place(x=50,y=200)
jaTxt.set('Hot/Cold')

p.mainloop()

