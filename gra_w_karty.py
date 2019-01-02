# Gra w karty
# Demonstruje tworzenie kombinacji obiektów

class Karta(object):
    """Karta do gry"""
    KARTY = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    KOLORY = ["♥", "♠", "♦", "♣"]

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        rep = self.rank + self.suit
        return rep


class Reka(object):
    """Ręka - karty do gry w ręku gracza"""
    def __init__(self):
        self.karty = []

    def __str__(self):
        if self.karty:
            rep = ""
            for karta in self.karty:
                rep += str(karta) + " "
        else:
            rep = "<pusta>"
        return rep

    def czysc(self):
        self.karty = []

    def dodaj(self, karta):
        self.karty.append(karta)

    def daj(self, karta, inna_reka):
        self.karty.remove(karta)
        inna_reka.dodaj(karta)


# część główna

karta1 = Karta(rank="A", suit="♣")
print("Wyświetlam obiekt karty (klasy Card):")
print(karta1)
karta2 = Karta(rank="Q", suit="♠")
karta3 = Karta(rank="K", suit="♥")
karta4 = Karta(rank="2", suit="♦")
karta5 = Karta(rank="6", suit="♥")
print("\nWyświetlam listę obiektów po jednym na raz")
print(karta2)
print(karta3)
print(karta4)
print(karta5)

my_hand = Reka()
print("\nWyświetlam zawartość mojej ręki przed dodaniem jakichkolwiek kart:")
print(my_hand)

my_hand.dodaj(karta1)
my_hand.dodaj(karta2)
my_hand.dodaj(karta3)
my_hand.dodaj(karta4)
my_hand.dodaj(karta5)

print("\nWyświetlam zawartość mojej ręki po dodaniu 5 kart:")
print(my_hand)

twoja_reka = Reka()
my_hand.daj(karta1, twoja_reka)
my_hand.daj(karta2, twoja_reka)
print("\nPrzekazuję pierwsze dwie karty z mojej ręki do Twojej.")
print("Twoja ręka:")
print(twoja_reka)
print("Moja ręka:")
print(my_hand)

my_hand.czysc()
print("\nMoja ręka po usunięciu z niej kart:")
print(my_hand)
input("\n\nAby zakończyć program, naciśnij klawisz Enter.")