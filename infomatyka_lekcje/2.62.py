def funkcja(x):
    #return (pow(x, 3) + 5*x -3)
    return (pow(x, 3) -8)


def szukanie_zerowych(p, q, e, l):
    s=(p+q)/2
    while (((funkcja(p) != 0) and (funkcja(q) !=0)) and e<=l):
        s=(p+q)/2
        if ((funkcja(p) * funkcja(q)) > 0):
            p=s
        else:
            q=s
        e+=1
    if (funkcja(p) == 0):
        return p
    if (funkcja(q) == 0):
        return q
    return s


#main
p = int(input('\nPodaj początek przedziału: '))
q = int(input('\nPodaj koniec przedziału: '))
l = int(input('\nPodaj ilość iteracji: '))
e = 0
print('Miejsce zerowe funkcji to: ')
print(szukanie_zerowych(p, q, e, l))

input('Aby zakończyć naciśnij Enter')