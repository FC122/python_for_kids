from tkinter import *

def pov():
    povrsina=int(u1.get())+int(u2.get())
    rez1=Label(p,text='Površina je '+str(povrsina))
    rez1.place(x=140,y=120)
def ops():
    opseg=2*(int(u1.get())+int(u2.get()))
    rez1=Label(p,text='Opseg je '+str(opseg))
    rez1.place(x=140,y=160)
p=Tk()
p.geometry('300x200')

t=Label(p,text='OPSEG I POVRŠINA PRAVOKUTNIKA')
t.place(x=50, y=20)

t1=Label(p,text='Upiši duljinu prve stranice:')
t1.place(x=30,y=50)
t2=Label(p,text='Upiši duljinu druge stranice:')
t2.place(x=20,y=80)

u1=Entry(p,width=10)
u1.place(x=180,y=50)
u2=Entry(p,width=10)
u2.place(x=180,y=80)

g1=Button(p,text='Površina', width=10,command=pov)
g1.place(x=40,y=120)
g2=Button(p,text='Opseg',width=10,command=ops)
g2.place(x=40,y=160)

p.mainloop()