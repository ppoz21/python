# Odwrócona notacja polska
# czyli zamiast 2+2 zapisujemy 2 2 + xDDDDD
# Wersja toporna dla Gabena

def odwrocona_notacja(x):
    wyr = list(x)
    i = len(wyr)
    j = 1
    wynik = int(wyr[0])
    liczba = 0
    while(j < i ):
        if(wyr[j] == " "):
            j += 1
            continue
        elif(wyr[j] == "+"):
            wynik = wynik + int(liczba)
        elif(wyr[j] == "-"):
            wynik = wynik - int(liczba)
        elif (wyr[j] == "*"):
            wynik = wynik * int(liczba)
        elif (wyr[j] == "/"):
            wynik = wynik / int(liczba)
        else:
            liczba = wyr[j]
        j += 1
    print("Wynik wyrażenia: ", wynik)


def main():
    wyrazenie = input("Wprowadź działanie w odwróconej notacji polskiej (liczby oddziel spacjami): ")
    odwrocona_notacja(wyrazenie)
    input("Aby zakończyć naciśnij Enter")

main()
