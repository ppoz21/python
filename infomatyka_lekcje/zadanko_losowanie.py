import random


def losuj():
    zwrot = random.randrange(15, 175), random.randrange(15, 175)
    return zwrot


def nwd():
    najw_nwd = 1
    plik = open("wynik.txt", "r")
    for linia in plik:
        i = plik.readline()
        if(i[4] == ","):
            x = i[1:4]
            x = int(x)
            if(i[-5] == " "):
                y = i[-4:-2]
                y = int(y)
            else:
                y = i[-5:-2]
                y = int(y)
        else:
            x = i[1:3]
            x = int(x)
            if(i[-5] == " "):
                y = i[-4:-2]
                y = int(y)
            else:
                y = i[-5:-2]
                y = int(y)
        j = 1
        while(j <= x or j <= y):
            if(x%j == 0 and y%j == 0):
                nwd = j
            j += 1
        print("Liczby:", x, y, "NWD:", nwd)
        if(nwd > najw_nwd):
            najw_nwd = nwd

    print("\nNajwiększe NWD: ", najw_nwd)
    plik.close()


def main():
    plik = open("wynik.txt", "w")
    for i in range(50):
        x = str(losuj())
        y = x + "\n"
        plik.write(y)
    plik.close()
    nwd()

main()
