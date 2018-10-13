#translator slangu komputerowego
#demonstruje używanie słowników

geek = {"404": "ignorant; od używanego w sieci WWW komunikatu o błędzie 404\n - nieznaleziono strony.",
        "Googling": "googlowanie; wyszukiwanie w internecie informacji dotyczącychjakiejś osoby.",
        "Keyboard Plaque" : "(skojarzone z kamieniem nazębnym)zanieczyszczenianagromadzone w klawiaturze komputera.",
        "Link Rot" : "(obumieranie linków) proces, w wyniku którego linki do stron WWWstają się nieaktualne.",
        "Percussive Maintenance" : "(konserwacja perkusyjna)naprawa urządzeniaelektronicznego przez stuknięcie.",
        "Uninstalled" : "(odinstalowany) zwolniony z pracy; termin szczególnie popularnyw okresie bańki internetowej.",
        "Komputer" : "Maszyna służąca do dokonywania obliczeń (lub grania w gierki)"
        }

choice = None

while choice != "0":

        print(
        """
        Translator slangu komputerowego
        0 - zakończ
        1 - znajdź termin
        2 - dodaj nowy termin
        3 - zmień definicję terminu
        4 - usuń termin
        5 - wyświetl dostępne terminy
        """
        )

        choice = input('Wybierasz: ')
        print()

        #wyjdź
        if choice == '0':
                print("Żegnaj")

        #pobierz definicje
        elif choice == '1':
                term = input("Jaki termin chcesz przetłumaczyć?: ")
                if term in geek:
                        definition = geek[term]
                        print('\n', term, 'oznacza', definition)
                else:
                        print("\nNiestety, nie znam terminu", term)

        #dodaj parę termin-definicja
        elif choice == '2':
                term = input('Jaki termin mam dodać?: ')
                if term not in geek:
                        definition = input("\nPodaj definicję tego terminu: ")
                        geek[term] = definition
                        print("\nTermin", term, 'został dodany')
                else:
                        print('\nTen termin już istnieje! Spróbuj zmienić jego definicję.')

        #zmiana definicji istniejącego teminu:
        elif choice == '3':
                term = input('Jaki termin mam przedefiniować?: ')
                if term in geek:
                        definition = input('Jaka jest nowa definicja?: ')
                        geek[term] = definition
                        print('\nTermin', term, 'został przedefiniowany')
                else:
                        print('\nTermin', term, 'nie istnieje! Spróbuj go dodać!')

        #usunięcie pary termin-definicja
        elif choice == '4':
                term = input('Jaki termin mam usunąć?: ')
                if term in geek:
                        del geek[term]
                        print('\nOK, usunąłem termin', term)
                else:
                        print('Nie mogę tego zrobić! Terminu', term, 'nie ma w słowniku')

        #wyświetlenie kluczy słownika
        elif choice == '5':
                print(geek.keys())

        #nieznana opcja
        else:
                print('\nNiestety', choice, 'to nieprawidłowy wynik')

input("\n\nAby zakończyć program, naciśnij klawisz Enter.")