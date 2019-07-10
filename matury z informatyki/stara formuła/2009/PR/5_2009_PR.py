def szukajc(w1, w2):
    if bwa(w1, w2):
        return w1
    elif prefix(w1, w2):
        return w2 + w1[3:]
    elif sufix(w1, w2):
        return w1 + w2[3:]
    global counter
    counter += 1
    return w1 + w2


def czypalindrom(slowo):
    if slowo == slowo[::-1]:
        return True
    return False


def prefix(w1, w2):
    if w2[:3] == w1[-3:]:
        return True
    return False


def sufix(w1, w2):
    if w2[-3:] == w1[:3]:
        return True
    return False


def bwa(w1, w2):
    if w2 in w1:
        return True
    return False


plik = open('dane\dane.txt', 'r')
lista = []
counter = 0
for linia in plik:
    lista.append(linia[:-1])
palindromy = 0
b_w_a = 0
slowa = []
for linia in lista:
    spacja = linia.index(' ')
    slowo1 = linia[:spacja]
    slowo2 = linia[spacja+1:]
    if czypalindrom(slowo1):
        palindromy +=1
    if czypalindrom(slowo2):
        palindromy +=1
    if bwa(slowo1, slowo2):
        b_w_a += 1
    slowa.append(szukajc(slowo1, slowo2))
plik.close()
print('Palindromy w danych: ', palindromy)
print('Slowa B w A: ', b_w_a)
print('Par, w których możliwe tylko sklejanie: ', counter)
wynik = open('zad_5.txt', 'w')
wynik.write('Palindromy w danych: ' + str(palindromy) + '\n')
wynik.write('Slowa B w A: '+ str(b_w_a) + '\n')
wynik.write('Par, w których możliwe tylko sklejanie: ' + str(counter) + '\n')
wynik.close()
plik_slowa = open('slowa.txt', 'w')
for slowo in slowa:
    plik_slowa.writelines(slowo + '\n')
