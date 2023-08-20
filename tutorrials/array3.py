#Napišite program koji će omogućiti upisivanje niza 
#duljine n. Program treba ispisati
#članove niza koji su veći od sljedećeg clana niza.

n = int(input(""))
a = []

for i in range(0,n):
    a.append(int(input("")))

for i in range(0,n-1):
    if a[i] > a[i+1]:
        print(a[i])