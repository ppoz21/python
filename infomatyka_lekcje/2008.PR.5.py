# Matura 2005

# a

def odwroc(tab):
    nowy = open('hasla_a.txt', 'w')
    for slowo in tab:
        slowo = slowo[::-1]
        nowy.writelines(slowo)
    nowy.close()


def najdluzsze(tab):
    nowy = open('slowa_a.txt', 'w')
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
    nowy.write('Najdłuższe hasło: ' + max_sl + 'Długość: ' + maxi)
    nowy.write('\nNajkrótsze hasło: ' + min_sl + 'Długość: ' + mini)
    nowy.close()


# b
def czy_palindrom(tab):
    czy = True



wczytane = open('slowa.txt', 'r')
odwroc(wczytane)
wczytane.close()
wczytane = open('slowa.txt', 'r')
najdluzsze(wczytane)
wczytane.close()
