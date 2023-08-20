from turtle import *
def kvadrat(a):
    for i in range(4):
        fd(a)
        lt(90)
def niz(a,k):
    while a>=10:
        kvadrat(a)
        a=a-k


niz(100,10)
