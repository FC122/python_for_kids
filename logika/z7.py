broj = int(input("Unesite troznamenkasti broj: "))

znamenka1 = broj // 100  # Prva znamenka
znamenka2 = (broj // 10) % 10  # Druga znamenka
znamenka3 = broj % 10  # Treća znamenka

zbroj_znamenki = znamenka1 + znamenka2 + znamenka3

print("Zbroj znamenki:", zbroj_znamenki)
