# Losowanie prezentów
# Odczyt z listy uczniów i przydzielenie każdemu z nich osoby do prezentu

import random

def odczytaj():
    lista = list(open("lista_uczniow.txt", "r"))
    return lista


def main():
    losujący = odczytaj()
    losowani = odczytaj()

    for osoba in losujący:
        kto = osoba.strip()
        wylosowany = random.choice(losowani)
        while(wylosowany == osoba):
            wylosowany = random.choice(losowani)
        losowani.remove(wylosowany)
        wylosowane = open("wylosowani.txt", "a")
        wylosowani = kto+" -> "+wylosowany.strip()+"\n\n"
        wylosowane.write(wylosowani)

        wylosowane.close()


main()