def palindrom(slowo):
    if slowo == slowo[::-1]:
        return True
    return False


plik = open('dane\dane.txt', 'r')
wynik = open('zadanie4.txt', 'w')
slowa = []
for slowo in plik:
    slowa.append(slowo[:-1])
for slowo in slowa:
    if palindrom(slowo):
        wynik.write(slowo+'\n')
plik.close()
wynik.close()
