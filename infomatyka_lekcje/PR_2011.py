# liczby inaczej


def bin_to_dec(number):
    return int(number, 2)


def ile_parz(liczby):
    parz = 0
    for liczba in liczby:
        if liczba % 2 == 0:
            parz += 1
    return parz


def wart_max(liczby, liczby_bin):
    max = 0
    index = 0
    for i in range(len(liczby)):
        if liczby[i] > max:
            max = liczby[i]
            index = i
    print("Najwiksza liczba: ", max, ", binarnie: ", liczby_bin[index])
    global plik_tesktowy
    plik_tesktowy.write("Najwiksza liczba: " + str(max) + ", binarnie: " + str(liczby_bin[index]))


def ile_ma_9_cyfr(liczby):
    nowe = []
    ile = 0
    suma = 0
    for liczba in liczby:
        if len(liczba) == 10:
            ile += 1
            nowe.append(bin_to_dec(liczba))
    for x in nowe:
        suma += x
    suma_bin = int(bin(suma)[2:])
    print("Dokadnie 9 cyfr ma", ile, "liczb. Ich suma to: ", suma,", co binarnie daje: ", suma_bin)
    global plik_tesktowy
    plik_tesktowy.write("Dokadnie 9 cyfr ma " + str(ile) + " liczb. Ich suma to: " + str(suma) + ", co binarnie daje: " + str(suma_bin))

plik_tesktowy = open('zadanie6.txt', 'w')
liczby = []
liczby_dec = []
plik = open('liczby.txt', 'r')
for liczba in plik:
    liczby.append(liczba)
for liczba in liczby:
    liczby_dec.append(bin_to_dec(liczba))

print("Parzystych: ", ile_parz(liczby_dec),'\n')
plik_tesktowy.write("Parzystych: " + str(ile_parz(liczby_dec)) + '\n')
wart_max(liczby_dec, liczby)
ile_ma_9_cyfr(liczby)
