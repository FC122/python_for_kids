from turtle import *
from random import randint
boja = ['red','green','blue']
def zvijezda():
    ind=randint(0,2)
    color(boja[ind], boja[ind])
    begin_fill()
    for i in range(5):
        fd(30)
        rt(2*360/5)
    end_fill()
def spirala(a,k):
    zvijezda()
    fd(a)
    rt(70)
    if a<10:
        return
    else:
        spirala(a-k,k)

spirala(200,5)