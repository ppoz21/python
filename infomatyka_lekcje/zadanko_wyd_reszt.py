# losowanie do pliku n-par liczb
def insert(path, n):
    import random
    file = open(path, "w")
    for i in range(n):
        number = random.randrange(1, 10)
        number = str(number)
        number = number + " "
        file.write(number)
        file.write("\n")
    file.close()


insert("waga.txt", 10)
insert("wartosc.txt", 10)
file1 = open("waga.txt", "r")
file2 = open("wartosc.txt", "r")
waga = []
wartosc = []

for linia in file1:
    waga.append(int(linia))

for linia in file2:
    wartosc.append(int(linia))

waga.sort()
waga.reverse()
wartosc.sort()
wartosc.reverse()

stosunek = []
for i in range(len(waga)):
    temp = wartosc[i]/waga[i]
    stosunek.append(temp)

print(stosunek)
