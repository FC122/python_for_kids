# Python tutorials
Content made while teaching python to kids along various workshops

# Tasks
Guessing Game: Create a program that generates a random number between 1 and 100 and asks the user to guess the number. The program should provide feedback to the user if their guess is too high or too low until they guess the correct number.

Korak 1: Uvezi potrebne module. Koristimo tkinter za izradu grafičkog korisničkog sučelja i randint iz modula random za generiranje nasumičnog broja.

Korak 2: Generiraj nasumični broj između 1 i 100. Ovaj broj će biti onaj koji korisnik treba pogoditi.

Korak 3: Definiraj funkciju hotCold(). Ova funkcija provjerava je li broj koji je korisnik unio veći, manji ili jednak nasumičnom broju. Ako je uneseni broj veći, postavlja tekst "Hot". Ako je uneseni broj manji, postavlja tekst "Cold". Ako je uneseni broj jednak nasumičnom broju, postavlja tekst "You guessed it".

Korak 4: Stvori glavni prozor aplikacije i konfiguriraj ga. Postavljamo veličinu na 280x300 piksela i boju pozadine na #57c5b6.

Korak 5: Stvori okvir u glavnom prozoru. Okvir je postavljen na "sunken" (utisnut), boja pozadine je postavljena na #159895, i ispunjava cijeli prozor.

Korak 6: Dodaj naslov, unosni okvir, gumb za pogađanje i oznaku za rezultat. Naslov je postavljen na "Guess the number". Unosni okvir se koristi za unos broja. Gumb za pogađanje poziva funkciju hotCold() kada se klikne. Oznaka za rezultat prikazuje je li uneseni broj "Hot", "Cold" ili "You guessed it".

Korak 7: Pokreni glavnu petlju. Ovo pokreće događajnu petlju tkintera. Aplikacija će ostati otvorena dok je korisnik ne zatvori.

Kod se može pokrenuti spremanjem kao .py datoteku i pokretanjem pomoću Python interpretera.




To-Do List: Create a program that allows the user to add tasks to a to-do list, mark tasks as completed, and remove tasks from the list.


**Korak 1:** Uvezi potrebne module. Trebat će nam `tkinter` biblioteka za izradu grafičkog korisničkog sučelja, te `messagebox` biblioteka za prikaz upozorenja kada je to potrebno.

**Korak 2:** Definiraj funkcije za gumbe. `add_task()` dodaje novi zadatak na popis, `delete_task()` briše odabrani zadatak, a `complete_task()` označava odabrani zadatak kao dovršen.

**Korak 3:** Stvori glavni prozor aplikacije. Ovo će stvoriti novi tkinter prozor koji će nam poslužiti kao glavni prozor aplikacije.

**Korak 4:** Konfiguriraj glavni prozor aplikacije. Ovo će postaviti veličinu prozora na 300x400 piksela i postaviti naslov prozora na "Popis zadataka".

**Korak 5:** Stvori okvir za listbox. Ovo će stvoriti novi widget okvira, koji je kontejnerski widget koji se koristi za organiziranje drugih widgeta.

**Korak 6:** Stvori listbox. Ovo će stvoriti novi listbox widget u okviru, postaviti njegovu veličinu, boje i druge atribute, a zatim ga pakirati u okvir.

**Korak 7:** Stvori unosni okvir. Ovdje će korisnik moći unijeti nove zadatke, te ga pakirati u glavni prozor.

**Korak 8:** Stvori gumbe. Ovo će stvoriti tri nova gumba i pakirati ih u glavni prozor. Parametar `command` se koristi za određivanje funkcije koja će se pozvati kada se klikne na gumb.

**Korak 9:** Pokreni glavnu petlju. Ovo će pokrenuti tkinter događajnu petlju. Aplikacija će ostati otvorena dok je korisnik ne zatvori.

Dice Roller: Create a program that simulates rolling a pair of dice. The program should allow the user to specify how many times they want to roll the dice and should display the results of each roll.

Korak 1: Uvezi potrebne module. Koristimo tkinter za izradu grafičkog korisničkog sučelja i randint iz modula random za generiranje nasumičnih brojeva.

Korak 2: Definiraj funkciju roll_dice(). Ova funkcija baca dvije kockice onoliko puta koliko je korisnik naveo. Rezultati se unose u widget results.

