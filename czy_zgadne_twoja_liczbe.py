#Komputer "zgaduje liczbe wymyslona przez uzytkownika"

import random

print("Witaj, spróbuję zgadnąć liczbę wymyśloną przez ciebie. Musi ona mieścić się w przedziale od 1 do 100. \nZaczynajmy")

input("Jeśli już wymyśliłeś swoją liczbę naciśnij Enter")
tury = 1
poczatek = 0
koniec = 100
liczba = 0

while liczba == 0:
    wymyslona = random.randint(poczatek,koniec)
    print("Myślisz o", wymyslona, "?")
    x = input("Jeżeli zgadłem wpisz tak, w przeciwnum wypadku wpisz większa lub mniejsza: \n")
    if x == "tak":
        break
    elif x == "większa":
        poczatek = wymyslona + 1
    elif x == "mniejsza":
        koniec = wymyslona - 1
    else:
        print("Wpisałeś błędne dane")
        continue
    tury += 1

print("Udało mi się zgadnąć twoją liczbę w", tury, "turach. Brawo ja!")
input("Aby zakończyć grę naciśnij przycisk Enter")

