# Turniej wiedzy
# Gra sprawdzająca wiedzę ogólną, odczytująca dane ze zwykłego pliku

import sys

def otworz_plik(nazwa_pliku, tryb):
    """Otwórz plik"""
    try:
        plik = open(nazwa_pliku, tryb)
    except IOError as e:
        print("Nie można otworzyć pliku", nazwa_pliku, "Program zostanie zakończony \n", e)
        input("Aby zakończyć program, naciśnij klawisz Enter")
        sys.exit()
    else:
        return plik


def nowa_linia(plik):
    """Zwróć kolejny wiersz pliku po sformatowaniu go"""
    linia = plik.readline()
    linia = linia.replace("/", "\n")
    return linia


def nowy_blok(plik):
    """Zwróć kolejny blok danych z pliku"""
    kategoria = nowa_linia(plik)

    pytanie = nowa_linia(plik)

    odpowiedzi = []
    for i in range(4):
        odpowiedzi.append(nowa_linia(plik))

    poprawna = nowa_linia(plik)
    if poprawna:
        poprawna = poprawna[0]

    wyjasnienie = nowa_linia(plik)

    return kategoria, pytanie, odpowiedzi, poprawna, wyjasnienie


def witaj(title):
    """Przywitaj gracza i pobierz jego nazwę"""
    print("\t\t Witaj w turnieju wiedzy!\n")
    print("\t\t", title, "\n")


def main():
    trivia_file = otworz_plik("kwiz.txt", "r")
    title = nowa_linia(trivia_file)
    witaj(title)
    score = 0
    # pobierz pierwszy blok
    kategoria, pytanie, odpowiedzi, poprawna, wyjasneinie = nowy_blok(trivia_file)
    while kategoria:
        # zadaj pytanie
        print(kategoria)
        print(pytanie)
        for i in range(4):
            print("\t", i+1, "-", odpowiedzi[i])
        # uzyskaj odpowiedz
        odpowiedz = input("Jaka jest Twoja odpowiedź?: ")
        # sprawdź odpowiedź
        if odpowiedz == poprawna:
            print("\nOdpowiedź prawidłowa!", end=" ")
            score +=1
        else:
            print("\nOdpowiedź niepoprawna.", end=" ")
        print(wyjasneinie)
        print("Wynik:", score,"\n\n")

        # pobierz kolejny blok
        kategoria, pytanie, odpowiedzi, poprawna, wyjasneinie = nowy_blok(trivia_file)

    trivia_file.close()
    print("To było ostatnie pytanie!")
    print("Twój końcowy wynik wynosi", score)


main()
input("\n\nAby zakończyć program, naciśnij klawisz Enter")
