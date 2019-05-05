def czy_odkryta(liczba):
    liczba = str(liczba)
    cyfry = []
    for cyfra in liczba:
        cyfry.append(int(cyfra))
    for cyfra in cyfry:
        if cyfra == 0:
            continue
        if int(liczba) % cyfra == 0:
            odkryta = True
        else:
            odkryta = False
            break
    return odkryta


wynik = czy_odkryta(12)
print(wynik)