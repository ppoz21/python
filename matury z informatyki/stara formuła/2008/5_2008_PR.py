# a

def odwroc(tab):
    nowy = open('wynik\hasla_a.txt', 'w')
    for slowo in tab:
        slowo = slowo[::-1]
        nowy.write(slowo[1:]+'\n')
    nowy.close()


def najdluzsze(tab):
    nowy = open('wynik\slowa_a.txt', 'w')
    maxi = ""
    mini = ""
    max_sl = ""
    min_sl = ""
    for slowo in tab:
        maxi = len(slowo)
        max_sl = slowo
        mini = len(slowo)
        min_sl = slowo
        break
    for slowo in tab:
        if len(slowo) > maxi:
            max_sl = slowo
            maxi = len(slowo)
        if len(slowo) < mini:
            min_sl = slowo
            mini = len(slowo)
    maxi = str(maxi)
    mini = str(mini)
    nowy.write('\nNajdłuższe hasło: ' + max_sl + 'Długość: ' + maxi)
    nowy.write('\nNajkrótsze hasło: ' + min_sl + 'Długość: ' + mini)
    nowy.close()


#b
def czy_palindrom(slowo):
    if slowo == slowo[::-1]:
        return True
    else:
        return False


def szukaj_palindromu(slowo):
    if slowo == slowo[::-1]:
        return slowo
    else:
        nowe = slowo[0]
        slowo = slowo[1:]
        pom = nowe
        for litera in slowo:
            pom = pom+litera
            if czy_palindrom(pom):
                nowe = pom
            else:
                continue
        return nowe


def dlugiena12(slowo):
    if len(slowo) == 12:
        return True
    else:
        return False


def b(tab):
    nowy = open('wynik\hasla_b.txt', 'w')
    for slowo in tab:
        pal = szukaj_palindromu(slowo)
        dlugosc = len(pal)
        nowe = slowo[dlugosc:]
        odwr = nowe[::-1]
        haslo = odwr + slowo
        nowy.write(haslo[1:])
    nowy.close()
    hasla = open('wynik\hasla_b.txt', 'r')
    nowy = open('wynik\slowa_b.txt', 'w')
    liter12 = []
    for slowo in hasla:
        if dlugiena12(slowo):
            liter12.append(slowo)
    nowy.write('1. \nHasła 12-literowe: \n')
    for slowo in liter12:
        nowy.writelines(slowo)
    hasla.close()
    hasla = open('wynik\hasla_b.txt', 'r')
    maxi = ""
    mini = ""
    max_sl = ""
    min_sl = ""
    for slowo in hasla:
        maxi = len(slowo)
        max_sl = slowo
        mini = len(slowo)
        min_sl = slowo
        break
    for slowo in hasla:
        if len(slowo) == 1:
            continue
        if len(slowo) > maxi:
            max_sl = slowo
            maxi = len(slowo)
        if len(slowo) < mini:
            min_sl = slowo
            mini = len(slowo)
    maxi = str(maxi)
    mini = str(mini)
    nowy.write('\n2.\nNajdłuższe hasło: ' + max_sl + 'Długość: ' + maxi)
    nowy.write('\nNajkrótsze hasło: ' + min_sl + 'Długość: ' + mini)
    hasla.close()
    hasla = open('wynik\hasla_b.txt', 'r')
    dlugosc = 0
    for slowo in hasla:
        dlugosc += (len(slowo)-1)
    hasla.close()
    nowy.write('\n\n3.\nSuma sługości haseł: ' + str(dlugosc))
    nowy.close()


wczytane = open('dane\slowa.txt', 'r')
odwroc(wczytane)
wczytane.close()
wczytane = open('dane\slowa.txt', 'r')
najdluzsze(wczytane)
wczytane.close()
wczytane = open('dane\slowa.txt', 'r')
b(wczytane)
wczytane.close()
