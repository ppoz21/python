#Najlepsze wyniki w.0
#Demonstruje sekwencje zagnieżdżone

scores = []

choice = None
while choice !='0':

    print(
    """
    Najlepsze wyniki 2.0
    0 - zakończ
    1 - wyświetl wyniki
    2 - dodaj wynik
    """
    )

    choice = input('Wybierasz: ')
    print()

    #zakończ
    if choice == '0':
        print('Do widzenia.')

    # wyświetl tabelę najlepszych wyników
    elif choice == '1':
        print('Najlepsze wyniki')
        print('GRACZ\t\tWYNIK')
        for entry in scores:
            score, name = entry
            print(name, '\t\t', score)

    #dodawanie wyniku
    elif choice == '2':
        name = input('Podaj nazwę gracza: ')
        score = int(input('Jaki wynik uzyskałeś?: '))
        entry = (score, name)
        scores.append(entry)
        scores.sort(reverse=True)
        scores = scores[:5] #zachowaj tylko 5 najlepszych wyników

    #niezanana opcja
    else:
        print("Niestety, ", choice, 'nie jest prawidłowym wyborem')

input('\n\nAby zakończyć program, naciśnij klawisz Enter.')