from tkinter import*
from turtle import*

def zbroj():
    a= int(unos.get())
    b= int(unos1.get())

    polje2=Label(prozor,bg="white",text= str(a+b))
    polje2.place(x= 150,y=200, width=60, height=20)
    
def razlika():
    a= int(unos.get())
    b= int(unos1.get())
    polje3=Label(prozor,bg="white",text=str(a-b))
    polje3.place(x= 150,y=250, width=60, height=20)
    
def umnozak():
    a= int(unos.get())
    b= int(unos1.get())
    polje4=Label(prozor,bg="white",text=str(a*b))
    polje4.place(x= 150,y=300, width=60, height=20)

def kolicnik():
    a=int(unos.get())
    b=int(unos1.get())
    polje5=Label(prozor,bg="white",text=str(a/b))
    polje5.place(x= 150,y=350, width=60, height=20)


def izracunaj():
    umnozak()
    zbroj()
    razlika()
    kolicnik()


prozor=Tk()
prozor.title('Python')
prozor.geometry('500x500')
prozor.config(bg='gold')

polje1=Label(prozor, text="Prvi broj",bg="cyan")
polje1.place(x= 50,y=100, width=60, height=20)

polje1=Label(prozor, text="Drugi broj",bg="cyan")
polje1.place(x= 50,y=150, width=60, height=20)

polje1=Label(prozor, text="Zbroj",bg="white")
polje1.place(x= 50,y=200, width=60, height=20)

polje1=Label(prozor, text="Razlika",bg="white")
polje1.place(x= 50,y=250, width=60, height=20)

polje1=Label(prozor, text="Umnozak",bg="white")
polje1.place(x= 50,y=300, width=60, height=20)

polje1=Label(prozor, text="Kolicnik",bg="white")
polje1.place(x= 50,y=350, width=60, height=20)


unos=Entry(prozor, bg="yellow")
unos.place(x=150,y=100,width=60,height=20)

unos1=Entry(prozor, bg="yellow")
unos1.place(x=150,y=150,width=60,height=20)


polje2=Label(prozor,bg="white")
polje2.place(x= 150,y=200, width=60, height=20)

polje3=Label(prozor,bg="white")
polje3.place(x= 150,y=250, width=60, height=20)

polje4=Label(prozor,bg="white")
polje4.place(x= 150,y=300, width=60, height=20)

polje5=Label(prozor,bg="white")
polje5.place(x= 150,y=350, width=60, height=20)

tipka=Button(prozor,bg="cyan",text="racunaj", command=izracunaj)#lambda:[zbroj(),razlika(),umnozak()])
tipka.place(x=300,y=350,width=90,height=70)


prozor.mainloop()
