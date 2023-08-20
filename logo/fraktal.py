from turtle import*
def krivulja(a,n):
    if(n==0):
        fd(a)
    else:
        krivulja(a/3.0,n-1)
        lt(60)
        krivulja(a/3.0,n-1)
        rt(120)
        krivulja(a/3.0,n-1)
        lt (60)
        krivulja(a/3.0,n-1)
def koch(a,n):
    for i in range(3):
        krivulja(a,n)
        rt(120)

koch(100,3)
