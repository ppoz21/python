#Pozwól, że policzę
#program wyświetla liczby z ciągu arytmetycznego

poczatek = int(input("Podaj 1 wyraz ciągu artymetycznego: "))
koniec = int(input("Podaj ostatni ciągu arytmetycznego: "))
odstep = int(input("Podaj różnicę ciągu ciągu: "))

for liczba in range(poczatek, koniec+1, odstep):
    print(liczba)

input("Naciśnij enter")