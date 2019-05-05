# szyfrowanie według słowa kluczowego
import string


def stworz_alfabet(klucz, alfabet):
    alf = []
    for litera in klucz:
        if litera in alf:
            continue
        else:
            alf.append(litera)
    for litera in alfabet:
        if litera in alf:
            continue
        else:
            alf.append(litera)
    return alf


def koduj(slowo, alfabet, kod):
    zakodowana = ''
    spacja = ' '
    for litera in slowo:
        if litera == spacja:
            zakodowana += spacja
        else:
            index = alfabet.index(litera)
            zakodowana += kod[index]
    return zakodowana


def dekoduj(slowo, alfabet, kod):
    dekodowana = ''
    spacja = ' '
    for litera in slowo:
        if litera == spacja:
            dekodowana += spacja
        else:
            index = kod.index(litera)
            dekodowana += alfabet[index]
    return dekodowana


print(
"""
Witaj w programie do kodów przestawnych.
Wybierz jedną z opcji:
1 - kodowanie
2 - dekodowanie
3 - zakończ program
"""
)
opcja = None
while opcja != 3:
    opcja = int(input("Wybrana opcja: "))
    if opcja == 1:
        klucz = input("Wprowadź słowo kluczowe: ").upper()
        alfabet = list(string.ascii_uppercase)
        alfabet2 = stworz_alfabet(klucz, alfabet)
        slowo = input("Wprowadź słowo do zakodowania: ").upper()
        zakodowane = koduj(slowo, alfabet, alfabet2)
        print(zakodowane)
    elif opcja == 2:
        klucz = input("Wprowadź słowo kluczowe: ").upper()
        alfabet = list(string.ascii_uppercase)
        alfabet2 = stworz_alfabet(klucz, alfabet)
        slowo = input("Wprowadź słowo do zdekodowania: ").upper()
        dekodowane = dekoduj(slowo, alfabet, alfabet2)
        print(dekodowane)
    elif opcja == 3:
        print("Do zobaczenia następnym razem!")
    else:
        print("Nietety, nie ma takiej mozliwości")

input("Aby zakończyć program naciśnij Enter")
#print(alfabet)
#print(alfabet2)


