plik = open('dane/anagram.txt', 'r')
wynik_a = open('odp_4a.txt', 'w')
wynik_b = open('odp_4b.txt', 'w')
linie = []
for linia in plik:
    linie.append(linia[:-1])
print(linie)
counter = 0
for slowa in linie:
    new = slowa.split(' ')
    if len(new[0]) == len(new[1]) and len(new[1]) == len(new[2]) and len(new[2]) == len(new[3]) and len(new[3]) == len(new[4]):
        for slowo in new:
            wynik_a.write(slowo+' ')
        wynik_a.write("\n")
        if sorted(new[0]) == sorted(new[1]) and sorted(new[0]) == sorted(new[2]) and sorted(new[0]) == sorted(new[3]) and sorted(new[0]) == sorted(new[4]):
            for slowo in new:
                wynik_b.write(slowo + ' ')
            wynik_b.write("\n")
        counter += 1
plik.close()
wynik_a.close()
wynik_b.close()
print(counter)
