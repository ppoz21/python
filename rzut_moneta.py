#Rzut monetą
#
#Program symuluje ilość orłów i reszek na 100 rzutów

import random

rzut = 1
orzel = 0
reszka = 0

while rzut <= 100:
    los = random.randint(1,2)
    if los == 1:
        orzel +=1
    elif los == 2:
        reszka +=1
    else:
        print("Błąd krytyczny programu!")
        break
    rzut +=1

print("Orzeł wypadł", orzel, "razy, natomiast reszka", reszka,"razy")

input("Aby zakończyć program niaciśnij Enter")