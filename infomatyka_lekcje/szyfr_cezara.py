# Szyfr Cezara
# Przykład szyfru przestawnego

def szyfruj(string):
    """Szyfrowanie wiadomości"""
    slowo = listuj(string)
    zakodowana = []
    nowe = ''
    for litera in slowo:
        kod = ord(litera) + 3
        kod = chr(kod)
        zakodowana.append(kod)
    for litera in zakodowana:
        nowe = nowe + litera
    print(nowe)



def deszyfruj(string):
    """Deszyfrowanie wiadomości"""
    slowo = listuj(string)
    odkodowana = []
    nowe = ''
    for litera in slowo:
        kod = ord(litera) - 3
        kod = chr(kod)
        odkodowana.append(kod)
    for litera in odkodowana:
        nowe = nowe + litera
    print(nowe)


def listuj(string):
    """Zwracamy string w postaci listy znaków"""
    return list(string)


def main():
    print("""
    Witaj w programie kodującym i dekodującym Szyfr Cezara!
    
    Dostępne opcje:
    
    1 - Szyfrowanie
    
    2 - Deszyfrowanie
    
    3 - Koniec programu
    
    """)

    while(True):
        opcja = input("Twój wybór: ")
        if opcja == '1':
            slowo = input("Wprowadź tekst do zaszyfrowania: ")
            szyfruj(slowo)
        elif opcja == '2':
            slowo = input("Wprowadź tekst do odszyfrowania: ")
            deszyfruj(slowo)
        elif opcja == '3':
            print("Do zobaczenia!")
            break
        else:
            print("Błędna opcja!")


main()
input("Aby zakończyć naciśnij Enter")