# Python Salabahter

# Varijable i tipovi podataka
moja_varijabla = 10
moj_string = "Hello, World!"
moja_lista = [1, 2, 3, 4, 5]
moj_tjedan = ("ponedjeljak", "utorak", "srijeda", "četvrtak", "petak")
moj_rjecnik = {"ime": "Ana", "dob": 25}

# Osnovne operacije
rezultat = 2 + 3  # Zbrajanje
rezultat = 5 - 2  # Oduzimanje
rezultat = 4 * 2  # Množenje
rezultat = 10 / 3  # Dijeljenje (rezultat je decimalni broj)
rezultat = 10 // 3  # Dijeljenje s ostatkom (rezultat je cijeli broj)
rezultat = 2 ** 3  # Potenciranje
rezultat = 10 % 3  # Modulo (ostatak pri dijeljenju)

# Uvjetne naredbe
if uvjet:
    # Izvršava se ako je uvjet istinit
elif drugi_uvjet:
    # Izvršava se ako je drugi_uvjet istinit
else:
    # Izvršava se ako nijedan uvjet nije istinit

# Petlje
for element in iterable:
    # Izvršava se za svaki element u iterable

while uvjet:
    # Izvršava se sve dok je uvjet istinit

# Funkcije
def moja_funkcija(argument1, argument2):
    # Kod koji se izvršava
    return rezultat

# String operacije
moj_string = "Hello, World!"

duljina = len(moj_string)  # Duljina stringa
podstring = moj_string[7:12]  # Izdvajanje podstringa

velika_slova = moj_string.upper()  # Pretvaranje u velika slova
mala_slova = moj_string.lower()  # Pretvaranje u mala slova

spojeni_stringovi = moj_string + " It's a beautiful day!"  # Spajanje stringova

# Lista operacije
moja_lista = [1, 2, 3, 4, 5]

duljina = len(moja_lista)  # Duljina liste
element = moja_lista[2]  # Pristup elementu

moja_lista.append(6)  # Dodavanje elementa na kraj liste
moja_<lista.insert(0, 0)  # Dodavanje elementa na određeni indeks

moja_lista.remove(3)  # Uklanjanje elementa po vrijednosti
element = moja_lista.pop(2)  # Uklanjanje elementa po indeksu i vraćanje vrijednosti

# Operacije sa rječnikom
moj_rjecnik = {"ime": "Ana", "dob": 25}

vrijednost = moj_rjecnik["ime"]  # Pristup vrijednosti po ključu

moj_rjecnik["grad"] = "Zagreb"  # Dodavanje novog ključa-vrijednosti
del moj_rjecnik["dob"]  # Uklanjanje ključa-vrijednosti

kljucevi = moj_rjecnik.keys()  # Dohvaćanje liste ključeva
vrijednosti = moj_rjecnik.values()  # Dohvaćanje liste vrijednosti

# Rad s datotekama
datoteka = open("moja_datoteka.txt", "r")  # Otvori datoteku za čitanje
sadrzaj = datoteka.read()  # Čitanje cijelog sadržaja datoteke
datoteka.close()  # Zatvori datoteku

datoteka = open("moja_datoteka.txt", "w")  # Otvori datoteku za pisanje
datoteka.write("Hello, World!")  # Upisivanje sadržaja u datoteku
datoteka.close()  # Zatvori datoteku

# Obrada iznimki
try:
    # Kod koji može izazvati iznimku
except TipIznimke:
    # Kod za rukovanje iznimkom

# Uvoz modula
import modul  # Uvoz cijelog modula
from modul import funkcija  # Uvoz određene funkcije iz modula
from modul import *  # Uvoz svih funkcija iz modula

# Komentari
# Ovo je jednolinijski komentar

"""
Ovo je
višelinijski
komentar
"""

# Ispis na ekran
print("Hello, World!")  # Ispisivanje stringa
print(f"Vrijednost je: {vrijednost}")  # Ispis formatiranih stringova


# Reading input from the keyboard
name = input("Enter your name: ")
age = input("Enter your age: ")

