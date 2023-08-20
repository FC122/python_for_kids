#Napišite program koji će omogućiti upisivanje 
#niza duljine n. Program treba ispisati
#članove niza s neprarnim indeksom.

n = int(input(""))
a = []

for i in range (0,n):
    a.append(int(input("")))

for i in range(0,n):
    if i%2 != 0:
        print(a[i])