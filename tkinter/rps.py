from tkinter import *
from random import randint
def rps():
    num=randint(1,3)
    if num==1:
        return 'skare'
    elif num==2:
        return 'papir'
    else:
        return 'kamen'
    
def kamen():
    racOdg=rps()
    jaTxt.set('Odabrali ste kamen')
    if racOdg=='kamen':
        racTxt.set('Racunalo je odabralo kamen')
        rjTxt.set('Izjednaceno')
    elif racOdg=='papir':
        racTxt.set('Racunalo je odabralo papir')
        rjTxt.set('Izgubili ste')
    else:
        racTxt.set('Racunalo je odabralo skare')
        rjTxt.set('Pobjedili ste')

def papir():
    racOdg=rps()
    jaTxt.set('Odabrali ste papir')
    if racOdg=='kamen':
        racTxt.set('Racunalo je odabralo kamen')
        rjTxt.set('Pobjedili ste')
    elif racOdg=='papir':
        racTxt.set('Racunalo je odabralo papir')
        rjTxt.set('Izjednaceno')
    else:
        racTxt.set('Racunalo je odabralo skare')
        rjTxt.set('Izgubili ste')

def skare():
    racOdg=rps()
    jaTxt.set('Odabrali ste skare')
    if racOdg=='kamen':
        racTxt.set('Racunalo je odabralo kamen')
        rjTxt.set('Izgubili ste')
    elif racOdg=='papir':
        racTxt.set('Racunalo je odabralo papir')
        rjTxt.set('Pobjedili ste')
    else:
        racTxt.set('Racunalo je odabralo skare')
        rjTxt.set('Izjednaceno')


w=Tk()
w.geometry('280x400')
w.config(bg='#57c5b6')
p= Frame(w, relief= 'sunken', bg= "#159895")
p.pack(fill= BOTH, expand= True, padx= 10, pady=10)

naslov=Label(p,text='Kamen, Skare, Papir',font=('Arial',11,'bold'),bg='#159895',fg='white')
naslov.place(x=75,y=10)

kamen=Button(p,text='Kamen',width=10,command=kamen,bg='#002B5B',fg='white')
kamen.place(x=100,y=50)
skare=Button(p,text='Skare',width=10,command=skare,bg='#002B5B',fg='white')
skare.place(x=100,y=100)    	
papir=Button(p,text='Papir',width=10,command=papir,bg='#002B5B',fg='white')
papir.place(x=100,y=150)
jaTxt= StringVar()
racTxt=StringVar()
rjTxt=StringVar()

ja=Label(p,textvariable=jaTxt,width=25,bg='#1A5F7A',fg='white')
ja.place(x=50,y=200)
jaTxt.set('Vi')
rac=Label(p,textvariable=racTxt,width=25,bg='#1A5F7A',fg='white')
rac.place(x=50,y=250)
racTxt.set('Racunalo')
rj=Label(p,textvariable=rjTxt,width=25,bg='#1A5F7A',fg='white')
rj.place(x=50,y=300)
rjTxt.set('Rjesenje')
p.mainloop()