Korak 3: Stvori glavni prozor aplikacije i konfiguriraj ga. Postavljamo veličinu na 300x400 piksela i naslov na "Dice Roller".

Korak 4: Stvori okvir unutar glavnog prozora. Ovaj okvir će sadržavati unosni okvir i gumb.

Korak 5: Dodaj unosni okvir unutar okvira. Korisnik će ovdje unijeti broj bacanja kockica.

Korak 6: Dodaj gumb unutar okvira. Kada se klikne na gumb, poziva se funkcija roll_dice().

Korak 7: Dodaj tekstualni widget koji će prikazivati rezultate bacanja. Ovaj widget se dodaje direktno u glavni prozor.

Korak 8: Pokreni glavnu petlju. Ovo pokreće događajnu petlju tkintera. Aplikacija će ostati otvorena dok je korisnik ne zatvori.


Napravite program koji sadrži 100 unaprijed definiranih riječi. Na početku igre, program bi trebao zatražiti koliko riječi želite pogađati. Nakon što ste odredili broj riječi, program vam nasumično daje jednu po jednu izmiješanu riječ koju trebate pogoditi. Kada pogodite jednu riječ, dobivate sljedeću i tako nastavljate dok ne pogodite broj riječi koji ste prethodno odabrali. Također biste trebali imati mogućnost preskakanja riječi koje ne možete pogoditi. Za izradu korisničkog sučelja, igra bi trebala koristiti tkinter.

Napravite program koji sadrži 100 unaprijed definiranih riječi. Na početku igre, program bi trebao zatražiti koliko riječi želite pogađati. Nakon što ste odredili broj riječi, program vam nasumično daje jednu po jednu izmiješanu riječ koju trebate pogoditi. Kada pogodite jednu riječ, dobivate sljedeću i tako nastavljate dok ne pogodite broj riječi koji ste prethodno odabrali. Također biste trebali imati mogućnost preskakanja riječi koje ne možete pogoditi. Za izradu korisničkog sučelja, igra bi trebala koristiti tkinter.
Uvezi potrebne module:
Koristimo tkinter za korisničko sučelje i modul random za nasumično miješanje popisa riječi i za odabir slučajne riječi s popisa.

Definiraj popis riječi:
Imamo popis od 10 riječi koje se ponavljaju 10 puta kako bismo dobili 100 riječi. Zatim koristimo funkciju shuffle() iz modula random da bi smo nasumično izmiješali ovaj popis.

Definiraj pomoćne funkcije:

scramble(word): Ova funkcija prima riječ kao ulaz, pretvara je u popis znakova, miješa popis, a zatim spaja znakove natrag u niz koji se vraća.

start_game(): Ova funkcija pokreće igru. Postavlja words_to_guess na korisnikov unos i correct_guesses na 0. Zatim poziva funkciju next_word() da prikaže prvu izmiješanu riječ.

next_word(): Ova funkcija se poziva za prikaz nove izmiješane riječi. Ako još uvijek ima riječi za pogađanje, bira slučajnu riječ s popisa, uklanja je s popisa, miješa je i prikazuje. Također smanjuje words_to_guess za 1. Ako više nema riječi za pogađanje, prikazuje "Kraj igre!" i broj točnih pogađanja.

check_guess(): Ova funkcija se poziva kada korisnik klikne na gumb "Pogodi". Ako je korisnikov odgovor točan, povećava correct_guesses za 1, briše unos i prikazuje sljedeću izmiješanu riječ. Ako odgovor nije točan, prikazuje poruku da pokuša ponovno.

skip(): Ova funkcija se poziva kada korisnik klikne na gumb "Preskoči". Briše unos i prikazuje sljedeću izmiješanu riječ.

Napravi korisničko sučelje:
Koristimo tkinter za izradu korisničkog sučelja. Imamo polje za unos broja riječi koje treba pogoditi, gumb za pokretanje igre, oznaku za prikaz izmiješane riječi, polje za unos korisnikovog odgovora, gumb za pogađanje, gumb za preskakanje i oznaku za prikaz poruka.

Pokreni igru:
Na kraju, pozivamo root.mainloop() da pokrenemo igru. Tkinter će pokrenuti svoju glavnu petlju i prikazati korisničko suč


