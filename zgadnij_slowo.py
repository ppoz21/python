#zgadnij słowo
#komputer losuje słowo, następnie użytkownik 5 razy pyta, czy dana litera znajduje się w słowie
#potem musi zgadnąć

import random

SLOWA = ("kotek", "piesek", "fizyka", "antidotum")

slowo = random.choice(SLOWA)

zgadles = slowo

print("Wylosowane słowo ma", len(slowo), "liter.")

szanse = 0
while szanse < 5:
    x = input("Czy w słowie znajduje się litera: ")
    if x in slowo:
        print("tak")
    else:
        print("nie")
    szanse += 1

print("Twoje pytania zakończone. Czas zgadnąć słowo! Jeśli chcesz się wycować naciśnij Enter nie wpisując słowa")
zgaduje = input("Podaj słowo: ")
while zgaduje != zgadles and zgaduje !="":
    print("To nie to słowo")
    zgaduje = input("Podaj słowo: ")

if zgaduje == zgadles:
    print("Gratulacje! Udało ci się zgadnąć słowo!")

print("Dziękuję za grę!")

input("Aby zakończyć naciśnij Enter!")