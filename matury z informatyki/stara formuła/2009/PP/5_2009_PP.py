# Liczby pierwsze
from math import *


def czy_pierwsza(liczba):
    liczbaINT = int(liczba)
    if liczba != liczbaINT:
        return False
    i = 2
    while i < sqrt(liczba):
        if liczba % i == 0:
            return False
        i += 1
    return True


plik = open('dane\liczby.txt', 'r')
wynik = open('wynik\zad_5.txt', 'w')
liczby = []
for slowo in plik:
    liczby.append(int(slowo))
plik.close()
for liczba in liczby:
    if czy_pierwsza(sqrt(liczba)):
        wynik.writelines(str(liczba)+'\n')
wynik.close()
