# Zwierzak z klasą
# Demonstruj atrybuty klasy i metody statyczne

class Critter(object):
    """Wirtualny pupil"""
    total = 0

    @staticmethod
    def status():
        print("\nOgólna liczba zwierzaków wynosi", Critter.total)

    def __init__(self, name):
        print("Urodził się zwierzak!")
        self.name = name
        Critter.total +=1

# część główna
print("Uzyskanie dostępu do atrybutu klasy Critter.total:", end=" ")
print(Critter.total)

print('Tworzenie zwierzaków')
crit1 = Critter("Zwierzak 1")
crit2 = Critter("Zwierzak 2")
crit3 = Critter("Zwierzak 3")

Critter.status()
print("Uzyskanie dostępu do atrybutu klasy poprzez obiekt:", end=" ")
print(crit1.total)

input("\n\nAby zakończyć program, naciśnij klawisz Enter.")