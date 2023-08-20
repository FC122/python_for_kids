import getpass

# Prvi korisnik postavlja lozinku
password = getpass.getpass("Unesite lozinku: ")

# Drugi korisnik pogađa lozinku
guess = input("Pogodite lozinku: ")

# Provjera točnosti lozinke
while guess != password:
    print("Lozinka je pogrešna.")
    guess = input("Pokušajte ponovno: ")

print("Upisali ste točnu lozinku.")
