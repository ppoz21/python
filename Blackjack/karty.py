# Moduł karty
# Podstawowe klasy do gry w karty

class Karta(object):
    """Karta do gry"""
    KARTY = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    KOLORY = ["♥", "♠", "♦", "♣"]

    def __init__(self, rank, suit, face_up = True):
        self.rank = rank
        self.suit = suit
        self.is_face_up = face_up

    def __str__(self):
        if self.is_face_up:
            rep = self.rank + self.suit
        else:
            rep = "XX"
        return rep

    def flip(self):
        self.is_face_up = not self.is_face_up

class Reka(object):
    """Ręka - wszystkie karty trzymane przez gracza"""
    def __init__(self):
        self.karty = []

    def __str__(self):
        if self.karty:
            rep = ""
            for karta in self.karty:
                rep += str(karta) + "\t"
        else:
            rep = "<pusta>"
        return rep

    def czysc(self):
        self.karty = []

    def dodaj(self, karta):
        self.karty.append(karta)

    def przekaz(self, karta, inna_reka):
        self.karty.remove(karta)
        inna_reka.dodaj(karta)

class Talia(Reka):
    """Talia kart"""
    def populacja(self):
        for suit in Karta.KOLORY:
            for rank in Karta.KARTY:
                self.dodaj(Karta(rank, suit))

    def tasuj(self):
        import random
        random.shuffle(self.karty)

    def rozdaj(self, rece, na_reke = 1):
        for rounds in range(na_reke):
            for reka in rece:
                if self.karty:
                    top_card = self.karty[0]
                    self.przekaz(top_card, reka)
                else:
                    print("nie mogę dalej rozdawać. Zabrakło kart!")

if __name__ == "__main__":
    print("To moduł zawierający klasy do gry w karty.")
    input("\n\nAby zakończyć program, naciśnij Enter.")
