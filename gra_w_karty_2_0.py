# Gra w karty 2.0
# Demonstruje dziedziczenie - rozszerzanie klasy

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


class Talia(Reka):
    """Talia kart do gry"""
    def talia(self):
        for kolor in Karta.KOLORY:
            for karta in Karta.KARTY:
                self.dodaj(Karta(karta, kolor))

    def tasuj(self):
        import random
        random.shuffle(self.karty)

    def rozdaj(self, hands, per_hand):
        for rounds in range(per_hand):
            for hand in hands:
                if self.karty:
                    top_card = self.karty[0]
                    self.daj(top_card, hand)
                else:
                    print("Nie moge daleh rozdawać. Zabrakło kart!")


#część główna
talia1 = Talia()
print("Utworzyłem nową talię.")
print("Talia:")
print(talia1)
talia1.talia()
print('\n Dodałem do talii komplet kart.')
print("Talia:")
print(talia1)
talia1.tasuj()
print("\nPotasowałem talię kart.")
print("Talia:")
print(talia1)

moja_reka = Reka()
twoja_reka = Reka()
rece = [moja_reka, twoja_reka]

talia1.rozdaj(rece, per_hand=5)

print("\nRozdałem sobie i Tobie po 5 kart.")
print("Moja ręka:")
print(moja_reka)
print("Twoja ręka:")
print(twoja_reka)
print("Talia:")
print(talia1)

talia1.czysc()
print("\nUsunąłem zawartość talii.")

print("Talia:", talia1)
input("\n\nAby zakończyć program, naciśnij klawisz Enter.")